#!/usr/bin/env python3

import pycouchdb
import requests
import sys
import xml.etree.ElementTree as ET

def usage():
    print("usage: ./parser.py <NETXML-FILE>")

def extract_ssid_data(rawdata):
    """Extract relevant SSID data from given XML-node.

    This data contains per SSID: maximum data rate, encryption modes and ESSID.
    """

    if not isinstance(rawdata,ET.Element):
        raise TypeError("given rawdata not an ElementTree-element")

    ssiddata = {}
    maxrate = rawdata.find('max-rate').text
    ssiddata['max-rate'] = float(maxrate)

    encryption_modes = rawdata.findall('encryption')
    enctxt = []
    for enc in encryption_modes:
        enctxt.append(enc.text)
        ssiddata['encryption'] = enctxt

    ssiddata['essid'] = rawdata.find('essid').text

    return ssiddata

def extract_snr_info(rawdata):
    """Extract relevant radio signal data from given XML-node.

    This data contains minimum and maximum levels of the signal and noise.
    """
    if not isinstance(rawdata,ET.Element):
        raise TypeError("given rawdata not an ElementTree-element")

    snrinfo = {}
    data = rawdata.find('min_signal_dbm').text
    snrinfo['min_signal_dbm'] = int(data)
    data = rawdata.find('min_noise_dbm').text
    snrinfo['min_noise_dbm'] = int(data)
    data = rawdata.find('min_signal_rssi').text
    snrinfo['min_signal_rssi'] = int(data)
    data = rawdata.find('min_noise_rssi').text
    snrinfo['min_noise_rssi'] = int(data)

    data = rawdata.find('max_signal_dbm').text
    snrinfo['max_signal_dbm'] = int(data)
    data = rawdata.find('max_noise_dbm').text
    snrinfo['max_noise_dbm'] = int(data)
    data = rawdata.find('max_signal_rssi').text
    snrinfo['max_signal_rssi'] = int(data)
    data = rawdata.find('max_noise_rssi').text
    snrinfo['max_noise_rssi'] = int(data)

    return snrinfo


def extract_gps_info(rawdata):
    """Extract relevant GPS data from given XML-node.

    This data contains the coordinates of the minimum, maximum and peak
    signal level.
    """

    if not isinstance(rawdata,ET.Element):
        raise TypeError("given rawdata not an ElementTree-element")

    gpsinfo = {}
    data = rawdata.find('min-lat').text
    gpsinfo['min-lat'] = float(data)
    data = rawdata.find('min-lon').text
    gpsinfo['min-lon'] = float(data)
    data = rawdata.find('max-lat').text
    gpsinfo['max-lat'] = float(data)
    data = rawdata.find('max-lon').text
    gpsinfo['max-lon'] = float(data)
    data = rawdata.find('peak-lat').text
    gpsinfo['peak-lat'] = float(data)
    data = rawdata.find('peak-lon').text
    gpsinfo['peak-lon'] = float(data)

    return gpsinfo

def calcuate_uid_index(db):
    mapfunction = "function(doc) {\
    var bssid, essid, uid, value;\
    if (doc.ssid.essid && doc.bssid) {\
        uid = [doc.bssid];\
        value = doc;\
        delete value['_id'];\
        delete value['_rev'];\
        names = [];\
        for (id in doc.ssid) {\
            names.push(id['essid']);\
        }\
        uid.push(names);\
        emit(uid, value);\
    }\
}"
    print(list(db.temporary_query(mapfunction)))

# only call if executed as script
if __name__ == '__main__':
    if 2 != len(sys.argv):
        usage()
        sys.exit(1)

    # assume default config for couchdb
    server = pycouchdb.Server()
    try:
        server.info()
    except requests.exceptions.ConnectionError:
        sys.stderr.write("connecting to server failed\n")
        sys.exit(1)
    # assume databasename, if database does not exists, create it
    dbname = "wifinetworks"
    try:
        db = server.database(dbname)
    except pycouchdb.exceptions.NotFound:
        print("database '"+dbname+"' does not exist, creating one ...")
        server.create(dbname)
        db = server.database(dbname)
    newdoccounter = 0

    tree = ET.ElementTree()
    try:
        tree = ET.parse(sys.argv[1])
    except FileNotFoundError:
        sys.stderr.write("opening file failed\n")
    root = tree.getroot()
    for network in tree.findall('wireless-network'):
        networkdata = {}
        # only handle fixed networks, ignore probes etc.
        if "infrastructure" == network.attrib['type']:
            # extract the data
            ssids = network.findall('SSID')
            ssiddata = []
            for ssidnode in ssids:
                ssiddata.append( extract_ssid_data(ssidnode) )
            networkdata['ssid'] = ssiddata
            networkdata['bssid'] = network.find('BSSID').text
            networkdata['snr-info'] = extract_snr_info( network.find('snr-info') )
            networkdata['gps-info'] = extract_gps_info( network.find('gps-info') )
            # push it into couchdb
            doc = db.save(networkdata)
            newdoccounter += 1
    print(str(newdoccounter) + " new networks added")
    calcuate_uid_index(db)

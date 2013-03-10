#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as ET

def usage():
    print("usage: ./parser.py <NETXML-FILE>")

# only call if executed as script
if __name__ == '__main__':
    if 2 != len(sys.argv):
        usage()
        sys.exit(1)

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
            ssids = network.findall('SSID')
            ssiddata = {}
            for ssid in ssids:
                maxrate = ssid.find('max-rate').text
                ssiddata['max-rate'] = float(maxrate)

                encryption_modes = ssid.findall('encryption')
                enctxt = []
                for enc in encryption_modes:
                    enctxt.append(enc.text)
                ssiddata['encryption'] = enctxt

                allessids = ssid.findall('essid')
                ids = []
                for essid in allessids:
                    ids.append(essid.text)
                ssiddata['essid'] = ids
            networkdata['ssid'] = ssiddata

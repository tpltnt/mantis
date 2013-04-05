import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *


def pytest_addoption(parser):
    parser.addini("dbusername", "CouchDB username")
    parser.addini("dbpassword", "CouchDB password")
    parser.addini("dbname", "CouchDB name")
    parser.addini("host", "host (name or IP) on which the CouchDB is running")
    parser.addini("port", "port number CouchDB listens on")


@pytest.fixture(scope="module")
def plainmantis():
    return Mantis()


#@pytest.fixture(scope="module")
@pytest.fixture
def authmantis(pytestconfig):
    return Mantis(
        username=pytestconfig.getini('dbusername'),
        password=pytestconfig.getini('dbpassword'))


@pytest.fixture(scope="module")
def et_networknode():
    tree = ET.ElementTree()
    try:
        tree = ET.parse('./tests/minimal.netxml')
    except FileNotFoundError:
        raise FileNotFoundError("netxml file not found")
    root = tree.getroot()
    return tree.findall('wireless-network')[1]


@pytest.fixture(scope="module")
def et_ssid_node(et_networknode):
    return et_networknode.find('SSID')


@pytest.fixture(scope="module")
def et_gps_node(et_networknode):
    return et_networknode.find('gps-info')


@pytest.fixture(scope="module")
def et_snr_node(et_networknode):
    return et_networknode.find('snr-info')


@pytest.fixture(scope="module")
def et_empty():
    tree = ET.ElementTree()
    return tree.getroot()


@pytest.fixture(scope="module")
def et_one_node():
    tree = ET.ElementTree()
    tree = ET.parse('./tests/onenode.xml')
    return tree.getroot()

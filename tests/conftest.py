import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

@pytest.fixture(scope="module")
def plainmantis():
    return Mantis()

@pytest.fixture(scope="module")
def et_ssidnode():
    tree = ET.ElementTree()
    try:
        tree = ET.parse('./tests/minimal.netxml')
    except FileNotFoundError:
        raise FileNotFoundError("netxml file not found")
    root = tree.getroot()
    network = tree.findall('wireless-network')[1]
    return network.find('SSID')

@pytest.fixture(scope="module")
def et_empty():
    tree = ET.ElementTree()
    return tree.getroot()

@pytest.fixture(scope="module")
def et_one_node():
    tree = ET.ElementTree()
    tree = ET.parse('./tests/onenode.xml')
    return tree.getroot()

import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

@pytest.fixture(scope="module")
def plainmantis():
    return Mantis()

@pytest.fixture(scope="module")
def et_ssidnode(mantis):
    foomantis = Mantis()
    tree = ET.ElementTree()
    try:
        tree = ET.parse('./tests/minimal.netxml')
    except FileNotFoundError:
        raise FileNotFoundError("netxml file not found")
    root = tree.getroot()
    network = tree.findall('wireless-network')[1]
    return network.find('SSID')

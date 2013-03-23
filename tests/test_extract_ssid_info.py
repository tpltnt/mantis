import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

def test_empty(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_info()

def test_float(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_info(2.3)

def test_int(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_info(42)

def test_string(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_info('foo')

def test_minimalfile(plainmantis,et_ssidnode):
    info = {'max-rate': 54.0, 'essid': 'WLAN', 'encryption': ['WPA+TKIP', 'WPA+PSK']}
    assert info == plainmantis.extract_ssid_info(et_ssidnode)

def test_emptyfile(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_info('./tests/empty.xml')

def test_empty_et(plainmantis,et_empty):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_info(et_empty)

def test_empty_et(plainmantis,et_one_node):
    with pytest.raises(AttributeError):
        plainmantis.extract_ssid_info(et_one_node)

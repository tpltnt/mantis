import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

def test_empty(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_data()

def test_float(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_data(2.3)

def test_int(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_data(42)

def test_string(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_ssid_data('foo')

def test_minimalfile(plainmantis,et_ssidnode):
    plainmantis.extract_ssid_data(et_ssidnode)

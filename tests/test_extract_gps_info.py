import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

def test_empty(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_gps_info()

def test_float(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_gps_info(2.3)

def test_int(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_gps_info(42)

def test_string(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_gps_info('foo')

def test_minimalfile(plainmantis,et_gps_node):
    info = {'peak-lat': 23.374794, 'max-lat': 23.375094, 'peak-lon': 8.125922, 'min-lat': 23.374236, 'max-lon': 8.126414, 'min-lon': 8.125497}
    assert info == plainmantis.extract_gps_info(et_gps_node)

def test_emptyfile(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_gps_info('./tests/empty.xml')

def test_empty_et(plainmantis,et_empty):
    with pytest.raises(TypeError):
        plainmantis.extract_gps_info(et_empty)

def test_empty_et(plainmantis,et_one_node):
    with pytest.raises(AttributeError):
        plainmantis.extract_gps_info(et_one_node)

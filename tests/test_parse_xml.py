import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

# adjust accordung to your configuration
USERNAME = 'username'
PASSWORD = 'password'

@pytest.fixture
def mantis():
    return Mantis(username=USERNAME,password=PASSWORD)

def test_empty(mantis):
    with pytest.raises(TypeError):
        mantis.parse_xml()

def test_float(mantis):
    with pytest.raises(TypeError):
        mantis.parse_xml(2.3)

def test_int(mantis):
    with pytest.raises(TypeError):
        mantis.parse_xml(42)

def test_nonexistent(mantis):
    with pytest.raises(ValueError):
        mantis.parse_xml('/i/do/not/exist')

def test_minimalfile(mantis):
    mantis.parse_xml('./tests/minimal.netxml')

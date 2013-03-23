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

import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

@pytest.fixture(scope="module")
def plainmantis():
    return Mantis()

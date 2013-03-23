import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

# adjust accordung to your configuration
USERNAME = 'username'
PASSWORD = 'password'

def test_contructor_empty():
    foo = Mantis()

def test_constructor_invalid_keyword():
    with pytest.raises(TypeError):
        foo = Mantis(bar='baz')

def test_username_and_password():
    foo = Mantis(username=USERNAME,password=PASSWORD)

def test_username_only():
    with pytest.raises(ValueError):
        foo = Mantis(username=USERNAME)

def test_password_only():
    with pytest.raises(ValueError):
        foo = Mantis(password=PASSWORD)

def test_no_username_and_password():
    foo = Mantis()


import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *


# adjust accordung to your configuration
USERNAME = 'username'
PASSWORD = 'password'
HOSTNAME = 'testhost'
PORT = 5984
DBNAME = 'testdb'


def test_contructor_empty():
    foo = Mantis()


def test_constructor_invalid_keyword():
    with pytest.raises(TypeError):
        foo = Mantis(bar='baz')


def test_username_and_password():
    foo = Mantis(username=USERNAME, password=PASSWORD)


def test_username_only():
    with pytest.raises(ValueError):
        foo = Mantis(username=USERNAME)


def test_password_only():
    with pytest.raises(ValueError):
        foo = Mantis(password=PASSWORD)


def test_wrong_username_and_password():
    with pytest.raises(pycouchdb.exceptions.AuthenticationFailed):
        foo = Mantis(username='807a7ac9', password='f3beeef72b')


def test_no_username_and_password():
    foo = Mantis()


def test_hostname():
    foo = Mantis(host=HOSTNAME)


def test_portnumber():
    foo = Mantis(port=PORT)


def test_port_too_low():
    with pytest.raises(ValueError):
        foo = Mantis(port=-1)


def test_port_too_high():
    with pytest.raises(ValueError):
        foo = Mantis(port=66535)


def test_sourcefile_float():
    with pytest.raises(TypeError):
        foo = Mantis(sourcefile=2.3)


def test_nonexistent_sourcefile():
    with pytest.raises(ValueError):
        foo = Mantis(sourcefile='/i/do/not/exit')


def test_sourcefile():
    foo = Mantis(sourcefile='./tests/minimal.netxml')


def test_dbname():
    foo = Mantis(username=USERNAME, password=PASSWORD, dbname=DBNAME)


def test_unauth_dbname():
    with pytest.raises(pycouchdb.exceptions.AuthenticationFailed):
        foo = Mantis(username='807a7ac9', password='f3beeef72b', dbname=DBNAME)

# test for valid, but non-admin user needed -> pycouchdb.exceptions.Conflict

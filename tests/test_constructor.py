import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *


def test_contructor_empty():
    foo = Mantis()


def test_constructor_invalid_keyword():
    with pytest.raises(TypeError):
        foo = Mantis(bar='baz')


def test_username_and_password(pytestconfig):
    foo = Mantis(
        username=pytestconfig.getini('dbusername'),
        password=pytestconfig.getini('dbpassword'))


def test_username_only(pytestconfig):
    with pytest.raises(ValueError):
        foo = Mantis(username=pytestconfig.getini('dbusername'))


def test_password_only(pytestconfig):
    with pytest.raises(ValueError):
        foo = Mantis(password=pytestconfig.getini('dbpassword'))


def test_wrong_username_and_password():
    with pytest.raises(pycouchdb.exceptions.AuthenticationFailed):
        foo = Mantis(username='807a7ac9', password='f3beeef72b')


def test_no_username_and_password():
    foo = Mantis()


def test_hostname(pytestconfig):
    foo = Mantis(host=pytestconfig.getini('host'))


def test_portnumber(pytestconfig):
    foo = Mantis(port=pytestconfig.getini('port'))


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


def test_dbname(pytestconfig):
    foo = Mantis(
        username=pytestconfig.getini('dbusername'),
        password=pytestconfig.getini('dbpassword'),
        dbname=pytestconfig.getini('dbname'))


def test_unauth_dbname(pytestconfig):
    with pytest.raises(pycouchdb.exceptions.AuthenticationFailed):
        foo = Mantis(username='807a7ac9', password='f3beeef72b',
                     dbname=pytestconfig.getini('dbname'))

# test for valid, but non-admin user needed -> pycouchdb.exceptions.Conflict

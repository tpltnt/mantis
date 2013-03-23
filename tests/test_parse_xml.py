import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *


def test_empty(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.parse_xml()


def test_float(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.parse_xml(2.3)


def test_int(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.parse_xml(42)


def test_nonexistent(plainmantis):
    with pytest.raises(ValueError):
        plainmantis.parse_xml('/i/do/not/exist')


def test_minimalfile(plainmantis):
    assert 1 == plainmantis.parse_xml('./tests/minimal.netxml')

import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *


def test_plain_empty(plainmantis):
    with pytest.raises(BaseException):
        plainmantis.deflate()


def test_plain_string(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.deflate('foo')

#def test_auth_empty(authmantis):
#    authmantis.deflate()


def test_auth_string(authmantis):
    with pytest.raises(TypeError):
        authmantis.deflate('foo')

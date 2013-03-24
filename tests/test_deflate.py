import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

pytest.fail("not implmenented")


def test_empty(plainmantis):
    plainmantis.deflate()


def test_string(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.deflate('foo')

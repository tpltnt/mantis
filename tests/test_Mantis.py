import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

def test_contructor_empty():
    foo = Mantis()

def test_constructor_non_keyword():
    with pytest.raises(TypeError):
        foo = Mantis(bar='baz')

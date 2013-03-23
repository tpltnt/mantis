import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

def test_empty_contructor():
    foo = Mantis()

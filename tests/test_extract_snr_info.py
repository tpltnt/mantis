import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *

pytest.fail("not implmenented")


def test_empty(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_data()


def test_float(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_data(2.3)


def test_int(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_data(42)


def test_string(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_data('foo')


def test_minimalfile(plainmantis, et_snr_node):
    data = {'max-rate': 54.0, 'esnr': 'WLAN',
            'encryption': ['WPA+TKIP', 'WPA+PSK']}
    assert data == plainmantis.extract_snr_data(et_snr_node)


def test_emptyfile(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_data('./tests/empty.xml')


def test_empty_et(plainmantis, et_empty):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_data(et_empty)


def test_empty_et(plainmantis, et_one_node):
    with pytest.raises(AttributeError):
        plainmantis.extract_snr_data(et_one_node)

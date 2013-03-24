import sys
sys.path.append('../mantis')
import pytest
from kismetlogparser import *


def test_empty(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_info()


def test_float(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_info(2.3)


def test_int(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_info(42)


def test_string(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_info('foo')


def test_minimalfile(plainmantis, et_snr_node):
    data = {'max_noise_rssi': 0, 'min_noise_dbm': -80,
            'max_signal_rssi': 0, 'min_signal_dbm': -93,
            'min_signal_rssi': 824, 'min_noise_rssi': 824,
            'max_noise_dbm': 39, 'max_signal_dbm': -68}
    assert data == plainmantis.extract_snr_info(et_snr_node)


def test_emptyfile(plainmantis):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_info('./tests/empty.xml')


def test_empty_et(plainmantis, et_empty):
    with pytest.raises(TypeError):
        plainmantis.extract_snr_info(et_empty)


def test_empty_et(plainmantis, et_one_node):
    with pytest.raises(AttributeError):
        plainmantis.extract_snr_info(et_one_node)

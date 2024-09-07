"""
Test main
"""
from tenda_everest import info


def test_info():
    """
    Test info
    :return: None
    """
    info_expected_text = 'First steps with TendaEverest'
    assert info() == info_expected_text

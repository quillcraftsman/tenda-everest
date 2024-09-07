"""
Fixtures for testing
"""
# import requests
from pytest import fixture
from testing.test_tenda_everest import mocks


@fixture
def requests_module():
    """
    fixture for requests test module
    """
    # return requests
    return mocks


@fixture
def host():
    """
    fixture for test host
    """
    return '9.9.9.9'
    # return 'http://10.173.1.142:8081'

# import requests
import testing.test_tenda_everest.mocks as mocks
from pytest import fixture


@fixture
def requests_module():
    # return requests
    return mocks

@fixture
def host():
    return '9.9.9.9'
    # return 'http://10.173.1.142:8081'

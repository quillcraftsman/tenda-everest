"""
Mocks for requests python module
"""
from tenda_everest import MODULES
from testing.test_tenda_everest.mocks.expected import expected_info

class MockResponse:
    """
    Mock for requests.Response class
    """

    def __init__(self, url):
        """
        Init mock response
        """
        self.modules = self.get_modules(url)

    def json(self):
        """
        mock request.json function
        """
        result = {}
        for module in self.modules:
            enum_module = MODULES[module]
            value = expected_info[enum_module]
            result.update(value)

        return result


    def get_modules(self, url):
        """
        special function for mock
        """
        _, params = url.split('?')
        _, values = params.split('=')
        modules = values.split(',')
        return modules


class MockSession:
    """
    Mock requests.Session class
    """

    def get(self, url, *args, **kwargs):  # pylint:disable=unused-argument
        """
        mock get request
        """
        return MockResponse(url)

    def post(self, *args, **kwargs):
        """
        mock post request
        """


def session():
    """
    mock request.session function
    """
    return MockSession()

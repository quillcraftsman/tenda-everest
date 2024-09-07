from tenda_everest import MODULES
from testing.test_tenda_everest.mocks.expected import expected_info

class MockResponse:

    def __init__(self, url):
        self.modules = self.get_modules(url)

    def json(self):
        result = {}
        for module in self.modules:
            enum_module = MODULES[module]
            value = expected_info[enum_module]
            result.update(value)

        return result

    def get_modules(self, url):
        host, params = url.split('?')
        module, values = params.split('=')
        modules = values.split(',')
        return modules


class MockSession:

    def get(self, url, *args, **kwargs):
        return MockResponse(url)

    def post(self, *args, **kwargs):
        pass

def session():
    return MockSession()

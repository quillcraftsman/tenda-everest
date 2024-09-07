"""
Test main
"""
from tenda_everest import login, get_info, request_firmware, MODULES
from tenda_everest.main import get_request_urls
from testing.test_tenda_everest.mocks.expected import expected_info


def test_get_request_urls_default():
    """
    test default usage
    """
    assert ['getStatus'] == get_request_urls()

def test_get_request_urls_no_modules():
    """
    test when no modules
    """
    urls = get_request_urls(firmware='V12.01.01.33_multi')
    assert ['getStatus'] == urls

def test_get_request_urls_multi():
    """
    Test for multi firmware
    """
    modules = [
        MODULES.systemInfo,
        MODULES.wifiBasicCfg,
        MODULES.wanBasicCfg,
        MODULES.dmz,  # unknown,
        MODULES.softWare,
    ]
    urls = get_request_urls(firmware='V12.01.01.33_multi', modules=modules)

    expected_result = [
        'getStatus',
        'getWifi',
        'getWAN',
        'getStatus',
        'getSysTools',
    ]

    assert urls == expected_result


def test_get_info(requests_module, host):
    """
    Test for get_info
    """
    # login
    session = login(requests_module, host)

    # request_firmware

    firmware = request_firmware(host, session)
    assert firmware == 'V02.03.01.125'

    info = get_info(
        host,
        session,
        modules=(
            MODULES.systemInfo,
            MODULES.wanBasicCfg,
            MODULES.wifiBasicCfg,
        )
    )

    expected_result = {}
    expected_result.update(expected_info[MODULES.systemInfo])
    expected_result.update(expected_info[MODULES.wanBasicCfg])
    expected_result.update(expected_info[MODULES.wifiBasicCfg])

    # del expected_result['systemInfo']['wanConnectTime']
    # del info['systemInfo']['wanConnectTime']

    assert expected_result == info

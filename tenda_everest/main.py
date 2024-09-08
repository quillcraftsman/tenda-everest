"""
Main module
"""
from enum import Enum, verify, UNIQUE, auto

DEFAULT_FIRMWARE = 'V02.03.01.125'

def login(requests, host):
    """
    Info
    """
    session = requests.session()

    url = '/login/Auth'

    referer = f'{host}/login.html'

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) '
                      'Gecko/20100101 Firefox/130.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
                  'image/avif,image/webp,image/png,image/svg+xml,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Connection': 'keep-alive',
        'Referer': referer

    }

    data = {
        'password': "YWRtaW4="  # admin coded in base64
    }

    request_url = f'{host}{url}'

    session.post(
        url=request_url,
        headers=headers,
        data=data
    )

    return session

# pylint:disable=invalid-name
@verify(UNIQUE)
class MODULES(Enum):
    """
    Available modules
    """
    systemInfo = auto()
    wifiBasicCfg = auto()
    wanBasicCfg = auto()
    softWare = auto()
    wifiBeamforming = auto()
    onlineList = auto()
    hasNewSoftVersion = auto()
    portList = auto()
    sysTime = auto()
    wifiRelay = auto()
    parentAccessCtrl = auto()
    ipv6Status = auto()
    LEDControl = auto()
    ping = auto()
    wifiTime = auto()
    parentCtrlList = auto()
    macFilter = auto()
    internetStatus = auto()
    IPTV = auto()
    guestList = auto()
    lan6Cfg = auto()
    wan6BasicCfg = auto()
    ipv6Enable = auto()
    deviceStatistics = auto()
    lanCfg = auto()
    wanAdvCfg = auto()
    productInfo = auto()
    wpsModule = auto()
    upnp = auto()
    wifiAdvCfg = auto()
    staticIPList = auto()
    isWifiClients = auto()
    localhost = auto()
    wifiGuest = auto()
    wifiWPS = auto()
    remoteWeb = auto()
    dmz = auto()
    wifiPower = auto()
    loginAuth = auto()
    ddns = auto()


def get_request_urls(firmware=DEFAULT_FIRMWARE, modules=None):
    """
    get different urls for request
    """
    # if firmware == 'V12.01.01.33_multi':
    if 'multi' in firmware:
        module_urls = {
            MODULES.systemInfo: 'getStatus',
            MODULES.wanBasicCfg: 'getWAN',
            MODULES.wifiBasicCfg: 'getWifi',
            MODULES.softWare: 'getSysTools',
        }
        result = []
        if modules:
            for module in modules:
                if module in module_urls:
                    result.append(module_urls[module])
                else:
                    result.append('getStatus')
        else:
            result.append('getStatus')
        return result

    return ['getStatus']


def get_info(host, session, modules=(MODULES.systemInfo,), firmware=DEFAULT_FIRMWARE):
    """
    Get info using different modules
    """
    available_modules = [module.name for module in modules]
    modules_str = ','.join(list(available_modules))

    request_urls = get_request_urls(firmware, modules)

    result = {}
    for url_item in request_urls:

        url = f'/goform/{url_item}?modules={modules_str}'

        headers = {
            'User-Agent':
                'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:130.0) Gecko/20100101 Firefox/130.0',
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.5',
        }

        request_url = f'{host}{url}'

        cookies = {
            'bLanguage': 'en',
            'ecos_pw': 'ecos_pw=YWRtaW4=wdv:language=cn'  # admin in base64
        }

        response = session.get(
            url=request_url,
            headers=headers,
            cookies=cookies,
        )

        result.update(response.json())

    return result

def request_firmware(host, session):
    """
    Request router current firmware
    """
    info = get_info(host, session, modules=(MODULES.systemInfo,))
    return info['systemInfo']['softVersion']

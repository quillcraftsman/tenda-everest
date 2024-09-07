"""
Expected values for tests
"""
from tenda_everest import MODULES

HIDDEN_MAC = 'XX:XX:XX:XX:XX:XX'
HIDDEN_DNS = 'XX.XX.XXX.XXX'
HIDDEN_KEY = '********'
HIDDEN_USER = 'user'
HIDDEN_SSID = 'SSID'

expected_systemInfo = {
    'systemInfo': {
        'lanIP': '192.168.0.1',
        'lanMask': '255.255.255.0',
        'macHost': HIDDEN_MAC,
        'softVersion': 'V02.03.01.125',
        'statusWanDns1': HIDDEN_DNS,
        'statusWanDns2': '1.1.1.1',
        'statusWanGaterway': '10.173.255.1',
        'statusWanIP': '10.173.1.142',
        'statusWanMAC': HIDDEN_MAC,
        'statusWanMask': '255.255.255.254',
        'wanConnectTime': '66039',
        'wanType': 'pppoe'
    }
}

expected_wanBasicCfg = {
    'wanBasicCfg': {
         'wanDns1': HIDDEN_DNS,
         'wanDns2': '1.1.1.1',
         'wanGateway': '10.173.255.1',
         'wanIP': '10.173.1.142',
         'wanMask': '255.255.255.254',
         'wanPPPoEPwd': HIDDEN_KEY,
         'wanPPPoEUser': HIDDEN_USER,
         'wanType': 'pppoe'
    }
}

expected_wifiBasicCfg = {
    'wifiBasicCfg': {
        'HasDoubleBandUnity': 'true',
        'doubleBandUnityEnable': 'false',
        'wifiEn': 'true',
        'wifiEn_5G': 'true',
        'wifiHideSSID': 'false',
        'wifiHideSSID_5G': 'false',
        'wifiNoPwd': 'false',
        'wifiNoPwd_5G': 'false',
        'wifiPwd': HIDDEN_KEY,
        'wifiPwd_5G': HIDDEN_KEY,
        'wifiSSID': HIDDEN_SSID,
        'wifiSSID_5G': HIDDEN_SSID,
        'wifiSecurityMode': 'WPAWPA2/AES',
        'wifiSecurityMode_5G': 'WPAWPA2/AES',
        'wifiTotalEn': 'true'
    }
}

expected_info = {
    MODULES.systemInfo: expected_systemInfo,
    MODULES.wanBasicCfg: expected_wanBasicCfg,
    MODULES.wifiBasicCfg: expected_wifiBasicCfg
}

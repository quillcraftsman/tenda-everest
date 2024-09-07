from tenda_everest import MODULES

hidden_mac = 'XX:XX:XX:XX:XX:XX'
hidden_dns = 'XX.XX.XXX.XXX'
hidden_key = '********'
hidden_user = 'user'
hidden_ssid = 'SSID'

expected_systemInfo = {
    'systemInfo': {
        'lanIP': '192.168.0.1',
        'lanMask': '255.255.255.0',
        'macHost': hidden_mac,
        'softVersion': 'V02.03.01.125',
        'statusWanDns1': hidden_dns,
        'statusWanDns2': '1.1.1.1',
        'statusWanGaterway': '10.173.255.1',
        'statusWanIP': '10.173.1.142',
        'statusWanMAC': hidden_mac,
        'statusWanMask': '255.255.255.254',
        'wanConnectTime': '66039',
        'wanType': 'pppoe'
    }
}

expected_wanBasicCfg = {
    'wanBasicCfg': {
         'wanDns1': hidden_dns,
         'wanDns2': '1.1.1.1',
         'wanGateway': '10.173.255.1',
         'wanIP': '10.173.1.142',
         'wanMask': '255.255.255.254',
         'wanPPPoEPwd': hidden_key,
         'wanPPPoEUser': hidden_user,
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
        'wifiPwd': hidden_key,
        'wifiPwd_5G': hidden_key,
        'wifiSSID': hidden_ssid,
        'wifiSSID_5G': hidden_ssid,
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

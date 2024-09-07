"""
Quickstart examples
"""


def main():
    """
    TendaEverest simple usage
    :return:
    """
    import pprint  # pylint: disable=import-outside-toplevel
    import requests  # pylint: disable=import-outside-toplevel
    from tenda_everest import login, get_info, MODULES, request_firmware  # pylint: disable=import-outside-toplevel

    host = 'http://192.168.0.1:8081'  # There is device located

    session = login(requests, host)  # connect to device and login

    firmware = request_firmware(host, session)  # check router firmware
    print(firmware)

    modules = (  # What do you want to know
        MODULES.systemInfo,
        MODULES.wanBasicCfg,
        MODULES.wifiBasicCfg,
        MODULES.softWare,
    )

    info = get_info(host, session, modules, firmware=firmware)

    pprint.pprint(info)

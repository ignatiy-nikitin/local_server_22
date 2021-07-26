import os

import configparser
from re import L


CONFIG_FILE = 'config.ini'
CONFIG_PARAMS = ('postresql_port', 'waitress_port')

CONFIG = configparser.ConfigParser()
CONFIG.read(CONFIG_FILE)


def _is_config_file_exists():
    if not os.path.isfile(CONFIG_FILE):
        return False
    return True


def _check_settings_section():
    try:
        CONFIG['SETTINGS']
    except KeyError:
        return False
    return True


def _check_config_params():
    CONFIG_SETTINGS = CONFIG['SETTINGS']
    params_not_ok = []
    for param in CONFIG_PARAMS:
        if not CONFIG_SETTINGS[param]:
            params_not_ok.append(param)
    params_not_ok


def _set_config_params():
    CONFIG.add_section('SETTINGS')
    CONFIG.set('SETTINGS', 'postresql_port', '5439')
    CONFIG.set('SETTINGS', 'waitress_port', '8000')
    with open(CONFIG_FILE, 'w') as file_:
        CONFIG.write(file_)


def _check_ports():
    CONFIG_SETTINGS = CONFIG['SETTINGS']
    ports_not_int = []
    for param in CONFIG_PARAMS:
        try:
            int(CONFIG_SETTINGS[param])
        except ValueError:
            ports_not_int.append(param)
    return ports_not_int


def get_postgresql_port():
    return int(CONFIG['SETTINGS']['postresql_port'])


def get_waitress_port():
    return int(CONFIG['SETTINGS']['waitress_port'])


def check_config():
    if not _is_config_file_exists():
        _set_config_params()
        return True, 'ok1'
    if not _check_settings_section():
        _set_config_params()
        return True, 'ok2'
    params_not_ok = _check_config_params()
    if params_not_ok:
        return False, "Сan't find config parameters: " + ', '.join(params_not_ok) + '. Fill them and restart'
    ports_not_int = _check_ports()
    if ports_not_int:
        return False, "The following ports have invalid values: " + ', '.join(ports_not_int) + ". Port must be an integer"
    return True, 'ok3'


# def get_ports():
#     return int(CONFIG['SETTINGS']['postresql_port']), int(CONFIG['SETTINGS']['waitress_port'])

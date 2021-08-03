from custom_config import CustomConfig, CustomConfigException

HOST = '127.0.0.1'
CONFIG_FILE = 'config.ini'

CONFIG_SETTINGS = {
    'SETTINGS': {
        'postresql_port': {
            'type': int,
            'default': 5439,
        },
        'waitress_port': {
            'type': int,
            'default': 8000,
        },
    }
}

try:
    config = CustomConfig(CONFIG_FILE, CONFIG_SETTINGS)
except CustomConfigException as e:
    print(f'Config error: {e}')
    exit()

POSTGRES_PORT = config['SETTINGS']['postresql_port']
WAITRESS_PORT = config['SETTINGS']['waitress_port']

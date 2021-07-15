from config import check_config, get_ports
import socket


HOST = '127.0.0.1'
CONFIG_FILE = 'config.ini'


def is_port_open(ip, port):
   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   try:
      s.connect((ip, port))
      s.shutdown(2)
      return True
   except:
      return False


def ports_check():   
    print('-- Port Check --')
    print('Checking config file...')
    config_checking_result, message = check_config()
    if not config_checking_result:
        print('Error in config file:')
        print(message)
        print('Fix problem in config.ini file and restart program')
        return False
    print('Checking file is ok')

    postresql_port, waitress_port = get_ports()

    print('Checking PostreSQL port...')
    if is_port_open(HOST, postresql_port):
        print('PostreSQL port is busy. Go to config.ini, change it and restart program')
        return False
    print('Checking Waitress port...')
    if is_port_open(HOST, postresql_port):
        print('Waitress port is busy. Go to config.ini, change it and restart program')
        return False

    print('Ports are ok')
    return True

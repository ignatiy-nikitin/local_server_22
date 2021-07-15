from port_check import ports_check
from config import get_ports
from waitress import serve

from server import create_app



HOST = '127.0.0.1'

if not ports_check():
    exit()

port = get_ports()[1]

print('-- Waitress --')
app = create_app()
print(f'Running server onn host {HOST} on port {port}...')
serve(app, host=HOST, port=port)
print('Server stopped')
input()
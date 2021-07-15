from database import create_database
import os

from port_check import ports_check
from config import get_ports
from waitress import serve

from server import create_app



HOST = '127.0.0.1'

if not ports_check():
    exit()

print('-- Start PostgreSQL --')
os.system('install.bat')

print('-- Create Database --')
try:
    create_database()
except Exception:
    print('Databae exists')

port = get_ports()[1]

print('-- Waitress --')
app = create_app()
print(f'Running server onn host {HOST} on port {port}...')
os.system('start http://127.0.0.1:8000')
serve(app, host=HOST, port=port)
print('Server stopped')
input()
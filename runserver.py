from config import get_waitress_port
import os

from waitress import serve


from database import create_database
from port_check import ports_check
from server import create_app

HOST = '127.0.0.1'

if not ports_check():
    input()
    exit()

print('-- Start PostgreSQL --')
os.system('start_db.bat')

print('-- Create Database --')
try:
    create_database()
except Exception:
    print('Databae exists')

waitress_port = get_waitress_port()

print('-- Waitress --')
app = create_app()
print(f'Running server onn host {HOST} on port {waitress_port}...')
os.system('start http://127.0.0.1:8000')
serve(app, host=HOST, port=waitress_port)
print('Server stopped')
input()

from config import get_postgresql_port, get_waitress_port
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

os.system('@SET PATH="%CD%\\PostgreSQL\\pgsql\\bin";%PATH%')
os.system('@SET PGDATA=%CD%\\PostgreSQL\\pgsql\\data')
os.system('@SET PGDATABASE=postgres')
os.system('@SET PGUSER=postgres')
os.system(f'@SET PGPORT={get_postgresql_port()}')
os.system('@SET PGLOCALEDIR=%CD%\\PostgreSQL\\pgsql\\share\\locale')

# "%CD%\PostgreSQL\pgsql\bin\initdb" -U postgres -A trust

os.system('"%CD%\\PostgreSQL\\pgsql\\bin\\pg_ctl" -D "%CD%\\PostgreSQL\\pgsql\\data" -l logfile start')

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

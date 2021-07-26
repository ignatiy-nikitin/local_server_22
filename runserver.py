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

line = f"""
@SET PATH="%CD%\\PostgreSQL\\pgsql\\bin";%PATH%
@SET PGDATA=%CD%\\PostgreSQL\\pgsql\\data
@SET PGDATABASE=postgres
@SET PGUSER=postgres
@SET PGPORT={get_postgresql_port()}
@SET PGLOCALEDIR=%CD%\\PostgreSQL\\pgsql\\share\\locale

"%CD%\\PostgreSQL\\pgsql\\bin\\pg_ctl" -D "%CD%\\PostgreSQL\\pgsql\\data" -l logfile start
"""

with open('start_db.bat', 'w') as file_:
    file_.write(line)

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
os.system(f'start http://127.0.0.1:{waitress_port}')
serve(app, host=HOST, port=waitress_port)
print('Server stopped')
input()

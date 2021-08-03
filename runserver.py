import os

from waitress import serve

from database import create_database
from port_check import is_port_busy
from server import create_app
from settings import HOST, POSTGRES_PORT, WAITRESS_PORT


def _fill_start_db_file():
    line = f"""
    @SET PATH="%CD%\\pgsql\\bin";%PATH%
    @SET PGDATA=%CD%\\pgsql\\data
    @SET PGDATABASE=postgres
    @SET PGUSER=postgres
    @SET PGPORT={POSTGRES_PORT}
    @SET PGLOCALEDIR=%CD%\\pgsql\\share\\locale

    "%CD%\\pgsql\\bin\\pg_ctl" -D "%CD%\\pgsql\\data" -l logfile start
    """
    with open('start_db.bat', 'w') as file_:
        file_.write(line)


print('Checking PostreSQL port...')
if is_port_busy(HOST, POSTGRES_PORT):
    print('PostreSQL port is busy. Go to config.ini, change it and restart program')
    exit()

print('Checking Waitress port...')
if is_port_busy(HOST, WAITRESS_PORT):
    print('Waitress port is busy. Go to config.ini, change it and restart program')
    exit()

print('Fill start_db.bat file...')
_fill_start_db_file()

print('Starting PostgreSQL...')
os.system('start_db.bat')

print('Creating database if necessary...')
try:
    create_database()
except Exception:
    print('Databae exists')

print('Starting Waitress...')
app = create_app()
print(f'Running server on host {HOST} on port {WAITRESS_PORT}...')
os.system(f'start http://{HOST}:{WAITRESS_PORT}')
serve(app, host=HOST, port=WAITRESS_PORT)

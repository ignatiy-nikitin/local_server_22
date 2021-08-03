@SET PATH="%CD%\pgsql\bin";%PATH%
@SET PGDATA=%CD%\PostgreSQL\pgsql\data
@SET PGDATABASE=postgres
@SET PGUSER=postgres
@SET PGLOCALEDIR="%CD%\pgsql\share\locale"
icacls "%CD%" /grant "%USERNAME%":(OI)(CI)F /T
"%CD%\pgsql\bin\initdb" -U postgres -A trust
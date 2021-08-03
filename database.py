import psycopg2

from settings import POSTGRES_PORT


def get_con():
    return psycopg2.connect(
        database="postgres",
        user="postgres",
        password="",
        host="127.0.0.1",
        port=POSTGRES_PORT,
    )


def create_database():
    con = get_con()
    cur = con.cursor()
    cur.execute('''CREATE TABLE items  
        (id SERIAL,
        value TEXT NOT NULL);''')
    con.commit()  
    con.close()


def insert_item(value):
    con = get_con()
    cur = con.cursor()
    cur.execute(f"INSERT INTO items (value) VALUES ('{value}')")
    con.commit()  
    con.close()


def get_items():
    con = get_con()
    cur = con.cursor()
    cur.execute("SELECT * FROM items;")
    values = cur.fetchall()
    con.close()
    return values 


if __name__ == '__main__':
    create_database()

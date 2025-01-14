import sqlite3


# dbname = 'new_db'
# user = 'den'
# password = 'den'
# host = 'localhost'
# port = '5432'


conn = sqlite3.connect('my_db.sqlite')

cursor = conn.cursor()

# cursor.execute("""CREATE TABLE users (
# id SERIAL,
# name varchar NOT NULL,
# description varchar NULL,
# CONSTRAINT users_pk PRIMARY KEY (id)
# );""")
cursor.execute(f"""INSERT INTO users ("name", "description") VALUES( 'Den110', 'descr22');""")
#
conn.commit()

cursor.execute(f"""Select * from users;""")

record = cursor.fetchall()
print("You are connected to - ", record)



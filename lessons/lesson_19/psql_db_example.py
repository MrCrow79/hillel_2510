import psycopg2


dbname = 'new_db'
user = 'den'
password = 'den'
host = 'localhost'
port = '5432'


try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    print("Connected to the database successfully!")

    cursor = connection.cursor()

    cursor.execute("SELECT version();")
    cursor.execute(f"""INSERT INTO public.users ("name", "description") VALUES( 'Den110', 'descr22');""")
    cursor.execute(f"""INSERT1 INTO public.users ("name", "description") VALUES( 'Den120', 'descr22');""")
    connection.commit()

    record = cursor.fetchall()
    print("You are connected to - ", record)

except (Exception, psycopg2.Error) as error:
    if connection:
        connection.rollback()
        print("Rollback activated", error)


finally:
    if connection:
        cursor.execute(f"""INSERT INTO public.users ("name", "description") VALUES( 'Den130', 'descr22');""")
        connection.commit()
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
import psycopg2


dbname = 'postgres'
user = 'anna'
password = 'anna'
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

    record = cursor.fetchall()
    print("You are connected to - ", record)

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")


def test_check_is_user_table_exist(cursor):

    cursor.execute("SELECT * from users")
    cursor.fetchall()


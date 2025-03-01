def test_employee_table_exists(cursor):
    cursor.execute("SELECT * FROM employees")
    cursor.fetchall()


def test_insert_to_employee_table(cursor, random_name, random_age, random_department):
    sql_insert_script = f"""
        INSERT INTO employees (name, age, department) 
        VALUES ('{random_name}', {random_age}, '{random_department}') 
        RETURNING id;
    """
    cursor.execute(sql_insert_script)
    new_row_id = cursor.fetchone()[0]

    sql_select = f"SELECT name, age, department FROM employees WHERE id = {new_row_id};"
    cursor.execute(sql_select)

    name, age, department = cursor.fetchone()
    assert name == random_name
    assert age == random_age
    assert department == random_department
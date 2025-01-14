import pytest
from faker import Faker

l_faker = Faker()


@pytest.fixture
def random_name():
    return l_faker.name()


@pytest.fixture
def random_text():
    return l_faker.text()[:20]


def test_insert_data_into_user_table(random_name, cursor, random_text):


    # insert data and get id of new row
    sql_insert = \
        f"""INSERT INTO public.users ("name", "description")  VALUES( '{random_name}', '{random_text}') RETURNING id;"""

    cursor.execute(sql_insert)
    # new_row_id = cursor.fetchall()  # list of rows  [(id_of_new_row, )]
    # new_row_id = cursor.fetchone()  # 1 row, tuple: (id_of_new_row, )
    new_row_id = cursor.fetchone()[0]  # 1 value: id_of_new_row

    sql_select = f"""Select name, description from users where id = {new_row_id}"""

    cursor.execute(sql_select)
    name, descr = cursor.fetchone()  # 1 row, tuple(name, descr)

    print(name)

    assert name == random_name
    assert descr == random_text



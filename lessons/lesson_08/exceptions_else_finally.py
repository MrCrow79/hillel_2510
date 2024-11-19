import time

user_ids = [1,2,3,None,4]

def get_data_from_db(user_id):

    connection = True  # creating connection to db
    print('Connection was opened')
    data = [user_id, 'some stuff']

    time.sleep(1)  #  чекати 5 секунд

    try:
    # бд щось робить і поверне помилку якщо user_id is None
        if user_id == None:
            raise AttributeError('Error from DB')

    except Exception as e:
        print('smth was wrong')
        raise e

    else:  #  буде відпрацьовувати якщо не впало помилки
        print('We get the data')
        return data

    finally:  #  цей блок виконуеться в кінці і завжди
        connection = False # закрили коннект до БД
        print('Connection was closed')
        print('-'*90)



for user in user_ids:
    user_data = get_data_from_db(user)
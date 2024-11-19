
def getting_data_from_db(user_id):

    try:
        1/user_id  # для виклику ZeroDvision
        user_id_in_db = str(user_id *5 + 17)  # як зберігаеться в бд
        # connect to db
        return {
            'user_id': user_id_in_db,
            'data': []
        }

    except TypeError:
        print('Type error. You have to use int')
        return {}

    # except ZeroDivisionError:
    #     print('ZeroDivisionError. user id must be > 0')
    #     return {}

    except Exception as e:
        print('something is wrong. COuld be connectio to db is broken')
        raise e  # raise - виклик помилки


def connect_by_ssh():
    raise AttributeError  #  викличемо помилку


counter = 5

while counter > 0:

    try:

        connect_by_ssh()
        counter = 0
    except Exception: # except:
        print(f'Cant connect, left {counter} attemp')
        counter = counter -1
#
# user_data = getting_data_from_db(18)
# print(user_data)
# print('-'*80)
# user_data = getting_data_from_db(0)
# user_data = getting_data_from_db('17')
# print(user_data)

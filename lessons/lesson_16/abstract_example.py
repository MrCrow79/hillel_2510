from abc import ABC, abstractmethod


class BaseDbConnector(ABC):

    def __init__(self, connection_string):  # підключення до БД буде ТІЛЬКИ через connection string
        self.connection_str = connection_string
        self._cursor = None

    @abstractmethod
    def open_connection(self):
        pass

    @abstractmethod
    def cursor(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass


class PostgresSql(BaseDbConnector):

    def __init__(self, connection_string='psql://..'):
        super().__init__(connection_string)


    def open_connection(self):
        print('Connection was created')

    def cursor(self):
        print('Cursor was created')
        self._cursor = True

    def close_connection(self):
        print('Connection was closed')

    def get_user_by_id(self, user_id):
        if self._cursor is None:  # це буде якщо нема курсора
            raise AttributeError('Cant connect to DB')
        print('User data is ....')


class SQLITE(BaseDbConnector):

    def __init__(self, connection_string='sqlite3://..'):
        super().__init__(connection_string)


    def get_user_by_id(self, user_id):
        if self._cursor is None:  # це буде якщо нема курсора
            raise AttributeError('Cant connect to DB')
        print('User data is ....')

    def close_connection(self):
        print('Connection was closed')

psql_db = PostgresSql()
psql_db.open_connection()
psql_db.cursor()
psql_db.get_user_by_id(5)
psql_db.close_connection()


sqlite_db = SQLITE()
sqlite_db.open_connection()
sqlite_db.cursor()
sqlite_db.get_user_by_id(5)
sqlite_db.close_connection()

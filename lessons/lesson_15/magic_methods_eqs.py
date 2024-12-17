# assertpy

response_from_api = {'name': 'Apple', 'empl': 3000, 'average_sal': 5000}
response_from_db = {'c_id': 20, 'c_name': 'Apple', 'c_empl': 3000, 'c_average_sal': 5000, 'created_date': '20-12-2000'}


# def compare_api_and_db_companies(api_c, db_c):
#
#     assert api_c['name'] == db_c['c_name'], 'company name'
#     assert api_c['empl'] == db_c['c_empl'], 'company empl'
#     assert api_c['average_sal'] == db_c['c_average_sal'], 'company average_sal'


class CompanyAPI:

    def __init__(self, name, empl, average_sal):
        self.name = name
        self.empl = empl
        self.average_sal = average_sal

    # відповідає за ==
    def __eq__(self, other):
        """
        != == not __eq__
        __gte__ >=
        __gt__ >
        __lte__ <=
        __lt__ <
        """

        # other_name = other.c_name if isinstance(other, CompanyDB) else other.name
        if isinstance(other, CompanyDB):
            other_name = other.c_name
        else:
            other_name = other.name

        other_empl = other.c_empl if isinstance(other, CompanyDB) else other.empl
        other_average_sal = other.c_average_sal if isinstance(other, CompanyDB) else other.average_sal

        if self.name != other_name:
            return False
        if  self.empl != other_empl:
            return False
        if self.average_sal != other_average_sal:
            return False

        return True


class CompanyDB:

    def __init__(self, c_id, c_name, c_empl, c_average_sal, created_date):
        self.c_id = c_id
        self.c_name = c_name
        self.c_empl = c_empl
        self.c_average_sal = c_average_sal
        self.created_date = created_date

user_api = CompanyAPI(**response_from_api)
user_db = CompanyDB(**response_from_db)


def compare_api_and_db_companies(api_c, db_c):
    print(api_c == db_c)  # ==> api_c.__eq__(db_c)
    print(api_c == api_c)  # ==> api_c.__eq__(db_c)

user_db.c_name = 'Asd'
compare_api_and_db_companies(user_api, user_db)

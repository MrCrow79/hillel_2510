
class IPhone15:

    brand = 'Iphone'
    model = 15
    last_os_versions = [17, 18.1, 18.2]  # attribute of class

    def __init__(self, number):
        self.base_number = number  # атрибут екземпляра
        self.os_version = 18.05  # атрибут екземпляра
        self.available_os_versions = [18.05, 18.09]  # атрибут екземпляра
        # self.last_os_versions = [20.0, 21.1]

    def call_and_send_sms(self, number, text):  # метод екземпляра
        self.make_a_call(number)
        self.send_sms(number, text)

    def make_a_call(self, number):
        print(f'Calling from {self.base_number} to {number}')

    def send_sms(self, number, text):
        print(f'Sending from {self.base_number} to {number}:\n{text}')

    @staticmethod
    def ping():
        print(f'Pong')





my_phone = IPhone15(number=123)
your_phone = IPhone15(number=456)

IPhone15.ping()
my_phone.ping()

# print(id(your_phone.available_os_versions))
# print(id(my_phone.available_os_versions))

print(id(your_phone.last_os_versions))
print(id(my_phone.last_os_versions))

your_phone.last_os_versions.append(19.0)

print(my_phone.last_os_versions)
print(id(my_phone.last_os_versions))

your_phone.last_os_versions = [20.0, 21.1]  # створення нової змінної last_os_versions ДЛЯ your_phone, self attribute
print(id(your_phone.last_os_versions))

print(id(your_phone.__class__.last_os_versions))
print(your_phone.last_os_versions)
print(your_phone.__class__.last_os_versions)
print(IPhone15.last_os_versions)


IPhone15.make_a_call(self=my_phone, number=789456123)


# print(id(your_phone.os_version))
# print(id(my_phone.os_version))

#
# print(my_phone.brand)
# print(my_phone.os_version)
#
# IPhone15.brand = 'Sams'
# print(my_phone.brand)
# my_phone.os_version = 17
# print(your_phone.os_version)
# print(my_phone.os_version)


# print(my_phone.brand)
# print(your_phone.model)
# print(my_phone.os_version)
# print(your_phone.os_version)

# print(IPhone15.os_version)
# IPhone15.os_version = 19.0

# print(my_phone.os_version)
# print(your_phone.os_version)

#
# print(id(my_phone.brand))
# print(id(your_phone.brand))
# print(id(IPhone15.brand))
#
# IPhone15.brand = 'Samsung'
#
# print(my_phone.brand)
# print(your_phone.brand)

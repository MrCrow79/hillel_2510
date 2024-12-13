
class Phone:

    def __init__(self, number):
        # print('Init calling')
        self.base_number = number  # атрибут екземпляра

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


my_phone = Phone(number=123) # instance, екземпляр
your_phone = Phone(number=456) # instance, екземпляр

print(my_phone.base_number)
print(your_phone.base_number)

Phone.make_a_call(self=my_phone, number=4567)  # my_phone.make_a_call(number=4567)
your_phone.make_a_call(number=4567)



#
# my_phone.ping()
# Phone.ping()
# Phone.send_sms(456, 'asd')

# print(id(my_phone))
# print(id(your_phone))

# my_phone.send_sms(123456, 'sms text asd')
# your_phone.send_sms(8888, ' asd sms text asd')


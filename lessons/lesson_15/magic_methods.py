class Student:

    def __init__(self, name, math_score=None, lit_score=None):
        self.name = name
        self.math_score = math_score
        self.lit_score = lit_score

    def print_info(self):
        print(f'my name is {self.name}')


    def __str__(self):
        return f'my name is {self.name}'


    def __repr__(self):
        return f'Student(name=\'{self.name}\', math_score={self.math_score}, lit_score={self.lit_score})'


alex = Student('Alex', 79, 89)
ivan = Student('ivan', 79, 89)
mor = Student('mor', 79, 89)

# [user.print_info() for user in [alex, ivan, mor]]
# [print(user) for user in [alex, ivan, mor]]

print(str(ivan)) # == print(ivan.__str__())
print(ivan.__str__())
print(repr(ivan))  # == print(ivan.__repr__())

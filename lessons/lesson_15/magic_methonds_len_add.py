class Courses:

    def __init__(self, name, duration = None):
        self.name = name
        self.students = []
        self.duration = duration if duration else 6  # 0.5 year by default
        self.current_duration = 0


    def skip_1_month(self):

        if self.current_duration + 1 <= self.duration:  # збільшую current_duration на 1 поки він не буде == duration
            self.current_duration += 1


    # def __add__(self, other):  # +, lit + math
    #     # [1,2,3].append([3,4]) => [1,2,3,[3,4]]
    #     # [1,2,3].extend([3,4]) => [1,2,3,3,4]
    #     self.students.extend(other.students)

    def __add__(self, other):  # new_course = lit + math
        new_c = Courses(name=self.name, duration=self.duration)
        new_c.students = self.students + other.students
        new_c.current_duration = self.current_duration
        return new_c



    def len_of_course(self):
        return self.duration - self.current_duration


    # def __len__(self):
    #     return self.duration - self.current_duration


    def __len__(self):
        return len(self.students) # == return self.students.__len__()

math = Courses('math')
lit = Courses('lit')



math.students.append('Alex')
math.students.append('Yuri')
math.students.append('Mor')
lit.students.append('Max')
print(len(lit))
print(lit.students)
new_course = lit + math
print(lit.students)
print(math.students)
print(new_course.students)


# print(math.len_of_course())
# print(len(math))  # ==> print(math.__len__())
# math.skip_1_month()
# math.skip_1_month()
# math.students.append('Alex')
# print(math.len_of_course())
# print(len(math))
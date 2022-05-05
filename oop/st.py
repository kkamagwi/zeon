class Students:
    SCHOOL = '6'
    __gpa = 0
    _mental_activity = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk_to_school():
        print('I go to school')

    def calculate_gpa(self, *marks):
        gpa = 0
        i = 0
        for mark in marks:
            gpa += mark
            i += 1
        self.__gpa = gpa / i



    def get_gpa(self):
        print(self.__gpa)


    @classmethod
    def change_school(cls, shkola):
        cls.SCHOOL = shkola


    @staticmethod
    def can_go_to_school(student):
        if student.age > 5:
            if student._mental_activity == False:
                Students.change_school('spesial school')
                return True
            return True
        else:
            return False


student1 = Students('John', 56)
student1._mental_activity = False
student1.calculate_gpa(5,3,4,2,5,5,5,5)
student1.get_gpa()
print(student1.SCHOOL)
Students.change_school('61')
print(student1.SCHOOL)
z = Students.can_go_to_school(student1)
print(student1.SCHOOL)
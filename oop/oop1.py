class User:
    def __init__(self,login,passw, group):
        self.login = login
        self.passw = passw
        self.group = group


    def admin(self):
        print(f'{self.login} состоит в группе {self.group}')



class Student(User):
    def __init__(self,login,passw,lesson,group,*args):
        super().__init__(login,passw, group)
        self.lesson = lesson
        self.args = args


    def average(self):
        a = 0
        for lesson in self.args:
            a += lesson
        res = a / len(self.args)
        print(f' Средний балл: {res} Ученика: {self.login}')

    def __str__(self):
        return f'{self.login} str {self.group}'


class Teacher(User):
    def __init__(self, login,passw, group):
        super().__init__(login, passw, group)
        print(self.login)

    def admin(self):
        print(f'{self.login} ведет в группах {self.group}')

    def __str__(self):
        return f'{self.login} str {self.group}'



us =Student('John',1234,7,'Python',5,5,3,5)
us2 = Student('Nick',1234,5,'Python',3,5,3,2)
us2.average()
us.average()
us.admin()
t =Teacher('Teacher12',1234, ['PTN1', "Eng2"])
t.admin()

list_of_objects = [us, us2, t]

def admin(list_of_objects):
    for i in list_of_objects:
        print('infa ', i)

admin(list_of_objects)
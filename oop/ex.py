class Group:
    def __init__(self, name):
        self.name = name

    def __call__(self, name_):
        self.name = name_
        return self.name

    def __str__(self):
        return self.name

a = Group("jakhsd")
a.name = 'PT'
b = Group("another")
b('ag')




class Journal:
    def __init__(self, *groups):
        self.groups= groups
        for group in groups:
            print(group)

    def __str__(self):
        return str(self.groups)

school1 = Journal(a, b)
print(school1)
class CharField:
    def __init__(self, chr, max_length):
        self.chr = chr
        self.max_length = max_length

        if len(self.chr) > self.max_length:
            raise Exception('Вы превысили количество знаков')

    def __str__(self):
        return self.chr

class IntegerField:
    def __init__(self,int_number):
        if type(int_number) != int:
            raise TypeError("Не тот тип данных, введите в следующий раз интеджер")
        self.int_number = int_number

class TextField:
    def __init__(self, text):
        self.text = str(text)

    def __str__(self):
        return self.text

class Author:
    def __init__(self,name):
        self.name = CharField(name, 63)

    def get_posts(self):
        for post in self.posts:
            print(post)

    def write_a_work(self,text_of_post,name_of_post,ID_of_post):
        self.posts.append(Post(description=text_of_post,title= name_of_post, ID= ID_of_post))


class Post:
    def __init__(self,ID, title, description,):
        self.title = CharField(title, 50)
        self.ID = IntegerField(ID)
        self.text = TextField(text=description)

    def __str__(self):
        return str(self.title)

p1 = Post(1, 'My first post', 
'''Hello! My name is balahblah and this is my firs post''')
p2 = Post(2, 'My second post', 
'''Hello! My name is balahblah and this is my firs postfkdsjfkj
fndskjfhlksjf
dfljkasflk''')
author1 = Author('Katya', [p1, p2])
author1.write_a_work(ID_of_post=3, name_of_post='My third post', 
text_of_post='''Hello! My name is balahblah and this is my firs postfkdsjfkj
fndskjfhlksjf
dfljkasflk''')
# print(p1)
print(author1.get_posts())
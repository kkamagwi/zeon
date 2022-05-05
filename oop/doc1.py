from word2number import w2n
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

def wordToNumbers(calculate):
    def wrapper(*args):
        # self, a, b, c
        args1 = []
        for i in range(1, 4):
            if isinstance(args[i], str):
                args1.append(w2n.word_to_num(lemmatizer.lemmatize(args[i])))
            elif isinstance(args[i], (int, float)):
                args1.append(args[i])

        calculate('kdjsf', args1[0], args1[1], args1[2])
    return wrapper


class QuadraticEquation:
    # @wordToNumbers
    def calculate(self, a, b, c):
        D = b ** 2 - 4 * a * c
        if D < 0:
            print ("Дискриминант = 0")
            print ("Корней нет")
        elif D == 0:
            x = (-b + D ** .5) / (2 * a)
            print ("Дискриминант = ", D)
            print ("Корень один: ", x)
        else:
            x1 =  (-b + D ** .5) / (2 * a)
            x2 =  (-b - D ** .5) / (2 * a)
            print ("Дискриминант = ", D)
            print ("Есть 2 корня: ")
            print ("Корень 1 =  ", x1)
            print ("Корень 2 =  ", x2)
a = QuadraticEquation()
print(a)
a.calculate(12, 'two' ,3)

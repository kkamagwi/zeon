class Marshrutka:
    plases = 15
    def __init__(self, name):
        self.name = name

class Passanger():
    fee = 10
    def __init__(self, id, name):
        self.id = id
        self.name = name


class MarshrutkaClack:
    def calculate(self, pasengers, marshrutka):
        print('Calculating Payroll')
        print('===================')
        fee = 0
        plases = marshrutka.plases - len(pasengers)
        for pasenger in pasengers:
            print(f'Payroll for: {pasenger.id} - {pasenger.name}')
            print(f'- Check amount: {pasenger.fee}')
            fee += pasenger.fee
            

        print(f'fee is {x} with {plases} plases in bus {marshrutka.name}')

p1 = Passanger(1, 'Vasya')
p2 = Passanger(2, 'Argen')
bus_101 = Marshrutka('101')

calc = MarshrutkaClack()
calc.calculate([p1, p2, p1], bus_101)

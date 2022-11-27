
#args, arguments would be a tuple - unlimited positional arguments, the position matters
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum

temp_total = add(1,2,3,4,5)
print(temp_total)

#kwargs, many keyword arguments, makes a dictionary in the background
def calculate(n,**kwargs):
    # print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    #     print(kwargs['add'])
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)
calculate(2,add=3, multiply=5)


class Car:

    def __init__(self, **kw):
        '''keys are make, model, color, seats'''
        self.make = kw.get('make')
       # self.model = kw['model'] #will fail if key does not exist
        self.model = kw.get('model') #returns none if key does not exist
        self.color = kw.get('color')
        self.seats = kw.get('seats')

my_car = Car(make='Nissan', model='GTR')
my_car2 = Car()
print(my_car.model)
print(my_car.make)
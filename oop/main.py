import time

def uppercase(func):
    import time
    def wrapper():
        s = time.time()
        upper = func()
        case = upper.upper()
        e = time.time()
        print('Time ',e-s)
        return case
    return wrapper

def split_string(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper

@split_string
@uppercase
def hi():
    # a = 15
    # b = 13
    # c  = a**b + a*b
    # return c
    return "hi, i create my first decorator"

print(hi())

def my_fav_mela(func):
    def print_meal(meal1, meal2):
        func(meal1, meal2)
        print("Мне нравится есть {0}, а так же я иногда ем {1}".format(meal1, meal2))
    return print_meal

@my_fav_mela
def my_pizza(pizza, lasagna):
    return pizza, lasagna

my_pizza("Пицу", "Лазанью")
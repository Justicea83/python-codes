def func():
    return 1


def hey(name='Jose'):
    print('The hello() has been executed')

    def greet():
        return '\t This is the greet() func inside hello'

    def welcome():
        return '\t This is the welcome() inside hello'

    print('I am going to return a function')

    if name == 'Jose':
        return greet
    else:
        return welcome


def hello():
    return 'Hi Jose'


def other(some_def_func):
    print('Ptjer Cpde rims jere')
    print((some_def_func()))

#@decorator

print(other(hello))

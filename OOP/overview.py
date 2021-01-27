import inspect
from queue import Queue
def make_class(x):
    class Dog:
        def __init__(self,name):
            self.name = name
        def print_value(self):
            print(x)
    return Dog

cls = make_class(10)
print(cls)
d = cls("Tim")
print(d.name)
d.print_value()
# print(inspect.getmembers(cls))
# print(inspect.getsource(make_class))
# print(inspect.getsource(Queue))

# The Python Data Model
class Person:
    def __init__(self,name):
        self.name = name
    # def __repr__(self):
    #     return f"Person({self.name})"

p = Person("tim")
print(p)

## Metaclass
class Meta(type):
    def __new__(self, class_name, bases,attrs):
        print(attrs)
        return type(class_name, bases, attrs)

class Dog(metaclass=Meta): 
    x = 5

# Decorators
def func(f):
    def wrapper(*args, **kwargs):
        print("started")
        f(*args, **kwargs)
        print("end")
    return wrapper

@func
def func1():
    print("I am func1")

func1()


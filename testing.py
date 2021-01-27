test_dic = {'a':1, 'b':2, 'c':3, 'd':4}

print(test_dic)
print(test_dic.keys())
print(test_dic.values())
print(test_dic.items())

temp = iter(test_dic)

# print(type(temp))
# print(next(temp))
# print(next(temp))
# print(next(temp))
# print(next(temp))

# g=(n for n in range(1,11))
# #Returns an generator object which is an iterator [contains element from 1 to 10]
# print (g) #Output: <generator object <genexpr> at 0x0116C728>
# #We can iterate through the iterator object using for loop or using next() function.

# print (next(g))#Output:1
# print (next(g))#Output:2
# print (next(g))#Output:3

# #for loop will iterate through the remaining elements (starting from fourth element)
# for i in g:
#     print (i, end="\n") #Output: 4 5 6 7 8 9 10 

print("{0:1} love {1:1}".format('I', 'You'))

class Person:
    __is_private = 'secret'
    is_public = 'neaaa'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __nonpublic_method(self):
        print('private')
    def public(self):
        print('public')

emon = Person('emon', 22)
## no!! nothing is private because __is_private textually replaced by _Person__is_private
print(emon._Person__is_private)


def power_factory(exp):
    def power(base):
        return base ** exp
    return power

square = power_factory(2)
print(square)
print(square(4))
## [Everything in Python is an object](https://www.codingninjas.com/blog/2020/08/27/how-everything-in-python-is-an-object/)

Different programming languages define “object” in different ways. In some, it means that all objects must-have attributes and methods while in others, it simply means that all objects are subclassable. In Python programming language its definition is looser as some objects have neither attributes nor methods and also not all objects are subclassable.

But the statement that “Everything in Python is an object” means in the sense that it can be assigned to a variable or passed as an argument to a function. So the objects are the building blocks of an object-oriented program, as the program that uses object-oriented technology is basically a collection of objects. Hence programmes written in python is also a collection of these objects in the form of variables. So it is important to revise that everything in Python objects it means that the strings are objects, Lists are objects, Functions are objects and Even modules are also objects.

```py
x= 4.0
x.is_integer()
type(x.is_integer)
```

Contrary to a language such as Ruby where everything is also an object, Python does not allow to add new attributes or methods to the built-in types such as int or str. So an object is an abstraction that allows us to program without having to manually keep track of every little thing.

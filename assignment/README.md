## Executing an assignment statement

- Evaluate the expression on the right-hand side, yielding the id of an object.
- If the variable on the left-hand-side doesn’t already exist, create it.
- Store the id from the expression on the right-hand-side in the variable on the left-hand side.

## Evaluating an expression

- If the expression is a variable, find the variable. If it doesn’t exist, this is an error. If it does exist, the value of the expression is the id stored in that variable.
- If the expression is a “literal value”, such as 176.4 or 'hello', create an object of the appropriate type to hold it. The value of the expression is the id of that object.
- If the expression is an operator, such as + or %, evaluate its two operands, apply the operator to them, and create a new object of the appropriate type to hold the result. The value of the expression is the id of that object.

## Mutability and aliasing

Some data types in Python (e.g., integers, strings, and booleans) are immutable, meaning that the value stored in an object of that type cannot change. If we reassigned the variable then it create new `id`.

More complex data structures in Python are mutable, including lists, dictionaries, and user-defined classes.

When two variables refer to the same object, we say that the variables are aliases of each other.

> Changing a reference is not the same as mutating a value

In general, a statement of the form `my_var = _____` never mutates the object that my_var refers to.

## Two types of equality

We can use the `==` operator to compare the values stored in the objects they reference. This is called **value equality**.

We can use the `is` operator to compare the ids of the objects they reference. With is, we are asking whether two variables reference the exact same object. This is called **identity equality**.

## A special case with immutable objects

Because ints are immutable, there isn’t much point in Python creating a separate int object every time your variable needs to refer to, say, 0. They can all refer to the very same object and no harm can be done since the object can never change. This explains the following code:

```py
x = 43
y = 43
x == y # True
x is y # True
x = 'foo'
y = 'foo'
x is y # True
x = 'Emon Hossain'
y = 'Emon Hossain'
x is y # True
```

The bottom line is this: know whether your objects are mutable—at each level of their structure. Memory model diagrams offer a concise visual way to represent that.

## Type Annotation

Python takes a very different approach: only objects have a type, not the variables that refer to those objects; and in fact, a variable can refer to any type of object.

> Just remember to import the `typing` module

- Primitive type: `int`, `float`, `str`, `bool`, `None`
- Compound type: `List[T]`, `Dict[T1,T2]`, `Tuple[T1,...]`
- Advanced type: `Any`, `Union`, `Optional`, `Callable`

> The type expression `Optional[T]` is equivalent to `Union[T, None]` for all type expressions T. The type `Callable[[int, str], bool]` is a type expression for a function that takes two arguments, an `integer` and a `string`, and returns a `boolean`.

## Choosing Test Cases

### doctest

```py
class Stack():
    """
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> stack.size()
    2
    >>> stack.pop()
    2
    >>> stack.peek()
    1
    >>> stack.pop()
    1
    >>> stack.isEmpty()
    True
    """
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return not bool(self.items)
    def size(self):
        return len(self.items)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# python testing.py -v
```

## Create Envirnment

```
conda env list
conda create --name uot-env python=3.8.5
conda activate uot-env
conda deactivate
conda env remove --name uot-env
```

## Representation Invariant

A **representation invariant** is a property of the instance attributes that every instance of a class must satisfy.

## Inheritance

- base class, superclass, and parent class are synonyms.
- derived class, subclass, and child class are synonyms.

## Stack

- Data: a collection of items
- Operations: determine whether the stack is empty, add an item (push), remove the most recently-added item (pop)

## Queue

- Data: a collection of items
- Operations: determine whether the queue is empty, add an item (enqueue), remove the least recently-added item (dequeue)

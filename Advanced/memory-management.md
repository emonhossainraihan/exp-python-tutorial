## What is Memory Management?

Memory management is the process of efficiently allocating, de-allocating, and coordinating memory so that all the different processes run smoothly and can optimally access different system resources. Memory management also involves cleaning memory of objects that are no longer being accessed.

In Python, the memory manager is responsible for these kinds of tasks by periodically running to clean up, allocate, and manage the memory. Unlike C, Java, and other programming languages, Python manages objects by using reference counting. This means that the memory manager keeps track of the number of references to each object in the program. When an object’s reference count drops to zero, which means the object is no longer being used, the garbage collector (part of the memory manager) automatically frees the memory from that particular object.

The user need not to worry about memory management as the process of allocation and de-allocation of memory is fully automatic. The reclaimed memory can be used by other objects.

Ineffective memory management leads to slowness on application and server-side components.

Even though most of Python’s memory management is done by the Python Memory Manager, an understanding of best coding practices and how Python’s Memory Manager works can lead to more efficient and maintainable code.

There are two types of memory:

- Stack (Static Memory)
- Heap (Dynamic Memory)

[How does Python work?](https://towardsdatascience.com/how-does-python-work-6f21fd197888)

There is a common step in any implementation, though: your code is first compiled (translated) to intermediate code - something between your code and machine (binary) code - called bytecode (stored into .pyc files). Note that this is a one-time step that will not be repeated unless you modify your code.

And that bytecode is executed every time you are running the program. How? Well, when we run the program, this bytecode (inside a .pyc file) is passed as input to a Virtual Machine (VM)1 - the runtime engine allowing our programs to be executed - that executes it.

Depending on the language implementation, the VM will either interpret the bytecode (in the case of CPython2 implementation) or JIT-compile3 it (in the case of PyPy4 implementation). PyPy often runs faster than CPython because PyPy is a just-in-time compiler while CPython is an interpreter.

[Python ships with an interpreter that can be used as a REPL (read-eval-print-loop), interactively, on the command line. Alternatively, you can invoke Python with scripts of Python code. In both cases, the interpreter parses your input and then compiles it into bytecode (lower-level machine instructions) which is then executed by a "Pythonic representation" of the computer. This Pythonic representation is called the Python virtual machine.](https://stackabuse.com/differences-between-pyc-pyd-and-pyo-python-files/)

> CPython is the default byte-code interpreter of Python, which is written in C.

You need to keep Python-the-language separate from whatever runs the Python code.

## What about Jython, etc.?

Jython, IronPython and PyPy are the current "other" implementations of the Python programming language; these are implemented in Java, C# and RPython (a subset of Python), respectively. Jython compiles your Python code to Java bytecode, so your Python code can run on the JVM. IronPython lets you run Python on the Microsoft CLR. And PyPy, being implemented in (a subset of) Python, lets you run Python code faster than CPython, which rightly should blow your mind. :-)

## Actually compiling to C

So CPython does not translate your Python code to C by itself. Instead, it runs an interpreter loop. There is a project that does translate Python-ish code to C, and that is called Cython. Cython adds a few extensions to the Python language, and lets you compile your code to C extensions, code that plugs into the CPython interpreter.

# Part VI

We'll walk here quickly on some additional Python constructs that weren't introduced before.

## 'args' and 'kwargs'

A function may have positional parameters and named parameters. The named parameters have each a default, and hence can be omitted in a call.
It is important to provide all the positional arguments first (to the left most), and then one can give any named argument that should get a different value from the default declared in the function definition to the matching parameter.

``` py
def my_func(p1, p2, named1=4, named2=7):
    print(p1 + p2 + named1 + named2)


my_func()
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[40], line 1
----> 1 my_func()

TypeError: my_func() missing 2 required positional arguments: 'p1' and 'p2'
```

``` py
my_func(1, 2, 3)
```

``` 13 ```

``` py
my_func(1, 2, named2=3)
```

``` 10 ```

A function may have a variable number of parameters. One way to achieve this is by actually having a list as a parameter, and documenting to the user of the function that he/she are expected to pass a list of values.

``` py
def count_characters(header, list_of_texts):
    """This function returns the total number of characters in the texts you pass in 'list_of_texts'.
    Note, you're expected to pass a list where the items are the individual texts
    'header' is used in the output"""
    
    return f'{header}: {sum(len(x) for x in list_of_texts)}'


count_characters("Summary count", ["Hi", "Bye"])
```

``` 'Summary count: 5' ```

There is a nicer Pythonic way to acchieve above.

``` py
def count_characters2(header, *list_of_texts):
    """This function returns the total number of characters in the texts you pass.
    'header' is used in the output"""
    
    return f'{header}: {sum(len(x) for x in list_of_texts)}'


count_characters2("Summary count", "Hi", "Bye")
```

``` 'Summary count: 5' ```

Starting from the asterisk '\*', the non-named arguments are collected into *list_of_texts* as a list. Note that the functions are similar and the only difference is the function declaration. The call to the function is then somewhat simpler. We've seen a similar call with 'print' for example.

If we want to pass a variable number of named arguments, potentially some that our function shall only forward to another function, we can pass them in a dict. Again, Python provides a nice way to achieve that. This time we'll be using '\*\*'.

``` py
def count_characters3(*list_of_texts, **kwargs):
    """This function returns the total number of characters in the texts you pass.
    'header' is used in the output"""
    
    header = kwargs.get("header", "Count")
    
    return f'{header}: {sum(len(x) for x in list_of_texts)}'


count_characters3("Hi", "Bye", header="Summary count is still")
```

``` 'Summary count is still: 5' ```

The names **args** and **kwargs** are commonly used for those parameters ('args' and 'keyword args'). Sometimes we'll use a specific name, as was in the example for *list_of_texts*. 

## Closure

A **closure** is an object that is not a result of a class initialization, but rather a scope of execution that is being "kept" for later.
For example.

``` py
def standardize(mean, std):
    """
    This function returns a function that accepts a number
    and returns the standardized equivalent.
    """
    
    def do_standardize(number):
        return (number - mean) / std
    
    return do_standardize


for std_fn in [standardize(1, 0.5), standardize(0, 1)]:
    print(tuple(std_fn(arg) for arg in [1, 2, -1]))
```

```
(0.0, 2.0, -4.0)
(1.0, 2.0, -1.0)
```

In above example the object that we refer to as the closure is a function that has the context of *mean* and of *std*. This function object when called with a single argument, *arg* -> *number* in the example, returns the standardized equivalent, taking into account *mean* and *std*. Above this was demonstrated with two such standardization function objects that, and for each of those we checked the returned value for *1*, *2*, and *-1*.

Why is it nice to have this support in the language? It may be nice not to have to pass repetitive parameters on every call. In the example, we pass once *mean* and *std* and then forget about them. If we have two different standardization settings, then we have two relevant function objects, and again in the reset of the function we just use the right standardization object.

There is a very useful util function, *patrial* in *functools* that would have help us achieve a similar "keep for later", if the *mean* and *std* where given as keyword args:

``` py
from functools import partial


def standardize(number, mean=0, std=1):
    return (number - mean) / std


for std_fn in [
    partial(standardize, mean=1, std=0.5),
    partial(standardize, mean=0, std=1)
]:
    print(tuple(std_fn(arg) for arg in [1, 2, -1]))
```

```
(0.0, 2.0, -4.0)
(1.0, 2.0, -1.0)
```

Here is another example for a potential usage of a closure. We want to count how many times we call specific functions in our program. We are aware of profiling "debugging" tools, yet we want to have it simply in our code. Something like the following:

``` py
def f1(a, b):
    return a + b


def f2(a, b, c):
    return a + b * c


def count_activation_f1():
    "Helper to count activations of f1"
    
    def wrapped_f1(a, b):
        wrapped_f1.count += 1
        return f1(a, b)

    wrapped_f1.count = 0
    return wrapped_f1


wrapped_f1 = count_activation_f1()


def count_activation_f2():
    "Helper to count activations of f2"
    
    def wrapped_f2(a, b, c):
        wrapped_f2.count += 1
        return f2(a, b, c)
    
    wrapped_f2.count = 0
    return wrapped_f2


wrapped_f2 = count_activation_f2()

for i in range(4):
    wrapped_f1(i, 3 * i + 1)

for i in range(42):
    wrapped_f2(i, 3 * i + 1, 5)

wrapped_f1.count, wrapped_f2.count
```

```
(4, 42)
```

## Function Decorators

In Python there is a nice way to achieve above. It is called **function decorator**. The code above can be written as follows.

``` py linenums="1"
def counted(f):
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped


@counted
def f1(a, b):
    return a + b


@counted
def f2(a, b, c):
    return a + b * c


for i in range(4):
    wrapped_f1(i, 3 * i + 1)
    
for i in range(42):
    wrapped_f2(i, 3 * i + 1, 5)    


f1.calls, f2.calls
```

``` (4, 42) ```

Note that *counted* can be used as a utility function decorator in additional places, and that we're making use of '*args' and '**kwargs' that were mentioned above. We add here that in order to pass those further to a function that expects the individual parameters, we also use '\*' and '\*\*' in the call (line 4).

There is a small observation that we need to pay attention to.

``` py
@counted
def f3(x, y, a):
    """This functions returns the 'mixture' of 'x' and 'y',
    'a' parts 'x' and (1 - a) 'y'"""  
    
    assert 0 <= a <= 1 # yes we can do that in Python
    return x * a + y * (1 - a)


print(f3.__doc__)
```

``` None ```

What just happened? Where is our docstring?

'f3' is not anymore what we think it is. 'f3' is "wrapped".  
To "fix" that we can do, for example, as follows (see line 5 below).

``` py linenums="1"
import functools


def counted(f):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
        wrapped.calls += 1
        return f(*args, **kwargs)
    wrapped.calls = 0
    return wrapped


@counted
def f3(x, y, a):
    """This functions returns the 'mixture' of 'x' and 'y',
    'a' parts 'x' and (1 - a) 'y'"""  
    
    assert 0 <= a <= 1 # yes we can do that in Python
    return x * a + y * (1 - a)


print(f3.__doc__)
```

``` This functions returns the 'mixture' of 'x' and 'y', 'a' parts 'x' and (1 - a) 'y' ```

## Context Managers

When we open a file for reading or for manipulation, we probably want to close the file when done with it. There are multiple reasons why to 'close' at the end. Maybe by keeping the file open, another program cannot access the file as we are "holding" it. Then, potentially some of our activity is still only cached and if we want it be reflected in the file, we have to 'flush' or to 'close' the file.
At any case an open file is associated with an OS resource or a handle, and it is a good idea to close it once we've done with using / modifying the file.

``` py
fh = open("my_file.txt", "w")
fh.write("E.T. phone home")
fh.close()
```

```
!cat my_file.txt
```

``` E.T. phone home ```

Above ('!cat ..') was done in a jupyter notebook and is a shell command-line execution.

A better way to achieve above would be:

``` py
with open("my_file.txt", "a") as fh:
    fh.write("\nHere's my mobile")
```

We "entered" the context manager of the file. When we "exited" (as of the indentation), the file was closed automatically.
Note the usage of the **with** statement.

If you have multiple files, for example you implement a filter that reads from one file and writes to another file, you can either indent even more, or also use commas in a single 'with' expression, as follows:

``` py
with open("my_file.txt", "r") as fh, open("my_out_file.txt", "w") as fh_w:
    for line in fh:
        fh_w.write(line)
```

Context managers can may be available on additional "resource" kind objects.
For example database connections.
You can also create additional classes that support the context manager protocol and can be used in a 'with' statement.

## global, nonlocal

Most of our variables should be local. What does it mean to be 'local'? Variables that are assigned in a function exist from the time they are defined till the end of the function's execution (when the function returns).

``` py
def main():
    a = 3
    print(a)


if __name__ == "__main__":
    main()
    print(a)
```

```
3
Traceback (most recent call last):
  File "try2.py", line 8, in <module>
    print(a)
NameError: name 'a' is not defined
```

If one defines a variable outside of the function then it will be available in the current namespace. It will become "global". This is not as terrible in Python as in other languages, as different namespaces do not share the globals among them. If one wants to access a global variable of another module, this needs to be done implicitly by prepending the name of the model and a dot, as, for example, in ``` my_model.tree_root ```.

Also in the example below, we see that the function does not assume its variable is the one in the outer context, but rather works with its own local variable.

``` py
a = 3


def f_a():
    a = 5
    print(a)


f_a()
print(a)
```

```
5
3
```

It is good that the function *f_a* did not have a side effect of changing our "global" *a*.

But what if we actually did mean to have it the same variable *a*? We need to make it implicit.

``` py
a = 3


def f_a():
    global a
    a = 5
    print(a)


f_a()
print(a)
```

```
5
5
```

Let's see another example, in which we should actually use **nonlocal** rather than **global**.

``` py linenums="1"
a = 3

def f_a2():
  a = 0
  def f_a3():
      a = a + 1
  f_a3()
  print(a)

f_a2()
print(a)
```

```
---------------------------------------------------------------------------
UnboundLocalError                         Traceback (most recent call last)
Cell In[31], line 10
      7   f_a3()
      8   print(a)
---> 10 f_a2()
     11 print(a)

Cell In[31], line 7, in f_a2()
      5 def f_a3():
      6     a = a + 1
----> 7 f_a3()
      8 print(a)

Cell In[31], line 6, in f_a2.<locals>.f_a3()
      5 def f_a3():
----> 6     a = a + 1

UnboundLocalError: local variable 'a' referenced before assignment
```

A possible solution is to implicitly declare *a* to be 'nonlocal':

``` py
a = 3

def f_a2():
  a = 0
  def f_a3():
      nonlocal a
      a = a + 1
  f_a3()
  print(a)

f_a2()
print(a)
```

```
1
3
```

By saying 'nonlocal' one just instructs the runtime to look up in the stack for the variable that should already be available in an upper frame.

## Type Hints

Python is a dynamic language. Duck typing replaces type declarations and hard static enforcements.

On the other hand, to build a more reliable software, and to help ourselves and future users, we may want here and there to implicitly "hint" the expected type or expected protocol of an argument and / or the type of the returned value.

``` py
from typing import List


def my_function(count: int) -> List[str]:
    return ['Python'] * count
```

The "hints" add to the documentation. An IDE can use them to highlight potential issues.
Tools such as *mypy* can verify that we pass the correct arguments.

My suggestion is to add slowly more and more type hints wherever relevant.
Does not need to happen all the once in all places in your code.

Whatever the members of your team decide..

## JSON / XML / YAML

JavaScript Object Notation (JSON) is a very convinient textual hierarchical format to exchange data.
Another useful and similar format Extensible Markup Language (XML).
Both those format have great support in Python.
A third format that is used often with Python is YAML.

Those formats are useful for exchanging "documents" and for defining configurations.
A Python code can quickly read a (small) JSON file into a dict. From there access to the different elements can be achieved with normal dict accessors.

``` py
import json


d = dict(a = 3, b = {'c': "hello"})

d_as_json = json.dumps(d)

assert type(d_as_json) == str

del d

d = json.loads(d_as_json)

d['b']['c']
```

``` 'hello' ```

We can "serialize" a dict for example into a serie of characters that can be saved in a file, or be presented to a human being. It can be very useful in inter-process communication, as the content in HTTP requests, as a message, etc.

All above formats can be, almost with no effort, converted from one format to the other. With Python this would be just by loading from the source format into a dict, and saving to the target format.

``` py
import yaml


print(yaml.dump(d))
```

```
a: 3
b:
  c: hello
```

Interesting to know that objects in Python have an accessor attribute *\_\_dict\_\_* that can be a good starting point for serialization.

``` py
class A:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
    def can_drive(self) -> bool:
        return self.age >= 18


my_a = A("Jaakov", 16)

my_a.__dict__
```

```
{'name': 'Jaakov', 'age': 16}
```

## Dataclass

When we want to collect some pieces of information into a single variable, for example the *x* and the *y* coordinates of a point, we can use any of the built-in collections such as dict, tuple, list. To add more structure and to add specific functionality we can create a new class, say *Point*. We then need to decide if we want to allow / enforce settings the coordinates in the constructor, and whether those can be modified etc. A useful standard library provided utility decorator is **dataclass**. A lot of times, a dataclass is exactly what we need.
Here is an example:

``` py
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    

p1 = Point(1, 2)
p2 = Point(1, 4)
p1, p2
```

```
(Point(x=1, y=2), Point(x=1, y=4))
```

Check this short (22:18) YouTube recording. [This Is Why Python Data Classes Are Awesome (ArjanCodes)](https://www.youtube.com/watch?v=CvQ7e6yUtnw)
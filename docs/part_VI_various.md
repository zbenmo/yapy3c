# Part VI

We'll walk here quickly on some additional Python constructs that weren't introduced before.

A function may have positional parameters and named parameters. The named parameters have a default each, and hence can be ommited in a call.
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

Starting from the asteric __\*__, the arguments are collected into *list_of_texts* as a list. Note that the functions are similar and the only difference is the function declaration. The call to the function is then somewhat simpler. We've seen a similar call in 'print' for example.

If we want to pass a variable number of named arguments, potentially some that our function shall only forward to another function, we can pass them in a dict. Again, Python provides a nice way to achive that. This time we'll be using __\*\*__.

``` py
def count_characters3(*list_of_texts, **kwargs):
    """This function returns the total number of characters in the texts you pass.
    'header' is used in the output"""
    
    header = kwargs.get("header", "Count")
    
    return f'{header}: {sum(len(x) for x in list_of_texts)}'


count_characters3("Hi", "Bye", header="Summary count is still")
```

``` 'Summary count is still: 5' ```

The names **args** and **kwargs** are commonly used for those parameters, unless they have a better name, as the example for *list_of_texts*. *kw* stands for 'keyword'. 

A **closure** is an object that is not a result of of class initiation rather than a scope of execution is being "kept" for later.
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

Here is another example. We want to count how many times we call specific functions in our program. We are aware of profiling "debugging" tools, yet we want to have it simply in our code. Something like the following:

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

In Python there is a nice way to achieve above. It is called **decorator**. The code above can be written as follows.

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

Note that *counted* can be used as a utility function decorator in additional places, and that we're making use of '*args' and '**kwargs' that were mentioned above. We add here that inorder to pass those further to a function that expects the individual parameters, we also use __\*__ and __\*\*__ in the call (line 4). 
In Part I we learn the basics, data types, and the structure of a program.

Let’s get an access to a Python environment.
The following should work for you:

https://www.python.org/shell/

There are a few versions of Python, we’ll use Python 3. Let’s make sure this is what we have. run there (in your shell):

````{verbatim}
import sys
print(sys.version)
````

For me it printed: *3.8.0*, which is good.

You see above, that we had to **import** 'sys'. Otherwise *sys* wasn’t available. Once we imported it, *sys.version* was the version of the current Python interpreter (the running environment above). The **print** statement just shows us what we’ve imported. We did not need to import anything special to have ‘print’.

Let’s try just

````{verbatim}
sys.version
````

It also prints the value (*3.8.0* for me). This is as we’re in an interactive shell, but generally, unless we print something, an expression, as *sys.version*, or *3 + 4*, is just yet another expression, and does not show in the output.
We can omit the 'print' here, as in this exercise, we’ll be in the interactive shell.
Let’s try:

````{verbatim}
3 + 4
````

We get a new value. To see the **type** of a value, we use for example:

````{verbatim}
type(3)
````

We get:

```<class 'int'>```  (an integer)

What about *‘hello’*, what is its type?

We get:

```<class 'str'>``` (a string)

If you happen to use *“hello”* it should be the same, both should work.

````{verbatim}
my_list = [1, 2, 4]
type(my_list)
````

We should get:

```<class 'list'>```

Note above, that we assigned the value into a **variable**, *my_list*. This is handy as to use later in a program.

A list can be also constructed as follows:

````
list('hello')
````

```['h', 'e', 'l', 'l', 'o']```

The characters in the string became each an element in the list.

With lists you can take **slices**, we’ll use the variable *my_list* from above to demonstrate:

````
my_list[1:]
````

```[2, 4]```

````
my_list[:2]
````

```[1, 2]```

Clarification: a single element, for example the first, will be *my_list[0]*, a slice can be for example *my_list[1:4]*, or as above (*1:*, means from the second to the end, and *:2* means up to but not including index 2, therefore the first two elements).

Note: the first index is 0. So the valid indices for a list ‘lst’ are: 0..len(lst) - 1 (ex. when *len(lst) == 3* then the valid indices are 0, 1, 2).

Slices are also lists, try to get the type of a slice.

A list can be of mixed types, and also nested:

````
[1, 'Dog', my_list]
````

```[1, 'Dog', [1, 2, 4]]```

But usually, we’ll use lists where the elements are of the same type.

Let’s have a **function**:

````
def add(a, b):
    return a + b

add(1, 4)
````

```5```

````
add('abc', 'def')
````

```'abcdef'```

````
add(1, 'def')
````

```
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
 File "<stdin>", line 2, in add
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

So we’ve seen that the same function, *add*, was good for integers and for strings. For strings ‘+’ means concatenation. When we tried mixed arguments. The call started as expected, but then ‘+’ is not defined between an integer and ‘str’. And so we got an error, or as it is called in Python an **exception**. If we wrote it in a software product, this would either be considered a bug, or it can be handled in run time, with some more control flow constructs (later).

We can solve it by converting the integer first to a string:

````
str(1) + 'def'
````

```'1def'```

If we look for a second at the definition of the function above, we see that we’ve started with the word ‘def’, then gave the name of the new function, then a **parameters** list in parentheses, then the column, and inside the function commands were indented with a tab or a few spaces. The last statement in a function is often **return** with the calculated value as the output of the function.

````
type(add)
````

```<class 'function'>```

And we can also assign a function to a variable (note: not adding the parentheses	as in a call). The variable can later be activated (called).

````
a_func = add
a_func(9, 8)
````

```17```

Remember, every time you have a value or a variable and you are not sure what it is, debug by printing its type.

````
print(type(print))
````

```<class 'builtin_function_or_method'>```

````
print(type(sys))
````

```<class 'module'>```

````
print(type(5 / 2))
````

```<class 'float'>```

It is not anymore an integer. Dividing an integer by another integer results in a float.

````
5 // 2
````

```2```

Here the result is an integer, and it wasn’t rounded but rather truncated.

We’ve seen before the type list, that is very useful. Another useful type is a dictionary, or **dict**. It is also referred to sometimes as associative memory. You have keys, and you have values. In a list, you use indices to address the content. Otherwise it is similar.

````
{'a': 4, 'b': 'Vier'} # One way to create a 'dict'

my_dict = dict() # yet another way to create a 'dict'

my_dict['my_key'] = 'your_value'
my_dict
````

```{'my_key': 'your_value'}```

We have added an entry here to an existing dictionary. To add values to a list, we can for example do:

````
my_list.append('Marshmello')
my_list
````

```[1, 2, 4, 'Marshmello']```

There is also a useful type, a **tuple**. For example:

````
my_tuple = (1, 3, 'g')
my_tuple
````

```(1, 3, 'g')```

````
type(my_tuple)
````

```<class 'tuple'>```

You can access elements of a tuple as you do with a list, yet it is not mutable.

````
my_tuple[0] = 2
````

```
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
```

````
my_tuple.append('Baby')
````

```
Traceback (most recent call last):
 File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
```

Tuples are useful in many cases. For example we can assign values to two variables at the same time.

````
old, new = 'Trump', 'Biden'
````

Here the parentheses are implicit.
Also, sometimes a function can return multiple values, and this can be done with returning a ‘dict’, or a ‘list’, but also sometimes as a tuple.

````
for k, v in my_dict.items():
    print(k, v)
````

```my_key your_value```

Note, above is a **for** loop. Its structure somewhat resembles a function definition (the column, and the indentation).
We got here two loop variables, *k* and *v*, as the function *items* of ‘dict’ instances returns an **iterator** of two values each iteration. We then printed those two in one ‘print’ statement. We happened to have only one key-value pair in the dictionary above.

Here is another example of a 'for' loop:

````
my_sum = 0
for i in range(3):
    my_sum += i

my_sum
````

```3```

We initialized *my_sum* to zero, then we added *0*, *1*, and finally *2*, to get *3*.

````
type(range(3))
````

```<class 'range'>```

**range** resembes a list of consequtive integers that is not mutable. We did not need to create and initialize a list, and also the 'range' has the advantage that it keeps its values in its "stomach", and only makes them available when we iterate over it. If we want the explicit values, we can do:

````
list(range(5))
````

```[0, 1, 2, 3, 4]```

We could have done above also simpler, by using the builtin function ‘sum’:

````
sum(range(3))
````

```3```

Here is a small example of a function that returns two values, using the builtin functions ‘min’, and ‘max’.

````
def min_and_max(a_list):
    return min(a_list), max(a_list)

min_and_max(range(6))
````

```(0, 5)```

````
min_and_max([4, 1, 3])
````

```(1, 4)```

Next we’ll see **boolean** conditions and an **if** statement. This is also very important to control the flow of the program.

````
len(my_list)
````

```4```

````
if len(my_list) > 3:
    print('it is')
````

```it is```

And the type of the expression: *len(my_list) > 3*, is:

````
type(len(my_list) > 3)
````

```<class 'bool'>```

Below is a function to reverse a string (or a list).

    def my_reverse(a_string):
        if len(a_string) < 2:
                return a_string
        else:
                return my_reverse(a_string[1:]) + a_string[0:1]

    my_reverse('maar')

'raam'

    my_reverse([3, 4, 5])

[5, 4, 3]

Note, the implementation of the above function, is based on the function itself. This kind of implementation is called **recursion**. Recursion is a bit more advanced way of writing stuff, but sometimes it is actually simpler. If using recursion, pay attention to a **stopping condition**. The problems should become simpler and simpler, and in the final steps, you should return a simple value, as was the case above when the string was short and its reverse is actually the same value.

I’ve checked the builtin ‘reversed’ function. It behaves a little differently for a list, or for a string.

    list(reversed([1,2,3]))

[3, 2, 1]

    # this is what we had before

    list(reversed('gadol'))

['l', 'o', 'd', 'a', 'g']

    # but for a string, we’ll get the list of characters (reversed).

BTW, ‘#’ and then text is a comment, and can be used in a program to help the reader follow the logic. ‘#’ can start after some other code, and from there it is a comment.

Strings, have some functionality that we’ve not explored before, for example:

    "hello".upper()

'HELLO'

## Exercise

The exercise will be to approximate **𝝅** by **sampling**. Let’s say we have a circle with radius 1. What will be its area? Take a 1 by 1 rectangle. And draw there a quarter of the above circle. The origin ```(0, 0)``` is the center of the (¼) circle. The area of the rectangle is ```1 * 1 == 1```. The area of the ¼ circle is ```𝝅 / 4```. Let’s sample a point from the rectangle. We’ll do that by sampling *x* between 0 and 1, and *y* between 0 and 1. If ```(x, y)``` falls within the quarter circle, we’ll count it in, otherwise, we’ll not count it. After enough samples, the number of counted points, divided by the total number of samples, should be equal to ```𝝅 / 4```. As a check of your work, compare the value that you got for 𝝅 to the number you get from:

````
import math

math.pi
````

Guidance:

The following code demonstrates sampling random numbers between *0* and *1* (each of type float). Remember that you need for each iteration two random numbers, one for *x* and another for *y*, and that the point ```(x, y)``` is at square distance of ``x ** 2 + y ** 2`` from the origin:

````
import random

x, y = random.random(), random.random()

square_distance = x ** 2 + y ** 2
````

Implement your code as a function that receives a parameter for the number of trials, and returns the approximated 𝝅. It is a good idea to write the code in an editor of your preference, and to paste the code to the interactive Python shell, so you can avoid retyping the code for each fix.

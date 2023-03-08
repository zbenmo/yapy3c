# Part III

In this part of the course, we'll learn some more pure Python.
We'll revisit some of the types and constructs we've seen before and learn some new tricks.
We're also going to touch some bits and bobs that are nice to know and just waited till now.

Let's look at the following code snippet.

``` py linenums="1"
def scan(a, b, c):
    "Does something interesting with the arguments passed to it in the parameters 'a', 'b', and 'c'"
    
    for num in range(a, b):
        for add in range(c):
            print(num + add, end=', ')
        print()

scan(2, 5, 7)
```

```
2, 3, 4, 5, 6, 7, 8, 
3, 4, 5, 6, 7, 8, 9, 
4, 5, 6, 7, 8, 9, 10, 
```

The first observation I would like us to note is the string being the first expresion of the function ("Does something ..").
This is a string like any other string, it is not a comment.
And yet it is serving as a comment for the programmer, and for tools that help us edit, debug, and document the function.
Those strings are called **docstrings**. 
There is no issue in introducing those strings at the beginning of a function. You can introduce any expression anywhere you want in your program, this expression may be evaluated (depending on the program's control flow), and the program shall continue to the next expression (given that the expression does not raise an exception etc.). Having a string as the first expression had a special meaning and this convension is well integrated in the language and ecosystem.

We note that 'range' can accept more than one argument. When two arguments are given, the first is the starting point, and the second is the value beyond the last value in the range. So 'range(3)' is equivalent to 'range(0, 3)'.

We see a nested loop above. Note that importance of identation. We must be exact with our identation. When we return to a previous level, we should be in the exact column of the desired level. For example in line *7* the 'print' happens outside the *add* loop.

BTW, a string (any strings) can be given in multiple lines, when it is wrapped with """ (or with '''). For docstring this is especially useful and often used.

``` py
def deep_neural_network(how_deep):
  """
This function constructs a DNN based on your specification
Please take into consideration the benefits of a deep network,
versus the downsides."""

  pass
```

Above, I defined a function, yet gave no implementation. I used 'pass' to indicate I have no implementation (at least for now). We need to add 'pass' to make the identation clear. If we omit it, and start new expressions at the same identation of the function's defenition, the interpreter would complain that we forgot identation.

We can still call our function, exactly as expected, with:

``` py
deep_neural_network(5)
```

The return value is ```None``` which is an important value to know, it just stands for "nothing". It is useful in many places, as a default value, or just when we don't have anything better to assign, or to pass as an argument.

In 'JupyterLab', which is the interactive Python that I'm using, I can do now:

```
deep_neural_network?
```

Which gives me:

```
Signature: deep_neural_network(how_deep)
Docstring:
This function constructs a DNN based on your specification
Please take into consideration the benefits of a deep network,
versus the downsides.
File:      /tmp/ipykernel_566/1092418094.py
Type:      function
```

We've already seen 'list's, 'dict's, and 'tuple's. Let's add to this winning team also 'set's.

``` py
s1 = set("hello")
s2 = set("bye")
s1, s2
```

```({'e', 'h', 'l', 'o'}, {'b', 'e', 'y'})```

``` py
s1 & s2, s1 - s2, s2 - s1
```

```({'e'}, {'h', 'l', 'o'}, {'b', 'y'})```

Note that sets use the same curly brackets as dicts, '{}'. You can initialize a set with curly brackets, as in:

``` py
nodes_visited_by_now = {'A', 'B', 'C'}
```

If you wish to assign an empty set to a variable, use 'set()', as an empty brackets '{}' will be interpreted with an empty dict.

A lot of times, just by using those built-in containers you can achieve very complicated functionality. We will also learn in next parts to create our own classes (object oriented), yet most of your code can often be realized with the basic constructs, types, and containers, available for free in the language, familiar to your fellow programmers, and already tested and optimized for you. Try to avoid cluttering your program with too many new constructs and ideas. This is a least my recommendation, which I picked at the times I was using Ruby and following the Ruby's community. I think it is also very relevant to Python.

There are a lot more goodies to learn about Python, we've only scratched the surface. Let's learn about **comprehension**.

Consider this list of strings:

``` py
words = "Welcome to my show!".split(); words
```

```['Welcome', 'to', 'my', 'show!']```

When we 'split' a string we get a list of strings, where the splitting character(s) are removed.

Let's say we want to lower all words (we see that there is only one word, 'Welcome', at the moment but for arbitrary input we don't know in advance).
The following code shall do the work:

``` py
words_lower = []
for word in words:
    words_lower.append(word.lower())

words_lower
```

```['welcome', 'to', 'my', 'show!']```

There is a very useful construct that is argubly more readable and may be even faster.

``` py
words_lower = [word.lower() for word in words]
```

*words_lower* is now a list with values as before, in our example, ```['welcome', 'to', 'my', 'show!']```.
Since the loop only serves for going over all the items in the list *words* we might as well have it inside the creation of the new list *words_lower*. 
This construct is called **list comprehension**. With list comprehension we can also filter out values. For example, let's filter out words that are in the set ```{'from', 'to', 'cc'}```.

``` py
words_filtered = [word for word in words_lower if word not in {'from', 'to', 'cc'}]; words_filtered
```

```['welcome', 'my', 'show!']```

Note the condition at the end of the list comprehension, which allows only words that are not in the given set of words.
We could have combine lower-casing the words and the filtering. Make your own judgement what is more readable given your situation.

Let's find out how many characters in the following strings.

``` py
fruits = ["apple", "banana", "orange"]
lens = {fruit: len(fruit) for fruit in fruits}; lens
```

```{'apple': 5, 'banana': 6, 'orange': 6}```

Which shows us that we can use comprehensions also with 'dict's. We've built a new dict on-the-fly while iterating over the entries in *fruits*.

In the next example, we'll calculate a "reverse index" to a given dict.

``` py
roman_numbers = {'I': 1, 'V' : 5, 'X': 10}
arabic_numbers = {v: k for k, v in roman_numbers.items()}; arabic_numbers
```

```{1: 'I', 5: 'V', 10: 'X'}```

If we wrap an iterable, such as a list, with 'enumerate', we get a new iterable that gives us tuples. The first component of the tuple is the index of the item, and the second component is the original component in the original iterable. Wow, I've said it! A picture is worth a thusand words:

``` py
enumerate(list("groceries"))
```

```<enumerate at 0x7f1b05a48480>```

We turned a string into a list or characters and wrapped it with an 'enumerate'. The output tells us that now we have an 'enumerate'. To show the values, we can construct a list out of the 'enumerate' object we have. We could have iterated over the 'enumerate' or use it in a comprehension expression. The list construction will serve us here.

``` py
list(enumerate(list("groceries")))
```

```
[(0, 'g'),
 (1, 'r'),
 (2, 'o'),
 (3, 'c'),
 (4, 'e'),
 (5, 'r'),
 (6, 'i'),
 (7, 'e'),
 (8, 's')]
```

And we see our expected tuples.

Time for a small example.

Let's build a function that takes a roman number as a string and returns the equivalent roman number.

``` py
def from_roman(roman):
    """
    This function receives a roman number as a string and returns the number.

    >>> from_roman("VII")
    7
    >>> from_roman("IV")
    4
    >>> from_roman("XIV")
    14
    >>> from_roman("XVIII")
    18
    >>> from_roman("MMM")
    ValueError                                Traceback (most recent call last)
        ...
    ValueError: Don't know to handle 'M'.    
    """
    
    mapping = {'I': 1, 'V': 5, 'X': 10}
    
    arabic = 0
    prev_val = 0
    for c in reversed(roman):
        val = mapping.get(c, None)
        if val is None:
            raise ValueError(f"Don't know to handle '{c}'.")
        if val >= prev_val:
            arabic += val
        else:
            arabic -= val
        prev_val = val
    return arabic
```

My logic above was to go from right to left, to add when we see the same value or a bigger value (ex. from **I** to **V**),
and to substract when we see a smaller value (ex. from **V** to **I**).

To go from right to left, I've wrapped the input string *roman* with 'reversed'. 'reversed' is an iterable that gives us the items in a reversed order. When accessing my mapping dict, I have used 'get' rather than indexing notation as to avoid an exception when a key is not present. But then I have "manually" raises an exception of type 'ValueError' when we got a character that is not currently supported. Note the **f-string** used when creating the exception. f-strings are a template, and we fill the values in, between currly brackaets, with Python expression. This is very convinient way to format a string.

The '+=' and '-=' operators are used here and mean the same as is the case in the *C* language. Try to avoid using those special operators when working with complex objects, yet for simple variables of type integer in this example, this should work perfectly.

The reason it may be risky to use '+=' and '-=' with objects is that a lot of times there is not explicit implementation of the operator. Then the operator '+=', as an example, is implicitly converted for example to ```a = a + 1``` which while seems benian actually results in a new object begin assigned to *a* in the example. If some other variable or data structure (for example a dict) used to reference *a* one may believe they have the handle to the up-to-date *a* yet it is not the case. They are probably still referencing the old *a*. Just keep that in mind.

Last thing to notice is that I've added examples in the docstring. This are of the form ``` >>> expression (newline) expected output ```. This adds clarity for the intended use, it becomes part of the documentation. But there is more! One can actually execute those tests with Python built-in **doctest**.

In a lot of Python file, you'll find a 'main' function, and toward the bottom of the file, an 'if' statement:

``` py
def main():
  ...


if __name__ == "__main__":
  main()
```

When you run the file with ```python my_file.py``` the expression in the bottom is evaluated to True and the code in the *main* function is executed. when the 'if' statement is missing code in functions are not called, so you may end up not really running anything. Only code outside functions is executed. It is a good practice to wrap your code in functions and call the starting point, say, *main*, from such an 'if' statement. A file with only functions can still be useful as a part of a module (and be called from outside the file, or from the command line with the *-m* flag). Whole this long detour was to show the following:

``` py
... # code containing potentially doctests


if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

The snippet above should look for doctests in the file and should execute them, verifying the output.

There is yet another very useful function when we're deeling with sequences (a list for example) and iterations. 'zip' allows us to traverse multiple lists for example together. Examining the first elements, and then the second elements, etc.

``` py
list(zip(range(3), "abc"))
```

```[(0, 'a'), (1, 'b'), (2, 'c')]```

'zip' is useful in many cases, and you can also use more than two lists (or other iterables).

## Exrecise

I've implemented above *from_roman* with the latest things we've learn. Not sure this implementation is better.
Up to you to decide. Take from it what you like. Nothing wrong with old good loops.

Make sure you can follow what we've done here.
Can you see why using 'reversed' was not required with this implementation?

``` py
def from_roman2(roman):
    """
    This function receives a roman number as a string and returns the number.

    >>> from_roman2("VII")
    7
    >>> from_roman2("IV")
    4
    >>> from_roman2("XIV")
    14
    >>> from_roman2("XVIII")
    18
    >>> from_roman2("MMM")
    ValueError                                Traceback (most recent call last)
        ...
    ValueError: Don't know to handle 'M'.    
    """
    
    mapping = {'I': 1, 'V': 5, 'X': 10}
    
    values = [mapping.get(c, None) for c in roman]
    if None in values:
        c = next(c for c, v in zip(roman, values) if v is None) # returns the (next) first occurance
        raise ValueError(f"Don't know to handle '{c}'.")
    # the sign +1 or -1
    add_or_sub = [1 if v1 >= v2 else -1 for v1, v2 in zip(values[:-1], values[1:])] + [+1] # right most element is added.
    return sum(v * s for v, s in zip(values, add_or_sub))
```
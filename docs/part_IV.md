# Part IV

In this part we'll dive a bit into functional programming. There is a very good support for functional programming in Python. A lot of Python code mixes functional programming with object oriented programming, whatever makes sense given the context.

We've already seen the ability to declare functions, and to assign a function to a variable. A function can also be passed as an argument.

``` py
arr = [(1, 'a'), (7, 'b'), (3, 'c'), (4, 'd'), (2, 'e')]
sorted(arr)
```

```[(1, 'a'), (2, 'e'), (3, 'c'), (4, 'd'), (7, 'b')]```

What do we see? We had a list with tuples *arr*. We used the built-in function 'sorted' that receives an 'iterable' and returs a list with the element sorted. We note that when comparing tuples, the first element takes precedance over the other elements. And so the tuples were ordered by the number.

What if we wanted to sort by the string (a single character here)? Luckily 'sorted' has an optional parameter 'key'. It is optional as there is a default of *None*, and when 'key' is not provided, the default *None* is intepreted as just compare the elements themselves. Let's use the 'key' parameter.

``` py
def by_the_characted(t):
  return t[1]

sorted(arr, key=by_the_characted)
```

```[(1, 'a'), (7, 'b'), (3, 'c'), (4, 'd'), (2, 'e')]```

We can see that now we have a list sorted by the second elements of the tuples. We can also define functions "on-the-fly", without a spacific name. Those are **lambda** functions. Lambda functions do not require a return statement, it is implicit from the last expression in the "function".

``` py
sorted(arr, key=lambda t: t[1])
```

```[(1, 'a'), (7, 'b'), (3, 'c'), (4, 'd'), (2, 'e')]```

Both options are as valid, using an explicit function, or using a lambda function. Pick the one most appropriate in the relevant context.

There is yet another way to map one iterator into another, and to filter elements. We've seen explicit for loops, and we've seen comprehensions.
There are also built in 'map' and 'filter' functionalities.

``` py
sentence = "The cat sat on the mat."
map(str.upper, sentence.split())
```

```<map at 0x7fbb082cdb20>```

We got a map object. To see the values, we we can construct a list out of the map (which is an iterable):

``` py
list(map(str.upper, sentence.split()))
```

```['THE', 'CAT', 'SAT', 'ON', 'THE', 'MAT.']```

The function we used in the first argument *str.upper* was taken from the type 'str'. Another similar code can be done with using a dict for translations.

``` py
en_to_nl = {
    'The': 'De',
    'cat': 'kat',
    'sat': 'zat',
    'on': 'op',
    'the': 'de',
    'mat.': 'mat.',
}

list(map(en_to_nl.get, sentence.split()))
```

```['De', 'kat', 'zat', 'op', 'de', 'mat.']```

This time the function 'get' was taken from a specific object *en_to_nl*. As long as a simple call, with one argument, which is the current element, is possible it should work.

Note that we gave the dict on multiple lines. Python interpreter is happy with this syntax given that we've openned with curly brackets '{'. A long expression can be placed in parantheses. This should make the program a bit more readable.

``` py
# just a random example..
partial_result = (
  f1(3) +
  f2(4) / f3(5) -
  (2 if x > y else 4)
)
```

What if we needed a default, say when we don't have a translation for a word, to add the original word in uppercase?

``` py
list(map(
    lambda en_word: en_to_nl.get(en_word, en_word.upper()),
    "The dog sat on the mat.".split()
))
```

```['De', 'DOG', 'zat', 'op', 'de', 'mat.']```

When to use 'map' or 'filter' and when to use comprehensions?
The expression above could have been written as follows:

``` py
[
    en_to_nl.get(en_word, en_word.upper())
    for en_word in "The dog sat on the mat.".split()
]
```

```['De', 'DOG', 'zat', 'op', 'de', 'mat.']```

Note that we did not have to use 'list', as we're already building one, and also the expression was given in a straight forward manner rather than through a (lambda) function.

The reason that we needed 'list' when we worked with 'map' is that the caculation and memory required did not happen yet when we called 'map'. 'map' is "lazy" in the sense that no list was constructed yet, and no element was "mapped" yet. Only during the iteration the transformation happens, one element at a time, and those are collected into a list, only when we explicitly construct a list from the iterator items (by wrapping the map in 'list'). There are situations, in which a pipeline can be constructed, by passing 'map' objects into other 'map' or 'filter' objects, and only at the last step we iterate over the results, or construct a list out of those. This can save time and memory. It might result also with a bit clearer code.

To be fair with comprehensions, there is a similar way to do "lazy" evaluation. One can also do above with "comprehensions" that use '()' instead of '[]'.

``` py
l = [1, 2, 3]
l_squared = (x ** 2 for x in l)
type(l_squared)
```

```generator```

``` py
[x for x in l_squared if x > 2]
```

```[4, 9]```

Pay attention to the fact that the **generator** is now excusted:

```
[x for x in l_squared if x > 2]
```

```[]```

Meaning that if we wanted to iterate over the elements again, we needed to "restart" the generator, for example by issuing again ```l_squared = (x ** 2 for x in l)```.

Using '()' instead of '[]' is actually called **generator expression** rather than comprehension. There are places when you can even introduce such a generator expression without the parenthesis. For example:

``` py
list(x ** 2 for x in range(3))
```

```[0, 1, 4]```

Just to wrap the discussion on 'map' and 'filter' vs. comprehensions, let's have above also with 'map' and 'filter'.

``` py
l = [1, 2, 3]
l_squared = map(lambda x: x ** 2, l)
list(filter(lambda x: x > 2, l_squared))
```

```[4, 9]```

Find your own zen with either way. You can mix and match as suits you.

A generator is a conviniet was to create an iterable. A function that contains one or more **yield** expression is a generator.

``` py
def my_gen(l):
    for e in l:
        yield e + 1
        
g = my_gen([1, 2, 3]); g
```

```<generator object my_gen at 0x7fbaf1426cf0>```

If we wish to see the items, we need to iterate over the generator.

``` py
list(g)
```

```
[2, 3, 4]
```

As the generator is now excusted, if we try above again we'll end up with ```[]```. But luckily we have a function that we can call again to receive a fresh copy of a generator.

``` py
list(my_gen([1, 2, 3]))
```

```[2, 3, 4]```

A generator is usuful in many situations. Let's have a random numbers generator. Note that if is to wrap a list around it we're prbably going to fail as the iterator we're just defining is infinite (try at your own risk). Therefore we'll use it in another way.

``` py
import random

def random_generator():
  while True:
    yield random.random()

for i, r in zip(range(4), random_generator()):
  print(i, r)
```

```
0 0.04245109121862101
1 0.4875224375865369
2 0.5398443861135133
3 0.16015149066151046
```

It seems that 'zip' stops as soon as one of its iterators is excusted. In this case it was the 'range'.

``` py
for i1, i2 in zip(range(4), range(3)):
  print(i1, i2)
```

```
0 0
1 1
2 2
```

Note that the infinite 'while' loop above should not cause our program to never end as after each 'yield' the control is returned to the place in code iterating over the generator.

There are other ways to create iterators (ex. for your custom objects / classes, or a wrapper for third party constructs), and there are other usages to generators (ex. co-routines). Let's keep that in mind, yet for now, let us get acquainted with generators and make the best usage of them when relevant.

## Exrecise

We are given a text. The text contains paragraphs, each paragraph contains sentences, and each sentence contains words. One paragraph is separated from the previous one by an empty line. Sentence end with one of {'.', '?', '!'}. Words are separated with ' '. We want to report for every word in the text all the places that it appeared. A place is indicated by a tuple: (paragraph nr., sentence nr., word in a sentence nr.).

One possible approach would be to generate paragraphs, for each paragraph to generate sentences, and for each sentence to generate words.

Ex. text (*All the Worlds a Stage* by *William Shakespeare*), or at least this is what the website where I find it claims:

"""
All the world's a stage,
And all the men and women merely players;
They have their exits and their entrances,
And one man in his time plays many parts,
His acts being seven ages.
 At first, the infant,
Mewling and puking in the nurse's arms.

Then the whining schoolboy, with his satchel
And shining morning face, creeping like snail
Unwillingly to school.
 And then the lover,
Sighing like furnace, with a woeful ballad
Made to his mistress' eyebrow.
 Then a soldier,
Full of strange oaths and bearded like the pard,
Jealous in honor, sudden and quick in quarrel,
Seeking the bubble reputation
Even in the cannon's mouth.
 And then the justice,
In fair round belly with good capon lined,
With eyes severe and beard of formal cut,
Full of wise saws and modern instances;
And so he plays his part.
 The sixth age shifts
Into the lean and slippered pantaloon,
With spectacles on nose and pouch on side;
His youthful hose, well saved, a world too wide
For his shrunk shank, and his big manly voice,
Turning again toward childish treble, pipes
And whistles in his sound.
 Last scene of all,
That ends this strange eventful history,
Is second childishness and mere oblivion,
Sans teeth, sans eyes, sans taste, sans everything.
"""

For example, a start of a solution can be:

``` py
def paragprahs(text):
    yield from text.split("\n\n")

for paragraph in paragprahs(text):
    print(paragraph)
    print('-' * 20)
```

```(output omitted)```

**yield from** is a short-hand for a loop over the iterator (a list in this case) and yielding each of the elements. This is different from returning the list itself. With 'yield from' we are returning a generator that can be iterated on only once. In a way, the list that was created by the call to 'split' can be **garbage collected** when the generator returned by *paragraphs* is excusted. If we returned the list, the caller may still keep a reference to the list somewhere and hence the list may have been kept "alive" in memory.

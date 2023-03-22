# Part V

We already mentioned that almost everything in Python is an object and has a type.
We learn here to create new types, or also known as classes.

``` py
class State:
  """
  a state in the game, what cards each player has, etc.
  """

  def __init__(self):
    # for the player I start with the sum rather than the cards to assure uniformity in the randomized start
    self.player_sum = random.randint(11, 21)
    # and so for the useful Ace
    self.player_useful_Ace = random.randint(0, 1) == 1 # boolean

    self.dealer_cards = [self._random_card(), self._random_card()]

  def _random_card(self):
    return random.randint(1, 10) # 1 - Ace, 2, .. 10

  def hits(self):
    new_card = self._random_card()
    self.player_sum += new_card # note since we start with 11 we cannot add another ACE.
    if self.player_sum > 21:
      if self.player_useful_Ace:
        self.player_sum -= 10
        self.player_useful_Ace = False
    return new_card

  def stick(self):                    
    return self._dealers_turn()
```

Above is taken from a Black Jack implementation. When we need a new "State" for a game, we call it, as an example, as follows:

``` py
current_state = State()

new_card = current_state.hits()
```

The call in the example above to ```State()``` allocates space for the new object and calls the **\_\_init\_\_** function on the new object.
In the *\_\_init\_\_* function we have the opportunity to initialize member variables. In addition to the *\_\_init\_\_* we'll have usually additional functions. Most of which will have as a first parameter **self** which will be passes the relevant object. The name *self* is a convention rather than inforced. It means the object itself. The two expressions below are equivelant:

``` py
new_card = current_state.hits()

# equivalent call
new_card = State.hits(current_state)
```

The initialization function *\_\_init\_\_*, as well as other functions, can of course have additional parameters.

``` py
class Car:
  """
  This class represents a car.
  A car is needed in our system, for example with respect to the license plate registration.
  """
  
  def __init__(self, license_plate):
    self.license_plate = license_plate
    self.level = None # till we learn otherwise
      
  def indicate_in_the_parking(self, level):
    self.level = level
      
  def indicate_out_of_the_parking(self):
    self.level = None
```

``` py
my_car = Car("1234567")

my_car.indicate_in_the_parking(3)
Car.indicate_in_the_parking(my_car, 4) # you'll not see code like this usually

my_car.level
```

Which returns ``` 4 ```. Note that it is a good practice to have all the member variables initialized in the *\_\_init\_\_* even with *None* if we don't have something better.

One can add functionality to an existing class, after all a class is an object by itself.

``` py
def wash(self, outside_only=True):
    print("It is clean now.")

Car.wash = wash

my_car.wash()
```

``` It is clean now. ```

If possible, avoid using this practice, just for your own sanity. But good to remember that it is an option.

Inheritance is possible, here is a simple example:

``` py
class CompanyCar(Car):
  """
  A car that is owned by the company and is
  currently allocated to one of our employees.
  """
  
  def __init__(self, license_plate, employee):
    super().__init__(license_plate)
    self.employee = employee
      
  def remind_APK(self):
    pass


company_cars = {
    employee: CompanyCar(license_plate, employee)
    for employee, license_plate in zip(
        ["Jan S.", "Marrie W.", "Sara L."],
        ["2222222", "2222223", "2222224"]
    )
}

company_cars
```

```
{'Jan S.': <__main__.CompanyCar at 0x7fcd90087f40>,
 'Marrie W.': <__main__.CompanyCar at 0x7fcd90087c40>,
 'Sara L.': <__main__.CompanyCar at 0x7fcd90087a30>}
```

Note that in the "constructor" of *CompanyCar* we have passed *Car*.

For a better human readable representation add the **\_\_repr\_\_** member function.

``` py
def company_car_repr(self):
    return f'car {self.license_plate} used by {self.employee}'

CompanyCar.__repr__ = company_car_repr

company_cars
```

```
{'Jan S.': car 2222222 used by Jan S.,
 'Marrie W.': car 2222223 used by Marrie W.,
 'Sara L.': car 2222224 used by Sara L.}
```

Make sure the representation of the object still represents the object as this may be used for hashing etc.
With above implementation, if you change the current employee using the car,
you may not find the car object in a dict if you previously added it there as a key with the previous user.

There are other useful **Dunder** (Double Under) "magic" methods in Python that are worth to know. For example **\_\_str\_\_** that is used when converting an object to a string, ex. in ``` print(f'my object="{obj}"') ```. My intuition was to introduce *\_\_str\_\_* yet to get above it turns out that one needs actually *\_\_repr\_\_*. When *\_\_repr\_\_* is implemented while *\_\_str\_\_* is not, *\_\_repr\_\_* seems to be a fallback for example in f-strings.

``` py
def company_car_str(self):
    return f'car {self.license_plate} used by {self.employee}'

CompanyCar.__str__ = company_car_str

def company_car_repr(self):
    return f'REPR car {self.license_plate} used by {self.employee}'

CompanyCar.__repr__ = company_car_repr

f'-->{company_cars["Jan S."]}'
```

``` '-->car 2222222 used by Jan S.' ```

Yet if we 'del' *\_\_str\_\_* we get:

``` py
del CompanyCar.__str__

f'-->{company_cars["Jan S."]}'
```

``` '-->REPR car 2222222 used by Jan S.' ```

With above we've inherited functionality from *Car* also to our *CompanyCar*s.

``` py
company_cars['Jan S.'].wash()
```

``` it is clean now ```

Object Oriented Programming (OOP) is very useful and definetly worth learning. For example with **Polymorphism** one can loop for example over a list of "communication channels", and "send" a message through all of those. The implementation of the "emails" instance will possibly be different from the "SMS" one, yet the interface of "send" is the same.

While OOP brings a lot of capabilities there are issues that we should be careful with, such as multiple inheritance. When a class inherits from multiple classes, and there are conflicts, what takes precedence? How does everything work togther. There is a concept of **Mixin**s that are regular Python classes, yet are meant to be self contained, used by inheritance just to add functionality, avoiding adding member variables, so less issues with multiple inheritance.

A side note (a possible repetitive suggestion). Use object oriented as needed, yet prefer a simple existing class / container if such exists and does the work reasonably.

Next I'm going to bring a nice example of the power of OOP when used in combination with functional programming.

``` py
from itertools import permutations


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __repr__(self):
        return f'({self.a}, {self.b})'
    
    def cmp(self, other):
        """
        This function returns 1 when this object strictly dominates the other.
        It returns -1 when the other object strictly dominates this one.
        Otherwise it returns 0.
        """
        
        if (
            (self.a > other.a and self.b >= other.b) or
            (self.a >= other.a and self.b > other.b)
        ):
            return 1
        elif (
            (self.a < other.a and self.b <= other.b) or
            (self.a <= other.a and self.b < other.b)
        ):
            return -1
        else:
            return 0
        
objs = [
    MyClass(2, 3),
    MyClass(1, 2),
    MyClass(3, 1),
]

for obj1, obj2 in permutations(objs, 2):
    print(f'{obj1=}, {obj2=}, cmp={obj1.cmp(obj2)}')
```

```
obj1=(2, 3), obj2=(1, 2), cmp=1
obj1=(2, 3), obj2=(3, 1), cmp=0
obj1=(1, 2), obj2=(2, 3), cmp=-1
obj1=(1, 2), obj2=(3, 1), cmp=0
obj1=(3, 1), obj2=(2, 3), cmp=0
obj1=(3, 1), obj2=(1, 2), cmp=0
```

Makes sense? Now let's try to sort the list.

``` py
sorted(objs)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[70], line 1
----> 1 sorted(objs)

TypeError: '<' not supported between instances of 'MyClass' and 'MyClass'
```

That's a pitty. We have a (partial) order already, why can't use use it for sorting? Let's try to use *cmp*.

``` py
def use_cmp(a, b):
    return a.cmp(b) < 0

sorted(objs, key=use_cmp)
```

```
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In[74], line 1
----> 1 sorted(objs, key=use_cmp)

TypeError: use_cmp() missing 1 required positional argument: 'b'
```

'key' is expecting a function with one parameter; an object.
Then *sorted* calls this function to obtain the "key" which is then used to compare with another "key" of the other objects.
What should be do? Give up and add the '<' operator to *MyClass*?

Idea: we'll return an object as a "key". The "key" object shall keep track of the original object, and will delegate to its *cmp* when the '<' is needed.

``` py
class Helper:
    """
    Enables '<' from 'cmp'.
    """
    
    def __init__(self, obj):
        self.obj = obj
        
    def __lt__(self, other):
        return self.obj.cmp(other.obj) < 0


sorted(objs, key=Helper)
```

``` [(1, 2), (2, 3), (3, 1)] ```

We probably could have implemented *\_\_lt\_\_* directly in *MyClass* yet this would have kill the story.
In *functools* you can find *cmp_to_key* that does exacly what we've just done (``` from functools import cmp_to_key ```).

## Exercise

Are you familier with the game "Animals"?
One person picks an animal (in his head). The other person (this will be the computer in this example), tries to guess the animal.
The computer asks questions such as "Does it live in water?". The human answers with "yes" or "no".

When the computer wants to guess, it asks for example: "Is it a dog?". If the computer was right, great.
Otherwise, the computer asks three questions as follows:

- What was your animal?
(ex. a cat)
- Can you give me a question that helps to tell between a cat and a dog?
(ex. Does it barks?)
- And what would be the answer for a cat?
(ex. no)

Then the game continues. The computer get's smarter and smarter, by keeping trace of the possible animals and the questions that help to tell among those.

A possible approach can be to create for the computer a "tree". A "node" in the tree is either a question, or an animal. A question leads to two subtrees, the one if the user's answer was "no" and another if the user's answer was "yes". An animal is a leaf node.

Implement this game, potentially with a few classes such as "TreeNode", "Animal", "Question". The following may be handy.

``` py
a = input("enter you name")

a
```

I have entered 'Oren' and indeed that was the content of *a* as a str.

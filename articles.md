# Context Managers (The Magic of Python Context Managers)

Source: https://towardsdatascience.com/the-magic-of-python-context-managers-adb92ace1dd0

The `contextlib` module contains predefined context managers, for example: `redirect_stderr`.

# map(): Processing Iterables Without a Loop

Source: https://realpython.com/python-map-function/

The advantages of functional programming and using pure functions:
* Functions are isolated, so it's easier to debug and test them. Hence, the development process is easier.
* Pure functions don't change the program's state so it's easier to understand.

Common technics used for a functional programming:
* **Mapping** (`map()`): transforming values in an iterable to another values.
* **Filtering** (`filter()`): filtering out items that don't match the condition.
* **Reducing** (`reduce()`): transforming an iterable into a single cumulative value.

The `map()` function is faster than looping (because it's written in C) and it consumes less memory (because 
it returns an iterator since Python 3.x.). So, if we want to create a list object from the results, we have to
use the `list()` function. 

```python
string_numbers = ['1', '2', '5']
int_numbers = list(map(int, string_numbers))
squared_numbers = list(map(lambda x: x**2, int_numbers))

# Multiple input iterables
base = [2, 3, 4]
exp = [4, 3, 2, 1]
pow_results = list(map(pow, base, exp)) # pow() takes two arguments. Result: [16, 27, 16]
```

`functools` is a Python module that contains higher-order functions (functions that take one or more functions as arguments
and/or returns a fuction as their results).

```python
from itertools import starmap
list(starmap(pow, [(2,3), (2,2)])) # [8, 4]
```

Using the functional programming tools, like `map()`, `reduce()` and `filter()` is not exactly a Pythonic Style.
Hence, the functions can be replaced with *list comprehension* or *generator expresion*. For example:

```python
square = lambda x: x ** 2
numbers = [2, 4, 8]

# map() function
list(map(square, numbers)) # [4, 16, 64]

# list comprehension equivalent
[square(x) for x in numbers] # [4, 16, 64]

# generator expresion equivalent (iterator)
squares_generator = (square(x) for x in numbers)
list(square_generator) # [4, 16, 64]

list(square(x) for x in numbers) # [4, 16, 64]
```


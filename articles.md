# Table of Contents

* [Context Managers (The Magic of Python Context Managers)](#context-managers-the-magic-of-python-context-managers)
* [map(): Processing Iterables Without a Loop](#map-processing-iterables-without-a-loop)
* [Python 3.9 - Cool New Features](#python-39-cool-new-features)
* [Python Snippets](#python-snippets)

# Context Managers (The Magic of Python Context Managers)

Source: https://towardsdatascience.com/the-magic-of-python-context-managers-adb92ace1dd0

The `contextlib` module contains predefined context managers, for example: `redirect_stderr`.

# map(): Processing Iterables Without a Loop

Source: https://realpython.com/python-map-function/

The advantages of functional programming and using pure functions:
* Functions are isolated, so it's easier to debug and test them. Hence, the development process is easier.
* Pure functions don't change the program's state so it's easier to understand.

Common techniques used for a functional programming:
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

# Python 3.9 - Cool New Features

Source: https://realpython.com/python39-new-features/

* Better support for Time Zones.
    * We had to use the `dateutil` module in earlied versions of Python.
    * The `tzdata` package, containing IANA (Internet Assigned Numbers Authority) time zones data,
      should be regularly updated. Linux and Mac operating systems have their own IANA time zones database.
* Simple Updating of Dictionaries
    * Union operator `|` and in-place union operator `|=` for merging dictionaries and dictionary-like objects.
    * `defaultdict` = dict subclass that calls a factory function to supply missing values.
* More flexible decorators.
* Annotated Type Hints.
* Upgraded Python Parser.
    * PEG instead of LL(1).
    * The old LL(1) parser will be completely removed in Python 3.10.
    * AST = Abstract Syntax Tree.
* `“Hello world”.removesuffix(“ world”)`
* `“Hello world”.rempveprefix(“Hello “)`
* Type hint definitions for built-in types. For example `numbers: list[float]` instead of `numbers: typing.List[float]`.
* [Topological sorting](https://en.wikipedia.org/wiki/Topological_sorting), used for example inalling package dependencies.
    * `graphlib` - new model added to the standard lib.
    * This type of sorting is also useful for planning parallel tasks execution
      (https://docs.python.org/3.9/library/graphlib.html).
* Greatest Common Divisor (`math.gcd()`).
* Least Common Multiple (`math.lcm()`).
* New HTTP status codes:
    * 103 (Early Hints).
    * 425 (Too Early).
    * 419 (I'm a Teapot) - from Hyper Text Coffee Pot Control Protocol (HTCPCP) :).
* `python -X dev script_name.py` - run the script in the 
  [development mode](https://docs.python.org/3.9/library/devmode.html#python-development-mode) 
  (available since Python 3.7). 

# Python Snippets

[Useful Python snippets](https://www.30secondsofcode.org/python/p/1)

Becoming a Pythonista
=====================

This chapter is will provide a very brief review of some important python concepts which will be useful and necessary. The basic concepts will be for those who are unfamiliar with Python, but a good refresher for those who don't write in Python every day. Intermediate concepts will be great for programmers of all levels to refresh on some Python idioms. The code below will focus on Python 2.5+ (see :ref:`targetting-xo`)

Basic Concepts
--------------

PEP8 and The Zen of Python
;;;;;;;;;;;;;;;;;;;;;;;;;;

One of the most important aspects of developing in Python is the Python community. Code is meant to be read, used, and worked on by many people. As this will most likely be a group project, these things are important even in your class. PEP8_ provides a style guide for Python code. It is a lengthy document, and not everything it has to say will be immediately applicable, but come back to it. Some guidelines you may choose to ignore in your own code with no reprecussions, but some guidelines are absolutely essential. Some guidelines that are essential to follow for this course:
  * Use 4 spaces per indentation level. (Good editors will allow you to set soft-tabs to four spaces. Figure this out before you continue. When working with a team, indentation style is non-negotiable.)
  * `Rules on blank lines <http://www.python.org/dev/peps/pep-0008/#blank-lines>`_
  * `Naming conventions <http://www.python.org/dev/peps/pep-0008/#prescriptive-naming-conventions>`_ are particularly important.

The Zen of Python is a list of guiding principles behind the design of Python, and a good list of guiding principles for any project written in python. The most common way to find it is a little easter egg. In a python interpreter

>>> import this
The Zen of Python, by Tim Peters
<BLANKLINE>
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!


.. _PEP8: http://www.python.org/dev/peps/pep-0008/

Control Flow in Python
;;;;;;;;;;;;;;;;;;;;;;

The ``if`` statement acts predictably in Python.

>>> if <conditional>:
...    statement
... elif <conditional>:
...    statement
... else:
...    statement

When it comes to loops, the most preferred idiom in Python is a ``for`` loop , used in the style that most other languages refer to as a "for each" loop.

>>> for <item> in <sequence>:
...    statement

Occasionally, you will use the other looping mechanism, ``while`` (but you probably shouldn't, second-guess any use of it).

>>> while <conditional>:
...    statement

Instead of a "do-until" loop like most languages have, a common idiom is

>>> for <item> in <sequence>:
...    statement
...    if <conditional>:
...       break

>>> while True:
...    statement
...    if <conditional>:
...       break

A final useful keyword is ``pass``, which simply ends execution of the branch. This is often used to define stubs and "to-do" code.

>>> if <conditional>:
...     pass # TODO: make this "statement"

"Variables" in Python
;;;;;;;;;;;;;;;;;;;;;

Don't mistake Python for having variables, because that's not really true. Instead, there are "names" and "references. There is a good pictorial explanation of this concept `here <http://python.net/~goodger/projects/pycon/2007/idiomatic/handout.html#other-languages-have-variables>`_.

Numerics
;;;;;;;;

There are two main kinds of numerical types in Python: ``float`` and ``int``. Basically, ``float`` is used for decimal values and ``int`` is used for Integers. When possible, stick with ``int``, because computers are `not good at storing and comparing <http://en.wikipedia.org/wiki/Floating_point#Accuracy_problems>`_ ``float``. When performing operations between ``float`` and ``int``, the result will be a ``float``. 

The operators ``+`` (addition), ``-`` (subtraction), and ``*`` (multiplication), all act predictably. Some other operations that are slightly more unusual are:

  * ``x / y`` (division): quotient of ``x`` and ``y``
  * ``x // y`` (integer division): quotient of ``x`` and ``y``, rounded down.
  * ``x % y`` (remainder, or `modulo <http://simple.wikipedia.org/wiki/Modular_arithmetic>`_): remainder of ``x / y``
  * ``x ** y`` (power): raises ``x`` to the power of ``y``
  * ``abs(x)`` (absolute value, or magnitude): forces ``x`` to be positive
  * ``int(x)`` (convert to integer): converts ``x`` to integer
  * ``float(x)`` (convert to float): converts ``y`` to float

Sequence Types
;;;;;;;;;;;;;;

A sequence_ is a key concept in Python. There are many different kinds of sequences, but the basic idea is simply a bunch of data.

The list and the tuple are two of the most common sequence types. Lists are denoted by square brackets, while tuples are usually denoted by parenthesis, though they are not required. Both of them allow access by numeric keys, starting from 0.

>>> alist = [1,2,3]
>>> atuple = (1,2,3)
>>> atuple
(1, 2, 3)
>>> atuple = 1,2,3
>>> alist[1]
2
>>> atuple[1]
2
>>> alist[2]
3
>>> atuple[2]
3

The key difference between lists and tuples is that lists are mutable_, and tuples are immutable_.

>>> alist[2] = 4
>>> alist
[1, 2, 4]
>>> atuple[2] = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> alist.append(1)
>>> atuple.append(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'

Lists also have a number of other useful methods. `More on Lists <http://docs.python.org/tutorial/datastructures.html#more-on-lists>`_.

Similar to a List is the ``set``. A ``set`` is mutable, but has no specific ordering. It's faster to test membership (``in``) with a set, so a ``set`` is a good choice if the order of the elements isn't important.

>>> prepositions = set(["to", "from", "on", "of"])
>>> 'dog' in prepositions
False
>>> prepositions.add('at')
>>> 'at' in prepositions
True

Strings
;;;;;;;

Strings in Python are actually just immutable sequences of characters. Python has a `ton of built-in functions <http://docs.python.org/release/3.1.5/library/stdtypes.html#string-methods>`_ to work with strings. Remember, because Strings are immutable, you cannot modify them - instead, functions that work on strings return new strings.

You can concatenate (join) strings in python using the ``+`` operator. However, it is much preferred to **use interpolation** with ``%`` instead. This method will allow you to provide named "arguments" to the string, which will be invaluable when it comes time to internationalize your game.

Compare the difference between concatenation:

>>> "Welcome, " + user + ", you are visitor #" + visitor + "."
"Welcome, Bob, you are visitor #3 to Platipy"

And interpolation:

>>> "Welcome, %(user)s, you are visitor #%(visitor)d to Platipy." %
...		{'user' : user, 'visitor' : visitor}
"Welcome, Bob, you are visitor #3 to Platipy"

You can use escape sequences inside of string literals. To prevent them from being escaped, you can prefix the string with an 'r' (great for dealing with regular expressions and windows file systems). You can also specify that the string should be unicode with a 'u' prefix.

>>> print "New\nLine"
New
Line
>>> print r"New\nLine"
New\nLine
>>> print u"Unicode"
Unicode

Sequence Unpacking
;;;;;;;;;;;;;;;;;;

A useful Python feature is the ability to unpack a sequence, allowing for multiple assignment. You can unpack a tuple as follows:

>>> position = (5, 10)
>>> x, y = position
>>> x
5
>>> y
10

This also allows swapping without a temporary variable, due to the way evaluation and assignment works in Python.

>>> a,b = b,a
>>> a
2
>>> b
1

It is the comma that determines if an expression is a tuple, not parenthesis.

>>> one_tuple = 5,
>>> not_tuple = (5)
>>> one_tuple
(5,)
>>> not_tuple
5

Tuple unpacking is wonderful, because it allows you to have elegant multiple returns from a function.

>>> x, y, width, height = image.get_dimensions()

Comprehensions
;;;;;;;;;;;;;;

Comprehensions are a very powerful Python idiom that allows looping and filtering of data in a single expression. For a simple list comprehension, we can create a list of the squares of the integers from 0-9.

>>> squares = [x ** 2 for x in range(10)]
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

This is shorter than the equivalent loop

>>> squares = []
>>> for x in range(10):
...     squares.append(x ** 2)
... 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

and also the preferred way of doing much of functional programming in Python. You may notice that this is the same as 

>>> map(lambda x : x ** 2, range(10))
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

In addition to mapping over sequences, comprehensions also support filtering

>>> odd_squares = [x ** 2 for x in range(10) if x % 2 == 1]
>>> odd_squares
[1, 9, 25, 49, 81]

Comprehensions also support iteration over multiple sequences simultaneously.

>>> [(x,y) for x in range(3) for y in range(4)]
[(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3)]

The rule of thumb is that evaluation happens right to left in the for sequences, as the last for sequence would be like the innermost for loop.

Generator expressions are also a form of comprehension that does not have the same speed and memory overhead as list comprehensions up front. You'll see more about them in :ref:`generators-and-iterators`. If you're using Python 2.7, you also have access to dict and set comprehensions, which we won't talk about here.

Dictionaries
;;;;;;;;;;;;

A dictionary, or a dict, is the standard mapping type in Python. Dicts can be created a few ways:

>>> {'key1' : 'value1', 'key2' : 'value2'}
{'key2': 'value2', 'key1': 'value1'}
>>> dict([('key1', 'value1'), ('key2', 'value2')])
{'key2': 'value2', 'key1': 'value1'}
>>> dict(key1 = 'value1', key2 = 'value2')
{'key2': 'value2', 'key1': 'value1'}

The keys in a dictionary can be any hashable_ object.

>>> a = { (0,1) : 1, 'a' : 4, 5 : 'test', (0, 'test') : 7 }
>>> a
{(0, 1): 1, 'a': 4, (0, 'test'): 7, 5: 'test'}

.. note::
    While it is possible to include different data types in lists and dicts due to Python's loose-typing, it is almost always a bad practice and should be used with extreme care.

To retrieve values from a dictionary, you access them in the same way as lists and tuples.

>>> a[(0,1)]
1
>>> a[5]
'test'

You can also test if a key is in a dictionary using the *in* keyword:

>>> 'a' in a
True
>>> 4 in a
False

You can also add new members to the dictionary:

>>> a[7] = 12
>>> a
{(0, 1): 1, 'a': 4, (0, 'test'): 7, 5: 'test', 7: 12}

Dictionaries, like lists, provide many more useful features. See the `Python tutorial's section on dicts <http://docs.python.org/library/stdtypes.html#typesmapping>`_.

.. _hashable: http://docs.python.org/glossary.html#term-hashable
.. _immutable: http://docs.python.org/glossary.html#term-immutable
.. _mutable: http://docs.python.org/glossary.html#term-mutable
.. _sequence: http://docs.python.org/glossary.html#term-sequence

Iterating Over Sequences
;;;;;;;;;;;;;;;;;;;;;;;;

Back in ``Control Flow``, we mentioned the ``for`` loop, and how it was used to iterate over sequences. It's very convenient!

>>> for a_dog_breed in ['Labrador', 'Corgi', 'Golden Retriever']:
...    print a_dog_breed
'Labrador'
'Corgi'
'Golden Retriever'

A very common use case is for iterating over a list of numbers. One way is to use ``range`` and it's generator equivalent ``xrange`` (we'll talk about how they are different in generators; for now, just use ``xrange``).

>>> for x in xrange(3):
...    print x
0
1
2

The best way to iterate over a list and keep track of indices is to use the `enumerate <http://docs.python.org/library/functions.html#enumerate>`_ function.

>>> for index, name in enumerate(seasons)
...    print index, name
0 spring
1 summer
2 fall
3 winter

You can even iterate over dictionaries if you use the ``items`` function.
>>> for key, value in {1: 'a', 2: 'b', 3: 'c'}.items()
...    print key, value
1 a
2 b
3 c

Truth-Testing
;;;;;;;;;;;;;

There is no boolean type in Python. Anything can be evaluated for Truthiness in a conditional, however. Some things are always true, and some things are always false. You can test truthiness with the ``bool`` function.

>>> bool(True)          # True are special keywords
True
>>> bool(5)             # non-zero numbers are true
True
>>> bool(-5)            # only zero is false!
True
>>> bool([1,2,3])       # A non-empty sequence is true
True
>>> bool("Hello World") # A non-empty string is true
True
>>> bool(bool)          # functions are first-order things!
True

Often, if you can think of it as "nothing", then it will evaluate to False.

>>> bool(False)  # False is a special keyword
False
>>> bool(0)      # zero is false
False
>>> bool([])     # empty list is false
False
>>> bool("")     # empty strings are false!
False
>>> bool(None)   # The special keyword None is false
False

There are quite a few built-in operators to test conditions. There are the usual suspects defined for most types (including non-numerics!): ``<``, ``<=``, ``>``, ``>=``, ``==``, and ``!=``.

An unusual operator is ``is``, which tests reference equality, meaning that both operands are identical objects (refer to the exact same thing). ``==`` is a value equality comparison (whether the two objects compute to the same thing). You will only use ``is`` for testing against ``None`` and testing object identity. Otherwise, use ``==``. Otherwise, you will find yourself in strange situations:

>>> 10 == 10
True
>>> 10 is 10 # accidentally works because of an internal python detail
True
>>> 1000 == 10**3
True
>>> 1000 is 10**3 # behaves unexpectedly!
False

Additionally, Python does contain boolean operators, but they are not ``&&``, ``||``, and ``!`` like many other languages, they are ``and``, ``or``,  and ``not``. They are `short-circuit operators <http://en.wikipedia.org/wiki/Short-circuit_evaluation>`_ like most other languages.

Finally, you can use ``in`` to test membership.

>>> 5 in [1,2,3,4]
False
>>> 3 in [1,2,3,4]
True

Typing in Python
;;;;;;;;;;;;;;;;

There are many types in Python, and you can always find out an expression's type by using the ``type(x)`` function.

>>> type(5)
<type 'int'>
>>> type(5.0)
<type 'float'>
>>> type("Hello World")
<type 'str'>
>>> type(u"Hello Unicode World")
<type 'unicode'>
>>> type([1,2,3])
<type 'list'>
>>> type(None)
<type 'NoneType'>
>>> type(type(None))
<type 'type'>

For more information on built-in types and truth value testing, see the `Python tutorial's section on Built-in Types <http://docs.python.org/library/stdtypes.html>`_.

Functions
;;;;;;;;;

Defining a function is simple in python.

>>> def my_function(argument1, argument2):
...    statement

You usually want to return something.

>>> def mean(first, second):
...    return (first + second) / 2

You can also have default arguments for your parameters.

>>> def mean(first= 0, second= 9):
...    return (first + second) / 2
>>> mean()
5

Be wary, however, of mutable default arguments. You should almost always use None instead of mutable types, and check against None to set the actual default argument.
>>> def foo(l=[]):
...    l.append(1)
...    return l
... 
>>> foo()
[1]
>>> foo()
[1, 1]

And you can even have arbitrary arguments.

>>> def mean(*numbers): #numbers will be a tuple!
...   return sum(numbers) / len(numbers)
>>> mean(1, 8, 10, 15)
8

You can use named parameters when calling a function.

>>> mean(first= 10, second= 14)
12

And you can also accept arbitrary named parameters.

>>> def foo(*args, **kwargs):
...     print args
...     print kwargs
... 
>>> foo(1,2,3, a=4, b=5)
(1, 2, 3)
{'a': 4, 'b': 5}


Python treats functions as first-class objects, which means you can pass them around like anything else:

>>> average = mean
>>> average
<function mean at 0x000000000>
>>> mean(5,9)
7
>>> average(5,9)
7
>>> bool(mean)
True


Closures
;;;;;;;;

Functions in Python have access to names which are in their calling scope. 

>>> def make_incrementor(start = 0):
...     def inc(amount):
...         return start + amount
...     return inc
... 
>>> i = make_incrementor()
>>> i(5)
5
>>> i2 = make_incrementor(5)
>>> i2(5)
10


Exceptions
;;;;;;;;;;

Python's exceptions are the same as most other languages

>>> try:
...    dangerous_statement
... except NameError, e:    # accept a specific type of exception
...    print e
... except Exception, e:    # accept all exceptions. You should almost never do this
...    print "Oh no!"       
... finally:                # cleanup code that should run regardless of exception, even when there wasn't one
...    print 'Always run this bit'

Don't use the ``as`` keyword, it was introduced in Python 3.

.. _generators-and-iterators:

Generators and Iterators
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Iterators are objects which define how iterating, or looping, over a sequence goes, but can also be used for general iteration purposes. To get an iterator of an object, you call `iter(obj)`. The returned object will have a `next()` method which will return the next item in the sequence or iterator. When there are no more items to iterate over, it will throw a `StopIteration` exception.

>>> l = [1,2]
>>> alist = [1,2]
>>> i = iter(alist)
>>> i.next()
1
>>> i.next()
2
>>> i.next()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

Generator is the name of the pattern used to create iterators, but also refers to two convenient ways to create iterators. First, as an example of an iterator, let's write a simplified version of the `xrange` generator that takes only one argument and always starts from 0.

>>> class xrange(object):
...     def __init__(self, n):
...         self.n = n
...         self.cur = 0
...     
...     def __iter__(self):
...         return self
...     
...     def next(self):
...         if self.cur < self.n:
...             ret = self.cur
...             self.cur += 1
...             return ret
...         else:
...             raise StopIteration()
... 
>>> xrange(5)
<__main__.xrange object at 0x10b130cd0>
>>> list(xrange(5))
[0, 1, 2, 3, 4]

We see immediately that this is a bit cumbersome and has a lot of boilerplate. Generator functions are a much simpler way to write this generator. In a generator function, the `yield` keyword returns a value, an the Python interpreter remembers where evaluation stopped when yield was called. On subsequent calls to the function, control returns to where `yield` was called. `xrange` now looks like the following.

>>> def xrange(n):
...     cur = 0
...     while cur < n:
...         yield cur
...         cur += 1
... 
>>> list(xrange(5))
[0, 1, 2, 3, 4]

You can even call yield in more than one place in the code, if you wish. This simplifies the creation of generators quite a bit.

Generator expressions are also commonplace. They use the same syntax as list comprehensions, but use `()` in place of `[]`. This allows for memory efficient use of generators and iterators for manipulating data.

>>> gen = (x ** 2 for x in range(6))
>>> gen
<generator object <genexpr> at 0x10b11deb0>
>>> list(gen)
[0, 1, 4, 9, 16, 25]

For more advanced tricks with generators and iterators, see the :ref:`itertools` module.

Object Oriented Programming
;;;;;;;;;;;;;;;;;;;;;;;;;;;

Python has classes!

>>> class <name>(object):
...   <body>

After you have a class, you can make instances of it:

>>> class Dog(object):
...    pass
>>> my_dog = Dog()

Classes usually have methods. Methods are functions which always take an instance of the class as the first argument. By convention, this is always named self. Accessing methods or member variables is done by using ``self.<name>``

>>> class Dog(object):
...    def sniff(self):
...        print "Smells funny"
>>> Spot = Dog()

The constructor for a class is named ``__init__``.

>>> class Dog(object):
...    def __init__(self):
...        self.breed = "Labrador"
...    def paint_it_black(self):
...        self.breed = "Black Lab"

Don't try and put properties outside of the ``__init__`` or other function, unless you want them to be `class` properties instead of `instance` attributes. `Read about the distinction here <http://stackoverflow.com/questions/207000/python-difference-between-class-and-instance-attributes>`_

>>> class Animal(object):
...    def breathe(self):
...        print "*Gasp*"
>>> class Dog(Animal):
...    pass
>>> my_dog = Dog()
>>> my_dog.breathe()
*Gasp*

There are lots of other details about Classes that you should read up about on the `Python Docs <http://docs.python.org/tutorial/classes.html>`_.

If __name__ == "__main__":
;;;;;;;;;;;;;;;;;;;;;;;;;;

If you want to see if a script is being called as main, you can use the foloowing at the bottom of your file:

>>> if __name__ == "__main__":
...    pass # main stuff

In this class, we'll be using the launcher. So don't bother using this!

Assertions
;;;;;;;;;;

Python has assertions, which are useful for verifying argument types, data structure invariants, and generally making assumptions explicit in your programs. The syntax is straightforward.

>>> assert 1 == True
>>> assert 0 == True
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AssertionError

The Python Wiki has a good article on `using assertions effectively <http://wiki.python.org/moin/UsingAssertionsEffectively>`_

Built-in Documentation and Docstrings
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
In the interpreter, it is often useful to quickly check and see some documentation on objects you're working with. The built-in help function can quickly provide some information and a list of methods on both Python's built-in classes, and user-defined classes which are documented properly.

>>> a = [1,2,3]
>>> help(a)
Help on list object:
class list(object)
 |  list() -> new empty list
 |  list(iterable) -> new list initialized from iterable's items
 |  
 |  Methods defined here:
 |  
 |  __add__(...)
 |      x.__add__(y) <==> x+y
 
 For your own classes and functions, you should provide docstrings so that this functionality works, and also so that anyone reading your code has this information available. If a class, function, or method definition has a string before any other code, that string is interpreted as the docstring, and stored in ``.__doc__`` for that object. By convention, docstrings are written as triple-quoted strings (``"""string"""``)
 
 Help on function bake_bread in module __main__:

>>> def bake_bread(self, ingredients):
...     """
...     This function bakes a loaf of bread given an iterable of ingredients.
...     """
...     pass
... 
>>> bake_bread.__doc__
'\n    This function bakes a loaf of bread given an iterable of ingredients.\n    '
>>> help(bake_bread)
bake_bread(self, ingredients)
    This function bakes a loaf of bread given an iterable of ingredients.


Importing, Modules, and Packages
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

This `article <http://effbot.org/zone/import-confusion.htm>`_ does a good job describing importing in Python.

Advanced Concepts
-----------------

New- and Old- Style Classes
;;;;;;;;;;;;;;;;;;;;;;;;;;;

Decorators
;;;;;;;;;;

Important Decorators
;;;;;;;;;;;;;;;;;;;;

@property, @classmethod, @lru_cache, @staticmethod

Metaclasses
;;;;;;;;;;;

Context Managers
;;;;;;;;;;;;;;;;

This could be considered basic as well

Descriptors
;;;;;;;;;;;


Additional Reading
;;;;;;;;;;;;;;;;;;

Important Modules
-----------------

.. _itertools:

itertools
;;;;;;;;;

random
;;;;;;

operator
;;;;;;;;

logging
;;;;;;;

collections
;;;;;;;;;;;

os and sys
;;;;;;;;;;

pdb
;;;

json and pickle
;;;;;;;;;;;;;;;

Additional Reading
;;;;;;;;;;;;;;;;;;

http://www.doughellmann.com/PyMOTW/py-modindex.html

Third-Party Modules
-------------------
Not sure if this is necessary here? Should mention things like requests


Additional Reading
------------------

* `Hidden Features of Python on StackOverflow <http://stackoverflow.com/questions/101268/hidden-features-of-python?sort=votes#sort-top>`_ is a great QA that just details some of Python's great features. Many of them have been listed here, a few haven't. 

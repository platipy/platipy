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

Lists and Tuples
;;;;;;;;;;;;;;;;

The list and the tuple are two of the most common sequence_ types. Lists are denoted by square brackets, while tuples are usually denoted by parenthesis, though they are not required. Both of them allow access by numeric keys, starting from 0.

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


Sequence Unpacking
;;;;;;;;;;;;;;;;;;

A useful Python feature is the ability to unpack a sequence, allowing for multiple assignment. You can unpack a tuple as follows

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

Numerics
;;;;;;;;

There are two main kinds of numerical types in Python: ``float`` and ``int``. Roughly speaking, ``float`` is used for decimal values and ``int`` is used for Integers. When possible, stick with ``int``, because computers are `not good at storing and comparing <http://en.wikipedia.org/wiki/Floating_point#Accuracy_problems>`_ ``float``. When performing operations between ``float`` and ``int``, the result will be a ``float``. 

The operators ``+`` (addition), ``-`` (subtraction), and ``*`` (multiplication), all act predictably. Some other operations that are slightly more unusual are:

  * ``x / y`` (division): quotient of ``x`` and ``y``
  * ``x // y`` (integer division): quotient of ``x`` and ``y``, rounded down.
  * ``x % y`` (remainder, or `modulo <http://simple.wikipedia.org/wiki/Modular_arithmetic>`_): remainder of ``x / y``
  * ``x ** y`` (power): raises ``x`` to the power of ``y``
  * ``abs(x)`` (absolute value, or magnitude): forces ``x`` to be positive
  * ``int(x)`` (convert to integer): converts ``x`` to integer
  * ``float(x)`` (convert to float): converts ``y`` to float

Strings
;;;;;;;

Strings in Python are actually just immutable sequences of characters. Python has a `ton of built-in functions <http://docs.python.org/release/3.1.5/library/stdtypes.html#string-methods>`_ to work with strings. Remember, because Strings are immutable, you cannot modify them - instead, functions that work on strings return new strings.

You can concatenate (join) strings in python using the ``+`` operator. However, it is much preferred to use interpolation with ``%`` instead. This method will allow you to provide named "arguments" to the string, which will be invaluable when it comes time to internationalize your game.

Compare the difference between concatenation:

>>> "Welcome, " + user + ", you are visitor #" + visitor + "."
"Welcome, Bob, you are visitor #3 to Platipy"

And interpolation:

>>> "Welcome, %(user)s, you are visitor #%(visitor)d to Platipy." %
...		{'user' : user, 'visitor' : visitor}
"Welcome, Bob, you are visitor #3 to Platipy"

Truth-Testing
;;;;;;;;;;;;;

Talk about True, False

Testing for ``==`` vs ``is``

Different expressions evaluate to True and False (``[]`` and ``""``)

Python has three important objects which we have not talked about thus far, ``True``, ``False``, and ``None``. These are special objects which are globally unique within a program. In Python 3, they are all keywords, though this is not true in Python2. These objects will be important in a moment.

Python has many of the comparison operators you would expect in most other languages, like ``<``, ``<=``, ``>``, ``>=``, ``==``, and ``!=``. The comparison operators behave like you would expect, but the ``==`` operator is a bit different, and has a cousin in Python, the ``is`` operator.

``is`` is the operator for object equality, meaning that both operands are identical objects. ``==`` is a less strict equality comparison. Here's some examples to hilight the differences

Additionally, Python does contain boolean operators, but they are not ``&&``, ``||``, and ``!`` like many other languages, they are ``and``, ``or``,  and ``not``. They are short-circuit operators like most other languages.

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

Exceptions
;;;;;;;;;;


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

If __name__ == "__main__":
;;;;;;;;;;;;;;;;;;;;;;;;;;

Assertions
;;;;;;;;;;

Built-in Documentation
;;;;;;;;;;;;;;;;;;;;;;
Using dir() etc.

Importing, Modules, and Packages
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Additional Reading
;;;;;;;;;;;;;;;;;;

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

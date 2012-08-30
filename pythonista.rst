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

A useful Python feature is the ability to unpack a sequence, allowing for multiple assignment.

>>> a,b,c = 1, 2, 3
>>> a
1
>>> b
2
>>> c
3

This also allows swapping without a temporary variable, due to the way evaluation and assignment works in Python.

>>> a,b = b,a
>>> a
2
>>> b
1



Comprehensions
;;;;;;;;;;;;;;

Data types and Comparisons
;;;;;;;;;;;;;;;;;;;;;;;;;;
Need to talk about is vs ==, in, etc.

Sequences, Iterators, and Generators
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Exceptions
;;;;;;;;;;

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

Additional Reading
;;;;;;;;;;;;;;;;;;

Important Modules
-----------------

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
Becoming a Pythonista
=====================

This chapter is will provide a very brief review of some important python concepts which will be useful and necessary. The basic concepts will be for those who are unfamiliar with Python, but a good refresher for those who don't write in Python every day. Intermediate concepts will be great for programmers of all levels to refresh on some Python idioms. The code below will focus on Python 2.5+ (see :ref:`targetting-xo`)

Basic Concepts
--------------

PEP8 and The Zen of Python
;;;;;;;;;;;;;;;;;;;;;;;;;;
One of the most important aspects of developing in Python is the Python community. Code is meant to be read, used, and worked on by many people. As this will most likely be a group project, these things are important even in your class. PEP8_ provides a style guide for Python code. It is a lengthy document, and not everything it has to say will be immediately applicable, but come back to it. Some guidelines you may choose to ignore in your own code with no reprecussions, but some guidelines are absolutely essential. Some guidelines that are essential to follow for this course:
  * Use 4 spaces per indentation level. (Good editors will allow you to set soft-tabs to four spaces. Figure this out before you continue)
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

Lists, Tuples, Dicts, and Sets
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

Lists and tuples are two of the most common sequence types, or iterables. Lists are denoted by square brackets, while tuples are usually denoted by parenthesis, though they are not required. Both of them allow access by numeric keys, starting from 0.

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

The key difference between lists and tuples is that lists are mutable, and tuples are immutable.

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




Sequence Unpacking
;;;;;;;;;;;;;;;;;;

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
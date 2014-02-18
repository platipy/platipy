Introduction and Target Audience
================================

This website is a collection of wisdom learned about developing games for the `OLPC XO <http://one.laptop.org/>`_, with a special focus on the goals of the students taking CISC-374 at the `University of Delaware <http://udel.edu>`_. We won't talk too much about developing individual games, as that varies widely from year to year and team to team, but instead we'll focus on the differences and particular challenges that are faced when placing these games on the OLPC, and some ways to overcome those challenges. Each section will conclude with links for additional reading that will often include more depth and breadth than will be presented here. 

While we will focus mostly on the needs of the course at the University of Delaware, most of the material is generally applicable for developing non-PyGTK activities for the OLPC XO. We will begin with a quick introduction to the One-Laptop-Per-Child project and the XO laptop, its flagship product.

The OLPC XO
-----------

The XO was chosen as a development environment for a number of reasons. Probably the most important reason is that the middle school with which CISC374 coordinates received a donation that allows them to assign one XO to every student at the school. There is also a large educational development community around the XO and the OLPC foundation, so the hope is that the results of this course can be released to the greater community.

Sugar and Activities
~~~~~~~~~~~~~~~~~~~~

Sugar is the user interface of the XO laptop. It is designed very differently from traditional systems like Windows or OS X. Built on Fedora, there are several concepts unique to the system that you should understand before designing for it.

Key Concepts
~~~~~~~~~~~~

Activities
  Basically, an application or program. Activities are meant to be used by humans. When they run, they take up the whole screen, and it is expected that you only use one Activity at a time.
Views
  There are three "Views" on the XO: "Home", "Neighborhood", "Group". The **Home View** is a listing of all the Activities available on the XO. The **Neighborhood View** is a list of all the visible networks you can connect to. You will never use the **Group View**. You can switch between Views by using the buttons in the top-left of the Frame.
Frame
  If you hold your mouse in the corner of the screen (or press the black rectangle in the top-right corner of your keyboard), the Frame will appear. On the top bar, there are buttons to switch between the Views and running Activites. On the bottom, you can see currently connected networks, USB drives, and other system information.
Journal
  A record of activity on the XO. When you start an Activity, an entry is added to the journal. When you download a file, it is stored in the journal. When you resume a stopped Activity, its state is restored from the journal.

Important Built-in Activities
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: images/icon-terminal.png
  :align: right
  
Terminal
  The most important Activity, this is a Linux terminal. You can use it to access the underlying Linux filesystem. 
  
.. image:: images/icon-log.png
  :align: right
  
Log
  This is the second most important Activity. When you get error messages, this is where they will show up. The entries on the left are from the Activities and Services that are running or have finished since you turned on the XO. Click on them to see their output. This is the only way to get to error messages!

.. image:: images/icon-browse.png
  :align: right
  
Browse
  When you need to browse the internet, you'll use this web browser. It's basically a dumbed-down version of Firefox. You can also install Opera or Firefox if you want, but it probably won't be necessary.
 
.. image:: images/icon-maze.png
  :align: right
  
Maze
  The maze is a fun little activity where you guide a shape out of a maze. Everytime you complete a level, a larger one is generated. For some reason, people love the Maze a lot, and it makes for a good distraction.

If you're interested in more activities, there are a large number of them at the `Sugar Activity Repository <http://activities.sugarlabs.org//en-US/sugar/>`_.

Connecting to the Internet
~~~~~~~~~~~~~~~~~~~~~~~~~~
To get internet access, go to the Neighborhood (in the top-left of the Frame). You should see a bunch of circles. If you hover over these circles, you can see that they represent available networks. Choose your network, and if prompted, put in your passphrase.

If you have problems connecting, try some of these fixes.
  * Give the XO a few minutes after you've reached the home screen. Sometimes it just takes a bit of time to get itself oriented.
  * Keep the "ears" (the little swiveling bars on the XO that cover the USB ports) upwards. That's where the wifi antennae are.
  * Try removing your network history. Right click the XO symbol on the Home View, choose "Control Panel", and go to "Network". There should be a button that promises to "Discard network history". Don't worry if clicking it doesn't appear to do anything. It's a silent fix. Just try connecting again.
  * Smack your XO until you feel better.
  * Try the stuff on `this page <http://wiki.laptop.org/go/Wifi_Connectivity#Special_Considerations>`_.

Development Options
-------------------

Python
~~~~~~

As with most platforms, there are a number of options available for development. The first choice we needed to make for the XO was language. Python is the language of choice for a number of reasons. First, the vast majority of activities and most of Sugar itself are written in Python, so using the preferred language makes finding examples and documentation significantly easier. Additionally, given the tight schedule for the course, a dynamic language that allows rapid development is a good choice.

Pygame vs PyGTK+
~~~~~~~~~~~~~~~~

With Python chosen, we have two choices for a user interface that will work with Sugar: pygame and PyGTK+. PyGTK+ is a set of bindings for GTK+, a common GUI toolkit for Desktop applications. While some games may be written easily within the confines of PyGTK+, many of the game ideas which have been proposed would not, requiring much custom development of widgets and internal knowledge of GTK+.

Pygame, however, is a library made specificially for game development. It provides simple and direct ways of drawing and managing 2D images on the screen, making it a great choice for making simple games. It does, however, also have a few downsides. Most notably, hardware support with pygame is notoriously lacking, and further limited by the XO's lack of OpenGL drivers on some models. Additionally, compared to PyGTK+, pygame is a second-class citizen in OLPC development, requiring a number of hacks and workarounds. To remedy this situation, a custom library built on top of pygame, called Spyral, has been developed for this course.

Spyral
~~~~~~

In addition to Python and Pygame, the recommendation for this course is Spyral, a library built on top of pygame to provide a number of features which are useful for rapid and efficient game development. Most importantly, spyral helps provide the following:

* Some built-in core concepts of game design. Pygame is really just a wrapper for doing 2D drawing, with a few nice features like sound and input support, but doesn't provide much in terms of higher level game design concepts. Spyral provides a scene system, improved game clocks, an events system, and much more.

* An optimized method of drawing. Because pygame on the XO is not hardware accelerated, pygame's software rendering is the slowest part of every game. Spyral provides a no-hassle method of doing dirty rendering which can increase performance significantly for sprite-based 2D games

Spyral is a complete wrapper on-top of pygame, meaning that the usage of pygame should be completely hidden from the user. For advanced users, pygame is in full use behind the scenes, and with clever reading of the spyral source code, you can use it in your games, but we feel that spyral should be sufficient for most users in this course. If you find yourself in need of a feature, please contact the developers by raising a new issue on the `Spyral Github <https://github.com/platipy/spyral/issues?state=open>`_ .

Additional Reading
------------------

* For some additional information about the OLPC XO, visit the `OLPC Wiki <http://wiki.laptop.org/go/The_OLPC_Wiki>`_, though be warned that there is a lot of out of date information floating around various areas.

* For some additional motivation for Python and PyGTK+ and Pygame, the `FLOSS Manuals guide to "Make your own sugar activities" <http://www.flossmanuals.net/make-your-own-sugar-activities/>`_ is a good read.

* For a more in-depth look at the motivation behind spyral, see our :ref:`Contributor Application <contributor_application>`.
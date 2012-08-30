.. _targetting-xo:

Targetting the OLPC XO
======================

Guidelines For Starting Your Game
---------------------------------

* Fix the resolution at 1200x900
* Use the Activity Bundle Skeleton
* Using Version Control
* Set up an icon
* Etc.
* Python Version Information
* Pygame Version Information

Screen Size
~~~~~~~~~~~

The XO screen has a resolution of 1200x900 and a dot pitch of 200dpi. For comparison, most laptop screens are either 1024x768 or 1366x768. This may cause problems when developing your application off the XO, unless you take advantage of Spyral's built-in scaling functionality. 

You can use the following lines of code to move the Activity window around when developing off the XO. Put them near the very beginning of your project, before Spyral or Pygame initializes.
  .. code:: python
  
    # for centering, use
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # for arbitrary placing, replace x and y and use
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x, y)

If you don't need every centimeter of screen space, you might consider putting a 75 pixel decorative border around your game. This way, when the Frame pops up (which can happen very easily by accident), it won't cover any game elements, since it is also 75 pixels thick.

Versions
~~~~~~~~

XO laptops do not run the most current version of most of their software. If you want to be a good XO developer, you'll want to develop using the following versions.
  * Python `2.5 <http://www.python.org/getit/releases/2.5.4/>`_: You might be able to get away with using 2.6 or even 2.7, but absolutely do not bother using 3.*. 
  * Pygame `1.8.1 <http://pygame.org/download.shtml>`_ (Scroll to the bottom for the 1.8.1 release): Make sure you are not using the most up-to-date version of Pygame (1.9), because there are several inconsistencies. For instance, the Color package is not present in 1.8.1.

The CISC374 Activity Bundle Skeleton
------------------------------------

Using The Test Launcher
-----------------------

Testing Inside Sugar
--------------------

Testing on the OLPC XO
----------------------

Packaging and Distributing
--------------------------

Translationing
--------------
Getting Started
===============

Required Software
-----------------

XO laptops do not run the most current version of most of their software. If you want to be a good XO developer, you'll want to develop using the following versions.
  * Python `2.5 <http://www.python.org/getit/releases/2.5.4/>`_: You might be able to get away with using 2.6 or even 2.7, but absolutely do not bother using 3.*. 
  * Pygame `1.8.1 <http://pygame.org/download.shtml>`_ (Scroll to the bottom for the 1.8.1 release): Make sure you are not using the most up-to-date version of Pygame (1.9), because there are several inconsistencies. For instance, the Color package is not present in 1.8.1. The documentation for 1.8.1 is provided :download:`here <files/pygame-1.8.1-docs.zip>`.

If you cannot get older versions installed, Python 2.7 and the latest version of pygame are acceptable, but make sure you are testing often on the XO.

Setting up the Launcher
-----------------------

The CISC374 Launcher is a tool provided for you that takes a lot of the boilerplate out of writing your game. You can download it `here <http://link_uploaded_soon>`, and extract it to whereever you will be working.

Once you've extracted the launcher, you should rename the Example.activity directory to a name of your choice. Since you probably don't yet know the name of your game, you can name it after yourself for now. Once it has been renamed, you should run *init.py* in a terminal. It will prompt you for some values for setting up your activity. Right now, these aren't too important, but come back to this section later when you're ready to pick a name and run your activity on the XO.

Running the example
-------------------

With the launcher installed, you can run the example game which comes with it, a simple version of Pong. For running on your regular computers, the file dev_launcher.py is the way to launch the game. It comes with a few options, but for now there are two important ones which we'll worry about. The first is *-r*, which allows you to specify a resolution. By default, the launcher will autodetect your screen's resolution. Because the XO uses a screen resolution of 1200 by 900, all games which we write in that class will have that resolution. This means that on most of your machines, the image will be streched because the aspect ratio does not match. For development, you should pick a good resolution which fits within your screen, and pass that as an option to the dev_launcher. For instance, I usually run "python dev_launcher.py -r 800 600".

The second important launcher option is "-h". It will show you other options available in the launcher. We'll come back to those later.



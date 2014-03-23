Getting Started
===============

Required Software
-----------------

.. warning:: XO laptops do not run the most current version of most of their software. If you want to be the best XO developer possible, you'll want to use the earlier versions. If you cannot get older versions installed, Python 2.7 and the latest version of pygame are acceptable, but make sure you are testing often on the XO. There are also programs that can search your source code and make sure it is `2.5 compliant <https://github.com/ghewgill/pyqver>`_ .
   
Spyral has several dependencies. Moreover, the installation process is very different on Mac and Windows. Please follow the directions that are appropriate for your system.

Mac
***

#. Install Python
#. Install setuptools
#. Install pip
#. Install greenlets
#. Install pygame
#. :download:`Download Pong <files/Pong-ea1.0-sp0.9.6.zip>`

Unix
****

#. sudo apt-get install python-setuptools
#. sudo apt-get install python-pip
#. sudo apt-get install python-pygame
#. sudo pip install greenlet
#. sudo pip install parsley
#. :download:`Download Pong <files/Pong-ea1.0-sp0.9.6.zip>`

Windows
*******

There are several steps to getting python and spyral fully running on your PC. 

.. note:: even if you have a 64-bit machine, use the 32-bit version of Python (it's still more stable). 

#. **Python**: Python is the name of the language and the interpeter. Use `2.7 <http://python.org/ftp/python/2.7.6/python-2.7.6.msi>`_ since 2.5 is no longer easily available on Windows.
#. **Greenlets**: Greenlets is a powerful module for adding multiprocessing. Download version 0.4.2, for windows 32-bit 2.7 Python, of `greenlets <http://www.lfd.uci.edu/~gohlke/pythonlibs/#greenlet>`_ .
#. **Pygame**: Pygame is the game development library for Python that is installed on the XOs. Download the latest version of `pygame <http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi>`_ .
#. **SetupTools**: This is a python module for quickly installing new python modules. Download version 2.2, for windows 32-bit 2.7 Python of `setuptools <http://www.lfd.uci.edu/~gohlke/pythonlibs/#setuptools>`_ .
#. **Pip**: SetupTools is a requirement for an even better installer named Pip. Download version 1.5.4, for windows 32-bit 2.7 Python, of `pip <http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip>`_ .
#. **Add Python to your Path**: To be able to directly run python from the command line, you must add the path to Python to your System's Path. This `Stack Overflow <http://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-7>`_ gives general directions, but you might need to google search for directions that work for your version. Make sure you add both the Python folder itself and the Scripts subfolder folder!
#. **Parsley**: This is a module that Spyral uses to handle Spyral Style Files. Use the following on the command line: ``pip install parsley``
#. **Download Pong Example**: :download:`Download Pong <files/Pong-ea1.0-sp0.9.6.zip>`

.. note:: Use PowerShell instead of the default Windows Command Line. It has a lot of unix features like ``ls`` and should already be installed on your system.


Setting up the Launcher
-----------------------

The Dev Launcher, named Example.activity, is a tool provided for you that takes a lot of the boilerplate out of writing your game. The download links can be found at :ref:`downloads`, and extract it to whereever you will be working.

Once you've extracted the launcher, you should rename the Example.activity directory to a name of your choice. Since you probably don't yet know the name of your game, you can name it after yourself for now. Once it has been renamed, you should run *init.py* in a terminal. It will prompt you for some values for setting up your activity. Right now, these aren't too important, but come back to this section later when you're ready to pick a name and run your activity on the XO.

The launcher contains a variety of other folders and directories. Many of them will be important later, and a few of them you can ignore entirely. Here's a summary of what's included:

================ ===========
File             Description
================ ===========
activity.py      The activity launcher required for the XO. You should never have to edit this file.
dev_launcher.py  This is the launcher that you will use during development. It supports a variety of options, you should never have to edit this file.
init.py          A script which does some setup for running your game as an activity on the XO. You should never have to edit this file.
setup.py         A script which will provide a number of way for you to deploy your game for testing or when you are ready for release. We'll come back to setup.py in a later chapter. 
activity/        This directory contains some metadata required for the XO. It can be modified directly, or generated for you by init.py. Until you have run init.py, this directory will be empty.
dist/            When you are building with *setup.py*, the output will go in here. Any files in this directory will be ignored when building.
game/            This is the directory where all your game assets will go. All the code, artwork, fonts, etc. should be placed in here. This is to facilitate updating the launcher in the future and keeping the directory structure clean.
libraries/       This directory contains any pure python libraries that you wish to distribute with your game.
locale/          This is a build output directory, like *dist*, except for built translations. You should never be placing things in here by hand
po/              This directory contains source files for translations. You can read more about this in the section on Translating
profiles/        This directory will contain the output from the performance profiler built into the development launcher.
skel/            This directory contains support files for init.py. You can safely ignore it.
================ ===========

Running the Example
-------------------

With the launcher installed, you can run the example game which comes with it, a simple version of Pong. For running on your regular computers, the file dev_launcher.py is the way to launch the game. It comes with a few options, but for now there are two important ones which we'll worry about. The first is *-r*, which allows you to specify a resolution. By default, the launcher will autodetect your screen's resolution. Because the XO uses a screen resolution of 1200 by 900, all games which we write in that class will have that resolution. This means that on most of your machines, the image will be streched because the aspect ratio does not match. For development, you should pick a good resolution which fits within your screen, and pass that as an option to the dev_launcher. For instance, I usually run "python dev_launcher.py -r 800 600".

The second important launcher option is "-h". It will show you other options available in the launcher. We'll come back to those later.

Modifying the Example
---------------------

Once you're ready to start modifying the example code, head into the *game* directory. Here, you will find the code which is actually of interest to you. In the next chapter, we'll build the game you see in the example from the ground up.

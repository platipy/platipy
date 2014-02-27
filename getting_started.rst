Getting Started
===============

Required Software
-----------------

.. warning:: XO laptops do not run the most current version of most of their software. If you want to be the best XO developer possible, you'll want to use the earlier versions. If you cannot get older versions installed, Python 2.7 and the latest version of pygame are acceptable, but make sure you are testing often on the XO. There are also programs that can search your source code and make sure it is `2.5 compliant <https://github.com/ghewgill/pyqver>`_ .
   
Spyral has several dependencies. Moreover, the installation process is very different on Mac and Windows. Please follow the directions that are appropriate for your system.

Mac
***

1. Install Python
2. Install setuptools
3. Install pip
4. Install greenlets
5. Install pygame
6. Download Pong Example

Windows
*******

------- --------------------- -----------------------------------------------------
Step #  Name                  Description                                          
------- --------------------- -----------------------------------------------------
1.      Python                The Python interpreter                               
2.      Setuptools            A tool for installing python software                
3.      Pip                   A better tool for installing (requires setuptools)   
4.      Greenlets             A tool for adding parallel processing to python      
5.      Pygame                The game dev library that Spyral builds on           
7.      Spyral Pong example   A simple game of Pong, with spyral included          
------- --------------------- ----------------------------------------------------- 

   
  * Python `2.5 <http://www.python.org/getit/releases/2.5.4/>`_: You might be able to get away with using 2.6 or even 2.7, but absolutely do not bother using 3.*. 
  * `Pygame <http://pygame.org/download.shtml>`_: Version 1.8.1 is the best to work with, but any version should work. Users for some operating systems may have to use the newest versions.



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

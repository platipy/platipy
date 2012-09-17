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

The launcher contains a variety of other folders and directories. Many of them will be important later, and a few of them you can ignore entirely. Here's a summary of what's included:

  | *Example.activity/activity.py* - The activity launcher required for the XO. You should never have to edit this file.
  | *Example.activity/dev_launcher.py* - This is the launcher that you will use during development. It supports a variety of options, you should never have to edit this file.
  | *Example.activity/init.py* - A script which does some setup for running your game as an activity on the XO. You should never have to edit this file.
  | *Example.activity/setup.py* - A script which will provide a number of way for you to deploy your game for testing or when you are ready for release. We'll come back to setup.py in a later chapter. 
  | *Example.activity/activity/* - This directory contains some metadata required for the XO. It can be modified directly, or generated for you by init.py. Until you have run init.py, this directory will be empty.
  | *Example.activity/dist/* - When you are building with *setup.py*, the output will go in here. Any files in this directory will be ignored when building.
  | *Example.activity/game/* - This is the directory where all your game assets will go. All the code, artwork, fonts, etc. should be placed in here. This is to facilitate updating the launcher in the future and keeping the directory structure clean.
  | *Example.activity/libraries/* - This directory contains any pure python libraries that you wish to distribute with your game.
  | *Examples.activity/locale/* - This is a build output directory, like *dist*, except for built translations. You should never be placing things in here by hand
  | *Examples.activity/po/* - This directory contains source files for translations. You can read more about this in the section on Translating
  | *Examples.activity/profiles/* - This directory will contain the output from the performance profiler built into the development launcher.
  | *Examples.activity/skel/* - This directory contains support files for init.py. You can safely ignore it.

Running the Example
-------------------

With the launcher installed, you can run the example game which comes with it, a simple version of Pong. For running on your regular computers, the file dev_launcher.py is the way to launch the game. It comes with a few options, but for now there are two important ones which we'll worry about. The first is *-r*, which allows you to specify a resolution. By default, the launcher will autodetect your screen's resolution. Because the XO uses a screen resolution of 1200 by 900, all games which we write in that class will have that resolution. This means that on most of your machines, the image will be streched because the aspect ratio does not match. For development, you should pick a good resolution which fits within your screen, and pass that as an option to the dev_launcher. For instance, I usually run "python dev_launcher.py -r 800 600".

The second important launcher option is "-h". It will show you other options available in the launcher. We'll come back to those later.

Modifying the Example
---------------------


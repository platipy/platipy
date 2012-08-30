Introduction and Target Audience
================================

This document is intended to be a collection of the wisdom learned about developing games for the OLPC XO, with a special focus on the goals of the students taking CISC374 at the University of Delaware. We won't talk too much about developing individual games, as that varies widely from year to year and team to team, but instead we'll focus on the differences and particular challenges that are faced when placing these games on the OLPC, and some ways to overcome those challenges. Each section will conclude with links for additional reading that will often include more depth and breadth than will be presented here.

While we will focus mostly on the needs of the course at the University of Delaware, most of the material is generally applicable for developing pygame-based activities for the OLPC XO.

The OLPC XO
-----------

* Talk about Chester and why OLPCs. Talk about the hardware on XO-1 and XO-1.5 (also perhaps XO-1.75). Compare the hardware to modern cellphones. Be sure to mention screen resolution, it's an important factor *

Sugar and Activities
--------------------

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

Pygame and Spyral
-----------------

* Talk a bit about why pygame was chosen, the upsides and downsides to that. Talk briefly about why spyral was written, the upsides and downsides to using spyral, and the benefit it has been to the course *

Alternatives to Pygame
----------------------
* Talk about GTK, about why other toolkits are generally not an option *

Additional Reading
------------------
* Some links to the OLPC wiki, pygame's about, spyral's about, pygtk's about, cisc374 wiki, etc.
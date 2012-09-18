Your First Game: Pong
=====================

Now that you've got the example launcher up and working, let's start from scratch and write a game. For the example, we'll write Pong. To begin, clear out the *game/* directory and follow along as we rewrite it.

In order for the Launcher to find your game, you must make the *game/* directory be an importable python module by creating *game/__init__.py* (you can read more about Python Packaging `here <http://docs.python.org/tutorial/modules.html#packages>`_). The Launcher expects this file to have a *main* function which pushes the first ``Scene`` for the game on the ``Director``'s stack.

Scenes and the Director
-----------------------

The ``Director`` and ``Scenes`` are the most fundamental way in which to organize a game in Spyral. At any given time, a Scene is running and controlling the game. The Director is a stack that manages and moves between Scenes. The top Scene on the stack is the currently Scene, and transitions require adding pushing new Scenes or popping old ones. Your game will have many Scenes (perhaps representing a main menu, a character select screen, an individual level, or a pause menu), but there is only ever one Director.

Our Pong game will eventually have two Scenes: a simple menu, and the actual Pong game. For now, let's make an empty class to represent the second of those two Scenes. Then we can have the *main* function push that Scene onto the top of the Director's stack. To keep our code organized, we'll split this into multiple files.

.. topic:: __init__.py

    .. literalinclude:: pong/1/__init__.py
        :linenos:

.. topic:: pong.py

    .. literalinclude:: pong/1/pong.py
        :linenos:
    
Scenes have four important functions to implement. The first two (and the most important) are *update* and *render*. These are called by the Director at regular intervals, in the Update and Render loops. You can change the length of the intervals by controlling the clock (TODO: clock link), but we should be fine with the default interval of 30 times per second.

The render function is where your Scene should handle any tasks related to drawing. Often, this function will be quite simple, consisting only of drawing groups, which we will learn about soon. The update function is where non-drawing based calculations will take place. This is where you'll write code which does physics simulations and handles user input.

The other two functions in a Scene are the constructor (*__init__*) and *on_enter*. We'll keep them as stubs for now.

.. topic:: pong.py

    .. literalinclude:: pong/2/pong.py
        :linenos:


Cameras
-------
Now that we've gotten a template for our scene set up, we need to define a camera. Cameras in spyral are where we will draw to. They support offsets and scaling, but for a simple game, we'll only need one camera. To make a camera, we'll ask the parent camera to make a new camera. We use this because the parent camera will know some details about the actual screen we're drawing to, whose resolution we don't directly control. We'll make a child camera where we specify the resolution that we'll be using internally for our game. Spyral and the launcher will handle scaling the game and setting up the screen's resolution to something that your machine can use. Since we're going to be targetting the XO, we'll use 1200x900 as the screen resolution.

.. topic:: pong.py

    .. literalinclude:: pong/3/pong.py
        :linenos:
        :emphasize-lines: 8

For now, this is all we need to know about cameras.




Animation and Collision Detection
---------------------------------
We'll have them animate the ball here, and show how we can use collision detection to have the ball bounce off the four edges of the screen. 

Keyboard Input
--------------
We'll show how we can use keyboard input to control and move the paddles. 

Fonts and Scoring
-----------------
We'll show how to render the score text and place it on screen

Putting it all together
-----------------------
We'll take everything we've done and put it together. We'll add the balls colliding with the paddle, and colliding with the left and right edges increasing the score

Scenes and the director part 2
------------------------------
Now we can show how to make the menu, since we know how to render text, and how to accept input, so we can make a menu that just says press space to enter game, and pushes into the game, and shows how the game can pop to exit, and how popping from the menu will close the game.

.. automodule:: spyral.scene
   :members:
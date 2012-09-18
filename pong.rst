Your First Game: Pong
=====================

Now that you've got the example launcher up and working, let's start from scratch and write a game. For the example, we'll write Pong. To begin, clear out the *game/* directory and follow along as we rewrite it.

In order for the Launcher to find your game, you must make the *game/* directory be an importable python module by creating *game/__init__.py* (you can read more about Python Packaging `here <http://docs.python.org/tutorial/modules.html#packages>`_). The Launcher expects this file to have a *main* function which pushes the first ``Scene`` for the game on the ``Director``'s stack.

Scenes and the Director
-----------------------

Scenes and the director are the most fundamental way in which we organize a game. At any given time, a scene is what is running and controlling the game. Spyral's director is the manager for scenes, that handles moving between scenes. It maintains a stack of scenes which are running. For our game, we'll end up creating two scenes, one for a simple menu, and one that will actually be our game. For now, let's make an empty class for our game, and push it onto the director's stack. For organization, we'll split this into a few files.

.. topic:: __init__.py

    .. literalinclude:: pong/1/__init__.py
        :linenos:

.. topic:: pong.py

    .. literalinclude:: pong/1/pong.py
        :linenos:
    
    
Scenes consist of a few important methods. The two most important are *update* and *render*. These are often referred to as the update and render loops, because they are called regularly by the director. The director handles calling these two functions on regular intervals. You can specify how often they are called by controlling the clock (TODO: link). For now, just know that by default, render and update are both called around 30 times per second.

The render function is where your scene should handle any tasks which are related to drawing. Often, this function will be quite simple, consisting only of drawing groups, which we will learn about soon. The update function is where non-drawing based calculations will take place. This is where you'll write code which does physics simulations and handles user input.

Other important functions are of course the constructor, and a function called on enter. We'll go ahead and fill those in with stubs for now.

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
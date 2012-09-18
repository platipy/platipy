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
    
Scenes have four important methods to implement. The first two (and the most important) are `update` and `render`. These are called by the Director at regular intervals, in the Update and Render loops. You can change the length of the intervals by controlling the clock (TODO: clock link), but we should be fine with the default interval of 30 times per second.

The render method is where your Scene should handle any tasks related to drawing. Often, this method will be quite simple, consisting only of drawing groups, which we will learn about soon. The update method is where non-drawing based calculations will take place. This is where you'll write code which does physics simulations and handles user input.

The other two methods in a Scene are the constructor (`__init__`) and `on_enter`. We'll keep them as stubs for now.

.. topic:: pong.py

    .. literalinclude:: pong/2/pong.py
        :linenos:


Cameras
-------

Another important concept in Spyral are ``Cameras``. Every Scene has one or more Cameras, all based on a Parent Camera. Having multiple cameras can be useful for making split screens and Head's-Up Displays (HUDs), since they support offsets, clipping, and scaling. Pong doesn't require any of these fancy features, so we'll only need one child camera. To make a child Camera, you must specify the resolution; since we're targetting the XO, we'll use 1200x900 as the screen resolution.

*Note that when we override an inherited method, we use `super` to first call the parent version of the method.*

.. topic:: pong.py

    .. literalinclude:: pong/3/pong.py
        :linenos:
        :emphasize-lines: 8

For now, the only other thing we need to know about cameras is that they support setting the background through the ``set_background`` method, but to do this, we'll first need to learn about ``Images``.

Images
------

Images in spyral are the basic building blocks of drawing. They are conceptually simple, but there are many methods to manipulate them. It is worthwhile to spend some time reading the docs on :ref:`spyral_Image`. To make our background, we will
  * create a new image using the constructor *Image*, sized to the background,
  * *fill* this image with black, and finally,
  * assign it as the background to the camera using *set_background*

.. topic:: pong.py

    .. literalinclude:: pong/4/pong.py
        :linenos:
        :emphasize-lines: 11-13

Now that we have a background, we'll want to create Images that represent the paddles and ball in Pong. For this, we'll talk about Sprites and Groups.

Sprites and Groups
------------------

Sprites are an Image along with some information about where and how to draw them. Sprites allow us to control things like positioning, scaling, rotation, and more. There are also more advanced Sprites, including ones that can do animation. For now, we'll work with basic sprites, but you can read more about the available sprites in :ref:`spyral_Sprites`.

Groups are a way of organizing sprites together - all Sprites live in a Group, which are then drawn together. Each Group must be associated with a Camera. Like with sprites, there are some advanced Groups. You can read about all the methods on Groups and about the other types of Groups in :ref:`spyral_Groups`.

For now, we'll 
   * create an Image that represents a paddle,
   * create two Sprites, and assign the paddle Image to both sprites,
   * position the sprites close to the left and right of the screen, using the sprite's anchor attribute to improve positioning,
   * create a Group, 
   * add both Sprites to this Group, and finally,
   * tell the Group to draw in the ``render`` method of our Scene.

.. topic:: pong.py

    .. literalinclude:: pong/5/pong.py
        :linenos:
        :emphasize-lines: 12-36, 45-46
        
Animating the Ball
------------------

Next, we'll add a ball, but we'll treat it differently than the paddles. The ball is going to move on it's own, so we'll make a `Ball` class, inheriting from the `Sprite` class and implementing it's `update` method. A Sprite's `update` method is called by its Group's `update`, which is in turn called by the Scene's `update`. A little bit convoluted, but it helps a lot when structuring larger programs.

The ball's constructor will handle picking a random angle and setting two velocity attributes on the sprite, and the update method will handle moving them. So far, our new code looks like this.

.. topic:: pong.py

    .. literalinclude:: pong/6/pong.py
        :linenos:
        :emphasize-lines: 2-3, 8-31, 70, 75, 93
        
Collision Detection
-------------------

Next, we'd like to have our ball interact with the sides of the game board, and with the paddles. We'll do two different types
of collision detection here just to showcase them. Which you use will depend largely on the game.

First, we'll have the ball bounce off the top and bottom of the screen. For this, we'll do simple checks on the y coordinate of the ball. You may remember that we used a center anchor on the ball, so the coordinates are relative to the center of the ball. To remedy this, we'll use the Sprite method `get_rect()`, which gives us a rectangle that represents the drawn area of the sprite, and we can check it's top and bottom attributes. When we see that they have passed the ceiling or the floor, we'll flip the x component of the velocity.

.. topic:: pong.py

    .. literalinclude:: pong/7/pong.py
        :linenos:
        :emphasize-lines: 43-62, 99-100
        
Next, we'll have the ball collide with the two paddles. We'll make another method in the `Ball` class called `collide_paddle`, and we'll have it take in a Sprite. It will check for collisions using the `Rect.collide_rect` method for rects, and flip the ball's x coordinate if it collides. We'll call `collide_paddle` in our Scene's `update` method, giving it the paddles.

.. topic:: pong.py

    .. literalinclude:: pong/8/pong.py
        :linenos:
        :emphasize-lines: 122-123, 64-66
        

Animation
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

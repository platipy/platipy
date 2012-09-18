Your First Game: Pong
=====================

Now that you've got the example launcher up and working, let's start from scratch and write a game. For the example, we'll write Pong, the example which is included. But for now, go ahead and clear out the *game/* directory, and you can follow along here as we rewrite it.

As the first step, the launcher API is quite simple. It requires that the *game/* directory be an importable python module, so let's go ahead and make an *__init__.py*. The second requirement is that the module has a function named *main* which pushes the first ``Scene`` for the game on the stack.

Scenes and the director
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

For now, the only other thing we need to know about cameras is that they support us setting the background through a ``set_background`` method, but to do this, we'll first need to learn about images.

Images
------
Images in spyral are the basic building blocks of what we're going to draw. They're really simple, so go ahead and read the API page on :ref:`spyral_Image`. Having done this, we know that we can make a new image that is the size of the camera, fill it with a color for our background, and we'll set it as the camera's background.

.. topic:: pong.py

    .. literalinclude:: pong/4/pong.py
        :linenos:
        :emphasize-lines: 11-13

Now that we know how to create images, we can easily create images that represent the paddles and the ball in pong, but we don't yet know how to draw them. For this, we'll talk about Sprites and Groups

Sprites and Groups
------------------

Sprites are a combination of an image which we want to draw, along with some information about where and how we wish for them to be drawn. Sprites allow us to control things like positioning, scaling, rotation, and more. There are also more advanced sprite groups for a variety of different purposes, like animation. For now, we'll work with basic sprites, but you can read more about some of the available sprites in :ref:`spyral_Sprites`.

Groups are a way of organizing sprites together. Groups are what we will ask to draw, and they will draw all of the sprites assigned to them. Each group must be associated with a camera so that it knows where to draw its sprites. Like with sprites, there are some different groups that can be used for other purposes. You can read about all the methods on groups and about the other types of groups in :ref:`spyral_Groups`.

For now, we'll create an image that represents a paddle. We'll then create two sprites, and assign the image to both sprites. We'll position the sprites close to the left and right of the screen, and we'll use the sprite's anchor attribute to help us with positioning. We'll then create a group, and we'll add both sprites to this group. We'll also tell the group to draw in the ``render`` method of our scene.

.. topic:: pong.py

    .. literalinclude:: pong/5/pong.py
        :linenos:
        :emphasize-lines: 12-36, 45-46
        



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

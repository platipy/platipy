Animations Tutorial
===================

Animations are a very useful feature for making things move and change over time.
They work by `interpolating <http://simple.wikipedia.org/wiki/Interpolation>`_ a property over time.
When you interpolate, you mathematically calculate changes from an initial value to a final value.

Remember back in Algebra, when you were given two points, and had to find a line that fit them?
And then in Algebra 2, you were taught that you could fit curves to multiple points.
Well, this is a little bit like that; you specify end points, a duration, and a mathematical function to Spyral, and it'll handle the rest.
The most common case is for movement; changing a Sprite's :func:`x <spyral.Sprite.x>` and :func:`y <spyral.Sprite.y>` position over time.

To get an idea of what interpolation can look like, check out this page of `easings <http://easings.net/>`_.

So let's start with a really simple game with just a sprite in the middle of the room that moves horizontally across the room using a linear interpolation over the ``x`` attribute for 5 seconds.

.. topic:: game/animating.py

    .. literalinclude:: tutorials/animations/1/animations.py
        :linenos:
        :emphasize-lines: 

.. note::
    
    If you have an animation running when the game starts, the first few frames might not be as the program loads. That means your animation might already be in progress by the time you're able to see it. You might consider having the animation triggered by a mouse or keyboard event.

We could also make it go vertically.

We could move quadratically, so that it starts slow and then picks up speed.

Or start fast and then slow down.

Or move back and forth.

.. code-block::

    self.block.animate(Animation('x', easing.Linear(0, 600), duration = 3.0))

Other Attributes
----------------

But animations can be used for more than just positions. You can iterate over images, for instance.

Or visibility

You can even iterate over your own custom variable.

Animation Events
----------------

An animation.end event is triggered when an animation is complete.

Combining Animations
--------------------

You can make animations run at the same time by adding them together:

    first_animation = 

Or one after another

A special kind of animation is the DelayAnimation, which let's you add delays.

Stopping Animations
-------------------

If an animation is not set to ``loop``, then it will stop after a single execution.
If you need to stop earlier, you can do it by :func:`stop_all_animations <spyral.Sprite.stop_all_animations>`:

.. code-block::
    
    spyral.register.event("input.mouse.down", self.block.stop_all_animations)

Or by passing in a specific animation to :func:`stop_animation <spyral.Sprite.stop_animation>`:

.. code-block::
        
    def __init__(self, scene):
        ...
        self.moving_animation = Animation('x', easing.Linear(0, 600), duration = 3.0)
        spyral.register.event("input.mouse.down", self.stop_moving)
    
    def stop_moving(self):
        self.block.stop_animation(self.moving_animation)
        
Follow the Cursor
-----------------

Now we can combine what we know to make a cute game where the block chases the cursor.


In order for the Launcher to find your game, you must make the *game/*
directory be an importable python module by creating *game/__init__.py* (you can
read more about Python Packaging `here
<http://docs.python.org/tutorial/modules.html#packages>`_). The Launcher expects
this file to have a *main* function which pushes the first ``Scene`` for the
game on the ``Director``'s stack.

The Director and Scenes
-----------------------
The ``Director`` and ``Scenes`` are the most fundamental way to 
organize a game in Spyral. At any given time, a Scene is running and 
controlling the game. The Director manages movement between Scenes. The top
Scene on the stack is the current Scene, and 
transitions require:

* :func:`Pushing <spyral.director.push>` new Scenes on top of old ones.
* :func:`Popping <spyral.director.pop>`  the current Scene.
* :func:`Replacing <spyral.director.replace>`  the current Scene with a new one.

Your game will have many Scenes (perhaps representing a main menu, a character 
select screen, an individual level, or a pause menu), but there is only 
ever the one Director. 

Our Pong game will eventually have two Scenes: a simple menu, and the 
actual Pong game. For now, let's make an empty class to represent the 
second of those two Scenes. Then we can have the *main* function push 
that Scene onto the top of the Director's stack. To keep our code 
organized, we'll split this into multiple files. 



.. topic:: game/__init__.py

    .. literalinclude:: pong/1/__init__.py
        :linenos:

.. topic:: game/pong.py

    .. literalinclude:: pong/1/pong.py
        :linenos:

For now, we will only add in a stub for the Scene's constructor (`__init__ 
<http://interactivepython.org/runestone/static/thinkcspy/Classes/classes 
intro.html#user-defined-classes>`_). Notice how we call the constructor 
for the Pong classes parent (``spyral.Scene``) by using the ``super`` 
python keyword. Whenever you subclass in Python, you should call the 
super class in this way (`More information
<http://learnpythonthehardway.org/book/ex44.html>`_). Scenes require a size
on initialization, and all XO games should have the same size. 

.. note::

    If your monitor is not big enough to display a 1200x900 window, you can
    scale the resolution without affecting your game using the development
    launcher.
    
    >>> .\dev-launcher.py -r 600 450

.. topic:: game/pong.py

    .. literalinclude:: pong/2/pong.py
        :linenos:
        
Before we can set our first scene property, we have to learn about Images.

Images
------

Images in spyral are the basic building blocks of drawing. They are 
conceptually simple, but there are many methods to manipulate them. It 
is worthwhile to spend some time reading the docs on 
:func:`Images <spyral.Image>`. To make our background, we will

* create a new image using the Image constructor, sized to the Scene,
* assign it as the :func:`background <spyral.Scene.background>` for this Scene
* :func:`fill <spyral.Image.fill>` this image with black, and finally,


.. topic:: game/pong.py

    .. literalinclude:: pong/3/pong.py
        :linenos:
        :emphasize-lines: 11-13

Now that we have a background, we'll want to create Images that 
represent the paddles and ball in Pong. For this, we'll talk about 
Sprites. 

Sprites
-------
Sprites have an Image, along with some information about where and how to 
draw themselves. Sprites allow us to control things like positioning, scaling, 
rotation, and more. There are also more advanced Sprites, including ones 
that can do animation. For now, we'll work with basic sprites, but you 
can read more about the available sprites in :func:`Sprites <spyral.Sprite>`. 

All Sprites must have an image and live in a Scene. They cannot move 
between Scenes, and when a Scene ends, so do the sprites. As soon as 
Sprites are created, they will start being drawn by the scene (you can 
stop them from being drawn with the :func:`visible 
<spyral.Sprite.visible>` attribute).

For now, we'll 

* create a new Paddle sprite,
* give the Paddle a new image (a solid rectangle),
* create two instances of the Paddle sprites within the scene, and,
* position the sprites close to the left and right of the screen, using the
  sprite's anchor attribute to improve positioning,

.. topic:: game/pong.py

    .. literalinclude:: pong/4/pong.py
        :linenos:
        :emphasize-lines: 7-11, 21-28
        
A good rule of thumb is to avoid manipulating sprites at the Scene level. So
we'll refactor the positioning and anchors inside the Paddle constructor.

.. topic:: game/pong.py

    .. literalinclude:: pong/5/pong.py
        :linenos:
        :emphasize-lines: 13-18

Moving the Ball
------------------
Next, we'll add a ball, but we'll treat it differently than the paddles.
The ball is going to move on it's own, so we'll make a `Ball` 
class, inheriting from the `Sprite` class again. We already know how to 
position, set an image (using the :func:`draw_circle <spyral.Image.draw_circle>`
fuction), and anchor this new sprite. 


.. topic:: game/pong.py

    .. literalinclude:: pong/6/pong.py
        :linenos:
        :lines: 9-16
        
To make the ball move every frame, we'll need to register a function
of the ball with the `director.update` event. There are many possible 
events (see the :ref:`Event List <ref.events>` for a complete list), and you can even make
your own (as we will see later). The `director.update` event is the most
common, however. When a method is registered
with this event, the method will be called every update.

Additionally, we need to perform some math to calculate the velocity of the
ball. In order to reuse this function later, and to keep our code simpler,
we can move it to new method that we'll name `reset`.

.. topic:: game/pong.py

    .. literalinclude:: pong/7/pong.py
        :linenos:
        :lines: 9-41
        :emphasize-lines: 9-33
        
Collision Detection
-------------------

Next, we'd like to have our ball interact with the sides of the game 
board, and with the paddles. We'll do two different types of collision 
detection here just to showcase them. Which you use will depend largely 
on the game. 

First, we'll have the ball bounce off the top and bottom of the screen. 
For this, we'll do simple checks on the y coordinate of the ball. You 
may remember that we used a center anchor on the ball, so the 
coordinates are relative to the center of the ball. To remedy this, 
we'll use the Sprite attribute :func:`rect <spyral.Sprite.rect>`, which gives us a
rectangle that represents the drawn area of the sprite, and we can check
it's top and bottom attributes. When we see that they have passed the
ceiling or the floor, we'll flip the y component of the velocity. 

.. topic:: game/pong.py

    .. literalinclude:: pong/8/pong.py
        :linenos:
        :lines: 9-33
        
Next, we'll have the ball collide with the two paddles. We will place the
collision check at the Scene level, because it requires checking two Sprites.
Every `director.update`, we'll check to see if the ball is colliding with either
padel; if so, then we will call a method in the `Ball` class called `bounce`
that flips the horizontal velocity of the ball. It will check for collisions
using the 
:func:`collide_sprites <spyral.Scene.collide_sprites>` method of scenes.
Note that sprites also have a 
:func:`collide_sprite <spyral.Sprite.collide_sprite>`
method.

.. topic:: game/pong.py

    .. literalinclude:: pong/9/pong.py
        :linenos:
        :emphasize-lines: 54-55, 82-88
        
User Input
----------
User Input is handled the same way that `director.update` is - by registering
a function with the event. To get started, we'll register another event on the
scene: ``system.quit``, which is fired when the user presses the exit button.
Almost every game will want to respect this event.

.. topic:: game/pong.py

    .. literalinclude:: pong/10/pong.py
        :linenos:
        :lines: 111-123

A much more interesting event is ``input.keyboard.down.*``, which is fired
whenever the keyboard is pressed. You can also register on specific keys, e.g.,
``input.keyboard.down.left`` or ``input.keyboard.keyboard.down.f``. A complete
list of keys is available :ref:`ref.keys`.

The left and right paddles need to move differently depending on which side
they are on - the left paddle responds to `w` and `s`, and the right paddle
responds to `up` and `down`. Also, we want the paddles to keep moving after
the keys are released. We'll use a ``moving`` attribute to keep track of
whether the paddle should move either ``"up"`` or ``"down"``.

.. topic:: game/pong.py

    .. literalinclude:: pong/10/pong.py
        :linenos:
        :lines: 57-111
        :emphasize-lines: 63-111

User Events
-----------

New events can be queued and registered in spyral as easily as system events.
We'll :func:`queue <spyral.event.queue>` a new event ``pong.score`` when the
ball goes either on the left or right side of the screen. Notice that we
pass in a :func:`Event <spyral.Event>`, which we give a parameter named
``scorer``. Functions registered to this event can take in a ``scorer``
parameter to find out who scored.

We also register the ``reset`` method with this ``pong.score`` event on the
Paddles and Ball, so that they are reset when someone scores. Finally, we
register an ``increase_score`` method on the Scene, so that we can keep
track of the score of the game. Notice how we have created a new ``model``
dictionary outside of the Scene; this model can hold the global state, and be
saved and loaded more easily if we someday wanted to enable saving.

.. topic:: game/pong.py

    .. literalinclude:: pong/11/pong.py
        :linenos:
        :emphasize-lines: 9, 20, 34-37, 87, 135-138

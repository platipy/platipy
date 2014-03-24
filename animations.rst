Animations Tutorial
===================

Animations are a useful feature for making Sprites move and change.
They work by `interpolating <http://simple.wikipedia.org/wiki/Interpolation>`_ a property over time.
When you interpolate, you mathematically calculate changes from an initial value to a final value. 
As an example, here is a simple game where a sprite moves horizontally across the room using an Animation over the ``x`` attribute for 1.5 seconds.

.. topic:: game/animating.py

    .. literalinclude:: tutorials/animations/1/animations.py
        :linenos:
        :emphasize-lines: 16-17

.. note::
    
    If you have an animation running when the game starts, the first few frames might not be drawn as the program loads. That means your animation might already be in progress by the time you're able to see it. If you are bothered by this, have the animation triggered by a mouse or keyboard event.

We create an ``Animation`` object, and then we pass it into the :func:`animate <spyral.Sprite.animate>` method of a Sprite. 
We could very easily make the sprite move vertically simply by changing the attribute, which you'll notice is given as a ``str``.

.. code-block:: python

    animation = Animation('y', easing.Linear(0, HEIGHT), duration = 1.5)
    self.block.animate(animation)
    
A simplest animation requires:

* an attribute (e.g., ``x``, ``scale``, ``image``, or even one you choose yourself)
* an easing (discussed next)
* and a duration (e.g., 1.5 seconds)

Easings
-------

Remember back in Algebra, when you were given two points, and had to find a line that fit them?
And then in Algebra 2, you were taught that you could fit curves to multiple points.
This is similar to an ``Easing`` in Animations; a mathematical function over a given interval that Spyral will use in its calculations.
Easings are actually a very common term: to get an idea of the variety of easings, check out this page of `easings <http://easings.net/>`_.

Spyral natively supports a number of easings. For instance, the :func:`QuadraticIn <spyral.easing.QuadraticIn>` can be used to start slowly and then go faster.

.. code-block:: python

    animation = Animation('y', easing.QuadraticIn(0, HEIGHT), duration = 1.5)

The :func:`QuadraticOut <spyral.easing.QuadraticOut>` starts fast and then slows down:

.. code-block:: python

    animation = Animation('y', easing.QuadraticIn(0, HEIGHT), duration = 1.5)

Not all of the easings have an explicit ``start`` and ``end`` though; consider the :func:`Sine <spyral.easing.Sine>` easing, which takes in an amplitude instead. First the attribute will oscillate to the positive ``amplitude``, and then to the negative ``amplitude``. Notice that we also use a new parameter of the ``Animation`` named ``shift``, that sets the initial value of the attribute.

.. code-block:: python

    animation = Animation('x', easing.Sine(WIDTH/4), duration = 1.5, shift=WIDTH/2)
   

Attributes
----------

Animations can be used for more than just positions. For example, to stretch the Sprite horizontally:

.. code-block:: python

    animation = Animation('scale_x', easing.Linear(1.0, 2.0), duration = 1.5)
    
Of course, some attributes are not numbers, they are :func:`Vec2Ds <spyral.Vec2D>`: for instance, :func:`pos <spyral.Sprite.pos>`. Then you must use a Tuple easing Function.

.. code-block:: python

    animation = Animation('pos', easing.LinearTuple((0, 0) , (WIDTH, HEIGHT)), duration = 1.5)
    
And some attributes take on discrete values: :func:`visible <spyral.Sprite.visible>` takes on either ``True`` or ``False``, and :func:`image <spyral.Sprite.image>` could take on one of a list of images. For these animations, you can use the :func:`Iterate <spyral.easing.Iterate>` easing. This can be used to achieve blinking:

.. code-block:: python
    
    animation = Animation('visible', easing.Iterate([True, False]), duration = .5)
    
Or for running through a sequence of images:

.. code-block:: python
    
    filenames = ["walk0.png", "walk1.png", "walk2.png"]
    images = [spyral.Image(filename=f) for f in filenames]
    animation = Animation('visible', easing.Iterate(images), duration = 1.5)

You can even iterate over your own custom variable. If you had a happiness level for your sprite, you might make it fluctuate between -10 and 10 by:

.. code-block:: python

    animation = Animation('happiness', easing.Sine(10), duration = 16)

Animation Events
----------------

Sometimes you need to perform an action when an animation is completed or has started.
Fortunately, animations trigger their own :ref:`Animation Events <ref.events.animations>`:

.. topic:: game/animating.py

    .. literalinclude:: tutorials/animations/2/animations.py
        :linenos:
        :lines: 19-34
        :emphasize-lines: 7-8, 12-16
        
Notice that the naming schema is:

* <the name of the Sprite's class>.
* <the name of the attribute>.
* animation.
* <either ``start`` or ``end``>

A common pattern is to have a `Finite-State Machine <http://en.wikipedia.org/wiki/Finite-state_machine>`_ control the behavior of a Sprite in conjunction with animations. For instance, if you had a turret that charges up and then fires, you could control this behavior with an FSM.

.. topic:: game/animating.py

    .. literalinclude:: tutorials/animations/3/animations.py
        :linenos:

Notice how we test the ``sprite`` parameter to make sure that the given sprite is ``self`` - all Turrets fire the ``Turret.image.animation.end`` event, so we need to handle each individual turret separately. Also notice how we use a ``str`` to identify the state - this is good, pythonic practice.

Combining Animations
--------------------

You can combine two animations into a new one very easily.
For instance, to make one animation run after another, ``+`` them together:

.. code-block:: python

    first_animation = Animation('x', easing.Linear(0, WIDTH), duration = 1.5)
    second_animation = Animation('scale_x', easing.Linear(1.0, 2.0), duration = 1.5)
    animation = first_animation + second_animation

To make them run at the same time, in parallel, use the ``&``:

.. code-block:: python
    
    animation = first_animation & second_animation

A special kind of animation is the DelayAnimation, which let's you add delays.

.. code-block:: python

    half_second_delay = DelayAnimation(.5)
    move_x = Animation('x', easing.Linear(0, WIDTH), duration = 1)
    scale_x = Animation('scale_x', easing.Linear(1.0, 2.0), duration = 1.5)
    animation = (half_second_delay + move_x) & scale_x
    
Looping and Stopping animations
-------------------------------

Animations normally end after one iteration, but you can make them loop infinitely by setting an Animation's ``loop`` parameter to ``True``.
This is extremely useful for things like pointing arrows meant to grab users' attention.

.. code-block:: python

    animation = Animation('x', easing.Sine(WIDTH/4), duration = 1.5, shift=WIDTH/2, loop=True)

If you need to stop an animation, you can do it by passing in a specific animation to :func:`stop_animation <spyral.Sprite.stop_animation>`:

.. code-block:: python
        
    def __init__(self, scene):
        ...
        self.moving_animation = Animation('x', easing.Linear(0, 600), duration = 3.0)
        self.animate(self.moving_animation)
        spyral.register.event("input.mouse.down", self.stop_moving)
    
    def stop_moving(self):
        self.stop_animation(self.moving_animation)
        
Or you can stop all the animations with :func:`stop_all_animations <spyral.Sprite.stop_all_animations>` :

.. code-block:: python
    
    spyral.register.event("input.mouse.down", self.block.stop_all_animations)
        
Follow the Cursor
-----------------

Now we can combine what we know to make a cute game where the block chases the cursor.

.. topic:: game/animating.py

    .. literalinclude:: tutorials/animations/4/animations.py
        :linenos:
        :emphasize-lines: 23-28


Custom Easings
--------------

You can create your own Easings; more examples are given in the source code for the Easing module.

.. code-block:: python
    
    def MyEasing(start=0.0, finish=1.0):
        """
        Linearly increasing: f(x) = x
        """
            def my_easing(sprite, delta):
                return (finish - start) * (delta) + start
        return my_easing
        animation = Animation('x', MyEasing(0, WIDTH), duration = 1.5)

If you end up creating any Easings of your own (e.g., QuadraticInTuple), please share them!

Conclusion
----------

Animations cover a wide range of use cases, from movement to image changes, and beyond. 
But don't let the great power go to your head: some actions will always be slow on the XO laptops.
For instance, animating over the ``angle`` attribute.
Basically, you want to avoid dynamic drawing as much as possible.
As you use more animations, test your creation on the XO laptop directly to see how it performs.

If you want to see all the easings and animations in action, there is an `example <https://github.com/platipy/spyral/blob/master/examples/animations.py>`_ in the Spyral github.
Scenes and the Director
-----------------------
Scenes are the basic units that are executed by spyral for your game, and should be subclassed and filled in with code which is relevant to your game. The director, which is accessible at *spyral.director*, is a manager for Scenes, which maintains a stacks and actually executes the code.


.. autoclass:: spyral.Scene
    :members:
    
.. autoclass:: spyral.scene.Director
    :members:
    
.. _spyral_Image:

Images
------
.. autoclass:: spyral.Image
    :members:

.. _spyral_Sprites:

Sprites
-------
.. autoclass:: spyral.Sprite
    :members:
    
.. autoclass:: spyral.AggregateSprite
    :members:

.. _spyral_Groups:

Groups
------
.. autoclass:: spyral.Group
    :members:
        
Event Handling
--------------

.. _spyral_events:

Event Types
~~~~~~~~~~~

Events returned from the event handler are dicts which have a type and various attributes depending on the type. A table of the attributes that each event type has is as follows:

===============     ================
Event type          Other attributes
===============     ================
QUIT                type
ACTIVEEVENT         type, gain, state
KEYDOWN             type, unicode, key, mod, ascii
KEYUP               type, key, mod, ascii
MOUSEMOTION         type, pos, rel, buttons
MOUSEBUTTONUP       type, pos, button
MOUSEBUTTONDOWN     type, pos, button 
JOYAXISMOTION       type, joy, axis, value
JOYBALLMOTION       type, joy, ball, rel
JOYHATMOTION        type, joy, hat, value
JOYBUTTONUP         type, joy, button
JOYBUTTONDOWN       type, joy, button
VIDEORESIZE         type, size, w, h 
VIDEOEXPOSE         type, none 
USEREVENT           type, code
===============     ================

.. _spyral_keys:

spyral.keys
~~~~~~~~~~~

`spyral.keys` is an object which gives convenient to remember names for special keyboard events, like the arrow keys. (This module is a work-in-progress). The attributes of `spyral.keys` are.

=========    =========
Attribute    Usage
=========    =========
left         left arrow key
right        right arrow key
up           up arrow key
down         down arrow key
=========    =========

.. _spyral_Vec2D:

Vec2D
-----

.. autoclass:: spyral.Vec2D
    :members:
    
.. _spyral_Rect:
    
Rect
----

.. autoclass:: spyral.Rect
    :members:
    
.. _spyral_animation:

Animations
----------
TODO: Write a section on animations!

.. _spyral_layering:

Layers
------
TODO: Write a section on layers.

    
Appendix
--------

.. _anchors:

Anchor Positions
~~~~~~~~~~~~~~~~

Sprites, Images, and Rects all support anchor positions. In Sprites and Images, anchor positions are strings which will specify where drawing is relative to, or a 2-tuple which specifies just the offset. For rects, these anchor positions are attributes which can be checked or assigned to. The list of anchor positions is:

`topleft`, `topright`, `bottomleft`, `bottomright`, `center`, `midtop`, `midbottom`, `midleft`, `midright`

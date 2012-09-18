.. _spyral_Image:

Images
------
.. autoclass:: spyral.Image
    :members:
    
Scenes and the Director
-----------------------
.. autoclass:: spyral.Scene
    :members:
    
.. autoclass:: spyral.scene.Director
    :members:
    
.. _spyral_Sprites:

Sprites
-------
.. autoclass:: spyral.Sprite
    :members:
    
.. autoclass:: spyral.AnimationSprite
    :members:
    
.. _spyral_Groups:

Groups
------
.. autoclass:: spyral.Group
    :members:
    
.. autoclass:: spyral.AnimationGroup
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

Animations
----------

.. autoclass:: spyral.animations.Animation
    :members:
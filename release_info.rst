Latest Versions
===============

The latest version of Example.activity is v0.3.
The latest version of spyral is v0.9.

.. _downloads:

Downloads
---------

To update spyral to a newer version than the one included with your launcher, remove libraries/spyral and replace with the downloaded version.

* :download:`Download Pong.v2 <files/Pong-ea1.0-sp0.9.1.zip>` (includes spyral)
* :download:`Download Spyral.v0.9.1 <files/spyral-0.9.1.zip>`

Old Versions
~~~~~~~~~~~~
* `Download spyral v0.2 <https://github.com/rdeaton/spyral/zipball/v0.2>`_
* `Download spyral v0.1.1 <https://github.com/rdeaton/spyral/zipball/v0.1.1>`_
* `Download spyral v0.1 <https://github.com/rdeaton/spyral/zipball/v0.1>`_
* :download:`Download Example.activity v0.2 <files/releases/Example.activity_v0.2.tar.gz>` (Includes spyral v0.2)
* :download:`Download Example.activity v0.1 <files/releases/Example.activity_v0.1.tar.gz>` (Includes spyral v0.1)


Git Repositories
----------------

The repositories are hosted on github:

* `spyral <http://github.com/platipy/spyral>`_
* `Example.activity <http://github.com/platipy/Example.activity>`_

Changelogs
==========

Spyral
------

v0.2.1 - In Progress (Changes available in git)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
* [animation] Fix a logic bug in animations that would cause them to not catch an exception they should
* [camera] Fix a broken return value on camera.get_rect()
* [docs] Fix a documentation bug which used the wrong terminology
* [image] Fix image.get_size() to return a Vec2D instead of a 2-tuple
* [image] Fix image.draw_lines() not respecting the width parameter
* [image] Fix an issue where changes to images would not be rendered to the screen
* [image] Fix color channels being swapped on certain systems, in particular under scaling
* [rect] Fix a bug which didn't allow rects properly in the constructor to rects
* [rect] Fix a bug with rect.inflate and rect.inflate_ip which would cause a crash
* [sprite] Fix sprite.width and sprite.height
* [sprite] Fix sprite.visible not hiding sprites which were marked as static
* [sprite] Fix AggregateSprites only rendering some children
* [sprite] Fix AggregateSprites requiring a group be passed on their creation
* [sprite] Fix AggregateSprites not being able to have AggregateSprites as children
* [vector] Fix Vec2D's support for being tested inside containers based on hashes (i.e. sets)
* [vector] Fix Vec2D's support for being divided by a constant or another 2-tuple/Vec2D


New Features
++++++++++++
* Add spyral.Image.draw_arc()
* spyral is now compatible with pypi and available in the cheeseshop
* Add support for object-attribute access for built-in event types
* A new rendering backend which is easier to maintain
* :above and :below modifiers for layers
* Add a more complete spyral.event.keys object
* Add official support for LiveEventHandler and ReplayEventHandler, with documentation


v0.2 - 10/02/2012
~~~~~~~~~~~~~~~~~

Backwards Incompatible Changes
++++++++++++++++++++++++++++++
* spyral.Sprite and spyral.Group now must have dt passed in as their first argument. (This was in the examples anyways)
* Remove sprite.blend_flags, was broken anyways. May be back in future release

New Features
++++++++++++
* Add spyral.Vec2D, sprite.pos and sprite.scale are now Vec2D automatically
* Add spyral.Signal to spyral, as well as a number of useful signals in the docs
* Add draw_image, rotate, copy, scale, crop, flip to spyral.Image
* Add support for anchor-based positioning in spyral.Image methods
* Add sprite.scale, sprite.scale_x, sprite.scale_y, and sprite.angle, with animation support
* Add sprite.flip_x and sprite.flip_y
* Animations no longer require AnimationSprite or AnimationGroup objects, they work on standard sprites and groups
* Add spyral.Font
* Add AggregateSprite

Bug Fixes
+++++++++
* Fix VIDEORESIZE events crashing spyral
* Fix a bug with parallel animations not evaluating their ending condition
* Fix a bug with group.empty calling remove on sprites
* Fix a bug where sprites were being set static even when they weren't
* Fix a bug where static sprites were redrawn without clearing behind them
* Fix a frame count bug in the Iteration animator, making it more smooth
* Fix the import system, allowing the import of spyral's submodules again
* Fix a bug in rect.move_ip, previously the offsets would become the new coordinates
* Fix a limitation on the number of layers which a game could have

Miscellaneous
+++++++++++++
* Remove the legacy spyral.util module
* Remove spyral/docs in favor of documentation in platipy
* Remove sprite.blend_flags, was broken anyways. May be back in future release
* Remove the antiquated and broken examples/pong.py
* Major revisions to built-in documentation.


v0.1.1 - 09/19/2012
~~~~~~~~~~~~~~~~~~~
* Fix group.remove() to ensure sprites are no longer drawn upon removal
* Fix rect.collide_rect(), results were previously inverted.

v0.1 - 09/18/2012
~~~~~~~~~~~~~~~~~
* First release

Example.activity
----------------

v0.2 - 10/02/2012
~~~~~~~~~~~~~~~~~
* Fix generation of PNGs for profiling paths with spaces in them
* Fix activity.py launcher loading games before the directory was initialized
* Bump spyral to v0.2

v0.1 - 09/18/2012
~~~~~~~~~~~~~~~~~
* First release


Contact Developers / Submit Changes
===================================

If there is a bug in spyral or Example.activity, you can e-mail rdeaton@udel.edu to notify me directly, submit a ticket on github, or send a pull request.

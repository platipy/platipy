Pygame and Spyral
=================

Pygame Primer
-------------

Spyral
------


Spyral Classes
~~~~~~~~~~~~~~

The five most important classes in Spyral are Director, Camera, Scene, Sprite, and Group.
  * **Director** - There is exactly one Director in a Spyral game. In a typical game, it is initialized at the beginning and then it's only use is to transition between scenes. The most important functions for you to understand are ''pop'', ''push'', and ''replace''.
  * **Camera** - Every Spyral game has at least one "top-level" camera that is automatically created with the Director. Cameras handle the layers and scaling functionality. You can have "child cameras" on screen in order to make, for example, a zoomed-in view or a zoomed-out view (such as a mini-map), since anything outside of the specified "virtual size" will be clipped.
  * **Sprite** - A Spyral Sprite is a basic game object. Its two most important properties are its image and position. If you have something on the screen, it's almost definitely a Sprite. Most non-trivial Sprites will override two important functions: __init__ (where the Sprite is initialized) and update (where the Sprite is given game logic). You'll often have a function named "render" that redraws the image, which will automatically trigger it to be redrawn.
  * **Group** - In order for Sprites to exist, they must belong to one or more group. When an instance of a Sprite has been removed from all the groups, it is removed from your game. You can use Groups to logically organize different kinds of Sprites such as enemies, user interface objects, and obstacles. Think of a Group as a List of Sprite instances.
  * **Scene** - Scenes are "rooms" for your Sprites (or rather, for your Groups, and the Groups contain the Sprites). You'll usually use them to move between different menus and levels of your game. Scenes are Stack-based: new scenes can be pushed onto old ones and then popped off later, restoring the original scene (this greatly simplifies the creation of pause menus!).

Spyral Start-up
~~~~~~~~~~~~~~~
  * Director initializes Pygame
  * Director creates the Root camera
  * Your first Scene is created, Groups and Sprites are added to it
  * Your first Scene is pushed onto the Director's Stack

Images in Pygame and Spyral
~~~~~~~~~~~~~~~~~~~~~~~~~~~
==== Images in Pygame and Spyral ====
There are a few terms in Pygame that confuse people at first: ** Surface == Image ** and ** Image != Sprite **. When you load an image in Spyral using ''spyral.util.load_image'' or ''spyral.util.Spritesheet'', these functions return a ** SURFACE **. And when you have a spyral Sprite, there is a property (variable) named ''image'' that can be set to a surface in order to give the Sprite a picture. Do not get these confused. 

Another important thing to remember is that images can only be loaded after Pygame has been initialized.
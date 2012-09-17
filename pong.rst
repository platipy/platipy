Your First Game: Pong
=====================

Setting up the launcher template
--------------------------------
Covers downloading the launcher, initializing a new activity with it, and using the dev_launcher (renamed from test_launcher).

Scenes and the director
-----------------------
Covers what a scene does, the update and render loops. We'll have them set up templates for two different Scenes here, one for an introduction screen and one for the game. For now, we'll have the first scene they enter be the game, and we'll talk more about Scenes and the director later.

Sprites and Groups
------------------
We'll have them load images for the ball and the paddle (they'll be provided. We won't have them generate them with pygame.draw commands. We'll probably try to avoid using them at all in this tutorial) and make them into sprites set at different positions on the screen. 

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
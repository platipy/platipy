Spyral by Example
=================

This chapter is a tutorial-style introduction to spyral, pygame, and some of the utilities provided for building games for the XO. In this tutorial, we will be creating a simple game. The first stage of every project should be to discuss and plan the features of our game.

The game we are going to create is inspired by a game created in a previous semester of the course, `Math Adder <http://todo/>`_. The Math Adder is a game based on the classic game snake, where the objective is to create expressions which evaluate to a certain number. We are going to create a similar game, but focused instead on spelling and vocabulary.

The Game Specification
~~~~~~~~~~~~~~~~~~~~~~

Game Modes
----------
* Practice Mode - flashes the word on screen, and then asks you to spell the word (showing the definition at the bottom still)
* Quiz Mode - shows only the definition at the bottom, and asks you to spell the word
* Marathon Mode - Goes through the list of words multiple times, getting progressively more difficult (see game difficulties below)
* Learning Mode - need a simple way to introduce students to the new lists of words. I have a few ideas for this that will come later. Perhaps Marathon mode, starting as practice as the first round, then going Quiz Easy, Quiz Medium, Quiz Hard would be a suitable option? This needs more consideration.

Game Difficulty
---------------
* Easy - Along with the definition, shows the first (and perhaps last) letter of each word. The only collectable letters are a part of the word
* Medium - Shows only the definition, and the only collectible letters are part of the word
* Hard - Shows only the definition, and the board contains duplicate letters which are in the word, and other letters which may not be in the word
* Expert - The hard difficulty, but the snake is continuously in motion. In Marathon mode, if the player completes the expert difficulty, the snake can move progressively faster.

In Game Mechanics
-----------------
* You start the game with 3 lives, and you have a certain number of words you must solve
* Arrow keys move the snake around the board. Letters will be on top of apples, and they will be added to the end of the snake when you move on to the apple.
* Once your attempt at spelling the word is completed, press a key (We have 4) will lock the guess in. An incorrect guess loses a life (egg), shows clearly that you were incorrect, and moves you to a new word. A correct guess gives you bonus points and moves you to a new word.
* Running into the wall or back into the snake causes you to lose a life and brings up a new word.
* (Good idea?) A mistake key can exist which causes you to lose 1/2 or 1/4 of a life if you've realized you've eaten the wrong apple. Each press of the button will return the last letter you ate back to the board.
* A hint key will hilight the next letter in the word (assuming you're correct so far, not sure what to do if the spelling is wrong so far). Hints can either subtract a 1/2 or 1/4 life, like the mistake key, or there can be a small fixed number of hints per game, with a score bonus at the end for each hint remaining.

Scoring
-------
* Points are awarded for the successful spelling of any word.
* Bonus multipler awarded for successful spelling of more than one word in a row.
* End of game bonuses for:
    * Lives remaining
    * Hints (?) remaining (If they don't cost lives)
    * Perfect round (no hints or lives used)
* In game scores should translate into an out of game gold system

Achievements
------------
* Completing an achievement should notify you of completion (XBLA-style)
* There should be an achievements page which shows all the achievements you can unlock, with a summary of them
* Achievements should give out of game gold, more for more difficulty achievements
* Example achievements include
    * Completing a round of easy, medium, hard, etc.
    * Perfect rounds of easy, medium, hard, etc.
    * Making it to certain rounds of marathon mode
    
Unlockables
-----------
* Using the out of game gold system, the user should be able to unlock upgrades to the game
* Upgrades include different backgrounds, snake styles, apple styles, etc.

Usability
---------
* It is important that the game have a consistent interface and controls
* Controls should be obvious and unambiguous at all times


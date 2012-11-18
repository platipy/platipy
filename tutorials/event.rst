Event Driven Game Development
=============================

.. note::
    
    This tutorial is under construction, and may have minor mistakes and errors. Read carefully.
    
In this tutorial, we're going to look at some new features in spyral that can help us to structure and organize games in a standard and maintainable way. While what we will investigate isn't the only way to develop games, it is recommended that you understand the concepts and determine how useful they will be to your game.

Spyral has two main classes that are used for handling events in games. The first is one that you should already be familiar with, the EventHandler. It is what you have likely come to rely on as being `self.event_handler` in your scene. This event handler is, in reality, not so much of an event handler as it is a way of receiving input from the operating system. It has a few methods for getting events and filtering the events that you receive, but the facilities are really minimal, and are useful only for simple games.

Once we start developing more complicated games, we need a way to better organize and deal with events from the operating system, but we'll also want to trigger and respond to custom events created by our game, or by other modules which we integrate (see: the forthcoming `Form` class). This is where the `EventManager` comes in, but let's first talk about what it means to develop an event driven game.

Let's take a look at the game of Pong we wrote during our introductory tutorial. Even in this simple game, we've had to make some design decisions which should, from a software engineering standpoint, make us cringe on some level. For instance, the Ball sprite had to be passed a reference to our scene, so that it could call a score method on the scene, so that the scene would be able to reset the ball and paddles and display a score.

Lucky for us, this isn't the end of the world, but what happens when we start with more complicated games, where certain conditions, like a score, trigger something that requires that a lot of other objects take some action. Do we just keep adding methods to the scene class for each case, and having each and every object which may need to trigger these actions keep a reference to scene lying around internally? What happens when one of these actions triggers another one, and another, and suddenly our stack trace has grown beyond control.

Hopefully you can imagine that this very quickly leads to coupling between all the game objects which is far too strong, and can lead to large stack traces and difficult to track down bugs, and a Scene class with a huge amount of methods that need to be maintained.

So how can we deal with some of these issues? Event driven programming. The basic premise is that our game will have one `EventManager`, to which we will send events. When we first initialize our scene, we will add *listeners* to the manager, which will be triggered when events that they are interested in happen. Any object which has a method called `handle_event` is a *listener*.

What this design pattern should allow us to do, is follow a simple goal: Each object in our game should need to know about as few other objects in the game as possible. What follows is what happens when we apply this concept to our pong game, and rewrite it from a more event-driven perspective.

.. topic:: pong.py

    .. literalinclude:: resources/event/pong.py
        :linenos:

In this version of pong, we were able to decouple things considerably. While it's hard to see the full benefits from a small example, event driven programming where we follow simple constraints will overall result in more maintainable and extensible code. The fact that we no longer have a monolithic event handling loop that needed to understand some of the working details of any object it may be handling input for is already a great sign.

One way that we could make this program, and all of our games, even more extensible is to abstract the input handling away from in game actions. For a number of games, we may create a special listener which we can call a mapper, which handles all the input from the operating system, and sends higher level events which are more relevant to our game. The `Form` class is an example of such a mapper.

Some guidelines we should all follow when working towards event driven programming:

* Separation is king. Each object should only need to know minimal amounts and keep references to minimal numbers of other objects. Any information that the sprite needs in order to react to an event it should have already, or that information should be included as an attribute of the event.

* Document events. Because events are strings, and they may have any attributes that are necessary for their purpose, it is important that our design documents list all the events that our game creates and deals with for reference.

* To be continued
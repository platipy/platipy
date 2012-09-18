import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900

class Ball(spyral.Sprite):
    def __init__(self, scene):
        super(Ball, self).__init__()
        # We take the scene as an argument so that we can have the ball
        # Tell the screen when the ball has hit an edge, so that a new
        # ball can be created.
        self.scene = scene
        
        self.image = spyral.Image(size=(20, 20))
        self.image.draw_circle((255, 255, 255), (10, 10), 10)
        
        # We'll start by picking a random angle for the ball to move
        # We repick the direction if it isn't headed for the left
        # or the right hand side
        theta = random.random()*2*math.pi
        while ((theta > math.pi/4 and theta < 3*math.pi/4) or
               (theta > 5*math.pi/4 and theta < 7*math.pi/4)):
            theta = random.random()*2*math.pi
        # In addition to an angle, we need a velocity. Let's have the
        # ball move at 300 pixels per second
        r = 300
        
        self.vel_x = r * math.cos(theta)
        self.vel_y = r * math.sin(theta)
        
        # We'll use the center of the ball for the anchor
        self.anchor = 'center'
        # We'll start the ball at the center. self.pos is actually the
        # Same as accessing sprite.x and sprite.y individually
        self.pos = (WIDTH/2, HEIGHT/2)
                
    def update(self, dt):
        self.x += dt * self.vel_x
        self.y += dt * self.vel_y
        
        # We use the rect for checking collisions
        # This saves having to take into account the anchor and the
        # size of sprite, as it is accounted for in the rect.
        r = self.get_rect()
        if r.top < 0:
            # We'll change this rect a bit, and use it to set the x and y coordinates again
            r.top = 0
            self.vel_y = -self.vel_y
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
            self.vel_y = -self.vel_y
        
        self.pos = r.center # We reset the pos using the cnter of the rect, since we are anchored
        
        # We'll also check the sides, and we'll call the scene's score function with the side
        # that was scored on
        if r.left < 0:
            self.scene.score('left')
        if r.right > WIDTH:
            self.scene.score('right')
            
    def collide_paddle(self, paddle):
        if self.get_rect().collide_rect(paddle.get_rect()):
            self.vel_x = -self.vel_x
        

class Pong(spyral.Scene):
    def __init__(self, *args, **kwargs):
        super(Pong, self).__init__(*args, **kwargs)
        
        self.camera = self.parent_camera.make_child(virtual_size = (WIDTH, HEIGHT))
        
        paddle_image = spyral.Image(size=(20, 300))
        paddle_image.fill((255, 255, 255))
        
        # We want to make sure we keep the paddles around, since we'll
        # work with them for motion and collision detection
        self.left_paddle = spyral.Sprite()
        self.left_paddle.image = paddle_image
        # This anchor means that the x and y coordinates we assign are
        # relative to the middle left of the image.
        self.left_paddle.anchor = 'midleft'
        # We'll keep the paddle just slightly off of the wall
        self.left_paddle.x = 20
        # We'll have the paddle start out vertically centered
        self.left_paddle.y = HEIGHT/2
        
        self.right_paddle = spyral.Sprite()
        self.right_paddle.image = paddle_image
        self.right_paddle.anchor = 'midright'
        self.right_paddle.x = WIDTH - 20
        self.right_paddle.y = HEIGHT/2
        
        self.ball = Ball(self)
        
        # We have to give our camera to the group so it knows where to draw
        self.group = spyral.Group(self.camera)
        # We can add the sprites to the group
        self.group.add(self.left_paddle, self.right_paddle, self.ball)
        
        # We should track whether the paddles are moving up and down
        self.left_paddle.moving = False
        self.right_paddle.moving = False
        
    def score(self, side):
        pass    
        
    def on_enter(self):
        background = spyral.Image(size=(WIDTH,HEIGHT))
        background.fill((0,0,0))
        self.camera.set_background(background)
        
    def render(self):
        # Simply tell the group to draw
        self.group.draw()
        
    def update(self, dt):
        """
        The update loop receives dt as a parameter, which is the amount
        of time which has passed since the last time update was called.
        """
        self.group.update(dt)
        
        # Gets all the events from the event handler
        for event in self.event_handler.get():
            # You should always be sure you're handling the quit events
            if event['type'] == 'QUIT':
                spyral.director.pop()  # Happens when someone asks the OS to close the program
                return
            if event['type'] == 'KEYDOWN':
                # On keydown, we store the direction the paddle should be moving
                # We reset this on keyup, so that holding down the buttons works
                if event['ascii'] == 'w':
                    self.left_paddle.moving = 'up'
                if event['ascii'] == 's':
                    self.left_paddle.moving = 'down'
                if event['key'] == spyral.keys.up:
                    self.right_paddle.moving = 'up'
                if event['key'] == spyral.keys.down:
                    self.right_paddle.moving = 'down'
            elif event['type'] == 'KEYUP':
                if event['ascii'] in ('w', 's'):
                    self.left_paddle.moving = False
                if event['key'] in (spyral.keys.up, spyral.keys.down):
                    self.right_paddle.moving = False
        
        paddle_velocity = 250
        
        # Since we don't want to repeat code for the left and the right
        # paddles, which should behave the same, we make a function
        def move_and_correct(paddle):
            # Move the paddle if it should be moving
            if paddle.moving == 'up':
                paddle.y -= paddle_velocity * dt
            elif paddle.moving == 'down':
                paddle.y += paddle_velocity * dt
                
            # We'll do some collision detection with the top and bottom
            # Just like we did for the ball
            r = paddle.get_rect()
            if r.top < 0:
                r.top = 0
            if r.bottom > HEIGHT:
                r.bottom = HEIGHT
            
            # We set the position based on the rect, but we use each sprite's
            # anchor for setting the coordinates since they are different
            paddle.pos == getattr(r, paddle.anchor)
        
        move_and_correct(self.left_paddle)
        move_and_correct(self.right_paddle)
        
        
        self.ball.collide_paddle(self.left_paddle)
        self.ball.collide_paddle(self.right_paddle)
        
        
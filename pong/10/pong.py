import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)

class Ball(spyral.Sprite):
    def __init__(self, scene):
        super(Ball, self).__init__(scene)
        
        self.image = spyral.Image(size=(20, 20))
        self.image.draw_circle((255, 255, 255), (10, 10), 10)
        self.anchor = 'center'
        
        spyral.event.register('director.update', self.update)
        self.reset()
        
    def update(self, delta):
        self.x += delta * self.vel_x
        self.y += delta * self.vel_y
        
        r = self.rect
        if r.top < 0:
            r.top = 0
            self.vel_y = -self.vel_y
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
            self.vel_y = -self.vel_y
        
    def reset(self):
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

        # We'll start the ball at the center. self.pos is actually the
        # same as accessing sprite.x and sprite.y individually
        self.pos = (WIDTH/2, HEIGHT/2)
    
    def bounce(self):
        self.vel_x = -self.vel_x

class Paddle(spyral.Sprite):
    def __init__(self, scene, side):
        super(Paddle, self).__init__(scene)
        
        self.image = spyral.Image(size=(20, 300)).fill((255, 255, 255))
        
        self.anchor = 'mid' + side
        
        self.side = side
        self.moving = False
        self.reset()
        
        if self.side == 'left':
            spyral.event.register("input.keyboard.down.w", self.move_up)
            spyral.event.register("input.keyboard.down.s", self.move_down)
            spyral.event.register("input.keyboard.up.w", self.stop_move)
            spyral.event.register("input.keyboard.up.s", self.stop_move)
        else:
            spyral.event.register("input.keyboard.down.up", self.move_up)
            spyral.event.register("input.keyboard.down.down", self.move_down)
            spyral.event.register("input.keyboard.up.up", self.stop_move)
            spyral.event.register("input.keyboard.up.down", self.stop_move)
        spyral.event.register("director.update", self.update)
    
    def move_up(self):
        self.moving = 'up'
        
    def move_down(self):
        self.moving = 'down'
        
    def stop_move(self):
        self.moving = False
        
    def reset(self):
        if self.side == 'left':
            self.x = 20
        else:
            self.x = WIDTH - 20
        self.y = HEIGHT/2
        
    def update(self, dt):
        paddle_velocity = 250
        
        if self.moving == 'up':
            self.y -= paddle_velocity * dt
            
        elif self.moving == 'down':
            self.y += paddle_velocity * dt
                
        r = self.get_rect()
        if r.top < 0:
            r.top = 0
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
        self.pos = r.center


class Pong(spyral.Scene):
    def __init__(self):
        super(Pong, self).__init__(SIZE)
        
        self.background = spyral.Image(size=SIZE).fill( (0, 0, 0) )

        self.left_paddle = Paddle(self, 'left')
        self.right_paddle = Paddle(self, 'right')
        self.ball = Ball(self)

        spyral.event.register("director.update", self.update)
        spyral.event.register("system.quit", spyral.director.pop)
    
    def update(self, delta):
        if (self.collide_sprites(self.ball, self.left_paddle) or
            self.collide_sprites(self.ball, self.right_paddle)):
            self.ball.bounce()

import spyral
import random
import math

WIDTH = 1200
HEIGHT = 900

# To keep things simple, for this example our manager will be a global
# inside our module. For larger games, we might put it, along with
# other resources that need to be shared amongst all of the code
# inside a module which is designed specifically for that data
manager = None

class Ball(spyral.Sprite):
    def __init__(self):
        super(Ball, self).__init__()
        self.image = spyral.Image(size=(20, 20))
        self.image.draw_circle((255, 255, 255), (10, 10), 10)
        
        self._reset()
        
    def handle_event(self, event):
        if event.type == 'pong_score':
            self._reset()
        
    def _reset(self):
        theta = random.random()*2*math.pi
        while ((theta > math.pi/4 and theta < 3*math.pi/4) or
               (theta > 5*math.pi/4 and theta < 7*math.pi/4)):
            theta = random.random()*2*math.pi
        r = 300
        
        self.vel_x = r * math.cos(theta)
        self.vel_y = r * math.sin(theta)
        self.anchor = 'center'
        self.pos = (WIDTH/2, HEIGHT/2)
                
    def update(self, dt):
        self.x += dt * self.vel_x
        self.y += dt * self.vel_y
        
        r = self.get_rect()
        if r.top < 0:
            r.top = 0
            self.vel_y = -self.vel_y
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
            self.vel_y = -self.vel_y
        
        self.pos = r.center
        
        if r.left < 0:
            e = spyral.Event('pong_score')
            e.side = 'left'
            manager.send_event(e)
        if r.right > WIDTH:
            e = spyral.Event('pong_score')
            e.side = 'right'
            manager.send_event(e)
            
    def collide_paddle(self, paddle):
        if self.get_rect().collide_rect(paddle.get_rect()):
            self.vel_x = -self.vel_x

class Paddle(spyral.Sprite):
    def __init__(self, side):
        spyral.Sprite.__init__(self)
        self.image = spyral.Image(size=(20, 300))
        self.image.fill((255, 255, 255))
        if side == 'left':
            self.anchor = 'midleft'
            self.x = 20
        else:
            self.anchor = 'midright'
            self.x = WIDTH - 20
        self.y = HEIGHT/2
        self.side = side
        self.moving = False
        
    def _reset(self):
        self.y = HEIGHT/2
        
    def handle_event(self, event):
        up = ord('w') if self.side == 'left' else spyral.keys.up
        down = ord('s') if self.side == 'left' else spyral.keys.down
        if event.type == 'KEYDOWN':
            if event.key == up:
                self.moving = 'up'
            if event.key == down:
                self.moving = 'down'
        if event.type == 'KEYUP':
            if event.key in (up, down):
                self.moving = False
        if event.type == 'pong_score':
            self._reset()

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
            
        self.pos == getattr(r, self.anchor)


class Pong(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        super(Pong, self).__init__(*args, **kwargs)
        
        self.camera = self.parent_camera.make_child(virtual_size = (WIDTH, HEIGHT))
        self.group = spyral.Group(self.camera)
        
        self.ball = Ball()
        self.left_paddle = Paddle('left')
        self.right_paddle = Paddle('right')
        
        self.group.add(self.left_paddle, self.right_paddle, self.ball)
        
        manager = spyral.EventManager()
        manager.register_listener(self, ['KEYDOWN', 'QUIT'])
        manager.register_listener(self.left_paddle, ['KEYDOWN', 'KEYUP', 'pong_score'])
        manager.register_listener(self.right_paddle, ['KEYDOWN', 'KEYUP', 'pong_score'])
        manager.register_listener(self.ball, ['pong_score'])
        
    def handle_event(self, event):
        # Our scene will be a listener that just watches for anything
        # Which should tell us to quit the game
        if event.type == 'QUIT' or (event.type == 'KEYDOWN' and event.ascii == 'q'):
            spyral.director.pop()
                
    def on_enter(self):
        background = spyral.Image(size=(WIDTH,HEIGHT))
        background.fill((0,0,0))
        self.camera.set_background(background)
        
    def render(self):
        self.group.draw()
        
    def update(self, dt):
        manager.send_events(self.event_handler.get())        
        self.group.update(dt)
        
        self.ball.collide_paddle(self.left_paddle)
        self.ball.collide_paddle(self.right_paddle)
    
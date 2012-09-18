import spyral

WIDTH = 1200
HEIGHT = 900

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
        
        # We have to give our camera to the group so it knows where to draw
        self.group = spyral.Group(self.camera)
        # We can add the sprites to the group
        self.group.add(self.left_paddle, self.right_paddle)
        
        
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
        pass
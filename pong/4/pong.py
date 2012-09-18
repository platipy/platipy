import spyral


class Pong(spyral.Scene):
    def __init__(self, *args, **kwargs):
        super(Pong, self).__init__(*args, **kwargs)
        
        self.camera = self.parent_camera.make_child(virtual_size = (1200,900))
        
    def on_enter(self):
        background = spyral.Image(size=(1200,900))
        background.fill((0,0,0))
        self.camera.set_background(background)
        
    def render(self):
        pass
        
    def update(self, dt):
        """
        The update loop receives dt as a parameter, which is the amount
        of time which has passed since the last time update was called.
        """
        pass
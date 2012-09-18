import spyral


class Pong(spyral.Scene):
    def __init__(self, *args, **kwargs):
        super(Pong, self).__init__(*args, **kwargs)
        
    def on_enter(self):
        pass
        
    def render(self):
        pass
        
    def update(self, dt):
        """
        The update loop receives dt as a parameter, which is the amount
        of time which has passed since the last time update was called.
        """
        pass
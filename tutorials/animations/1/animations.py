import spyral
import sys
from spyral import Animation, easing

WIDTH = 1200
HEIGHT = 900
SIZE = (WIDTH, HEIGHT)

class Game(spyral.Scene):
    def __init__(self):
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE).fill((0,0,0))
        
        self.block = spyral.Sprite(self)
        self.block.image = spyral.Image(size=(64, 64)).fill((255, 0, 0))
        self.block.anchor = 'center'
        self.block.y = HEIGHT / 2
        
        spyral.event.register("system.quit", sys.exit)
        
        animation = Animation('pos', easing.LinearTuple(self.block.pos, pos), duration = 1.0)
        self.block.animate(animation)

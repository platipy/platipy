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
        
        spyral.event.register("input.mouse.motion", self.animate)
        
    def animate(self, pos):
        # Move horizontally from one side of the screen to other over 1 second
        #animation = Animation('x', easing.Linear(0, WIDTH), duration = 1.0)
        self.block.stop_all_animations()
        
        self.block.animate(animation)
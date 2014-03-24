class Turret(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(64, 64)).fill((255, 0, 0))
        self.anchor = 'center'
        self.pos = (WIDTH/2, HEIGHT/2)
        self.load_images()
        
        self.charging_ani = Animation('image', easing.Iterate(self.charging_images), 4)
        self.firing_ani = Animation('image', easing.Iterate(self.firing_images), 2)
        self.charge()
        spyral.register('Turret.image.animation.end', self.update_state)
    
    def update_state(self, sprite):
        if sprite == self:
            # If you have more states, using a dictionary would be more elegant
            # e.g., self.state_functions[self.state]()
            if self.state == 'charging':
                self.fire()
            elif self.state == 'firing':
                self.charge()
                
    def fire(self):
        self.state = 'firing'
        self.animate(self.firing_ani)
    
    def charge(self):
        self.state = 'charging'
        self.animate(self.charging_ani)
        
    def load_images(self):
        self.charging_images = [] #Images go here
        self.firing_images = [] #Images go here
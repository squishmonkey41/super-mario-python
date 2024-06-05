from copy import copy
from classes.Animation import Animation
from entities.EntityBase import EntityBase
from entities.Item import Item


class PiranhaPlant(EntityBase):
    def __init__(self, screen, spriteCollection, x, y, sound, dashboard, gravity=0):
        super(PiranhaPlant, self).__init__(x, y, gravity)
        self.screen = screen
        self.spriteCollection = spriteCollection
        self.animation = Animation(
            [
                self.spriteCollection.get("piranhaClosed").image,
                self.spriteCollection.get("piranhaOpen").image,
            ],
            self.spriteCollection.get("piranhaOpen").image,
            self.spriteCollection.get("piranhaOpen").image,
            14
        )
        self.type = "Mob"
        self.triggered = False
        self.time = 0
        self.maxTime = 10
        self.sound = sound
        self.dashboard = dashboard
        self.vel = 1
        self.item = Item(spriteCollection, screen, self.rect.x, self.rect.y)


    def update(self, cam):
        self.screen.blit(self.animation.image, (self.rect.x + cam.x, self.rect.y))
        self.animation.update()

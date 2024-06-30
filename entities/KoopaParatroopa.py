import pygame

from classes.Animation import Animation
from classes.Collider import Collider
from classes.EntityCollider import EntityCollider
from classes.Maths import Vec2D
from entities.EntityBase import EntityBase
from traits.leftrightwalk import LeftRightWalkTrait
from entities.Koopa import Koopa
from traits.LeftRightConstrained import LeftRightConstrainedTrait

class KoopaParatroopa(Koopa):
    def __init__(self, screen, spriteColl, xMin, xMax, y, level, sound):
        super(Koopa, self).__init__(y - 1, xMin, 1.25)
        self.spriteCollection = spriteColl
        self.animation = Animation(
            [
                self.spriteCollection.get("koopa-flying-1").image,
                self.spriteCollection.get("koopa-flying-2").image,
                self.spriteCollection.get("koopa-flying-3").image,
                self.spriteCollection.get("koopa-flying-4").image,
            ]
        )
        self.screen = screen
        self.leftrightTrait = LeftRightWalkTrait(self, level)
        self.timer = 0
        self.timeAfterDeath = 35
        self.type = "Mob"
        self.dashboard = level.dashboard
        self.collision = Collider(self, level)
        self.EntityCollider = EntityCollider(self)
        self.levelObj = level
        self.sound = sound
        self.obeyGravity = False
        self.demotingFrames = 0
        self.traits = {
            "LeftRightConstrainedTrait": LeftRightConstrainedTrait(xMin, xMax)
        }

    def update(self, camera):
        if self.alive and self.active:
            self.updateAlive(camera)
            self.checkEntityCollision()
        elif self.alive and not self.active and not self.bouncing:
            self.sleepingInShell(camera)
            self.checkEntityCollision()
        elif self.bouncing:
            self.shellBouncing(camera)

    def demoteToKoopa(self, camera):
        self.obeyGravity = True
        if self.timer < self.timeAfterDeath:
            animation = self.animation = Animation(
                [
                    self.spriteCollection.get("koopa-1").image,
                    self.spriteCollection.get("koopa-2").image,
                ]
            )
            self.screen.blit(
                animation.image,
                (self.rect.x + camera.x, self.rect.y - 32),
            )
        self.applyGravity()
        self.demotingFrames = 60
        self.traits["LeftRightConstrainedTrait"].reset()

    def isFlying(self):
        return self.obeyGravity == False

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import pyganim
import  os

__author__ = 'kran'


MOVE_SPEED = 7
WIDTH = 22
HEIGHT = 32
COLOR = "#888888"

JUMP_POWER = 10
GRAVITY = 0.25

ANIMATION_DELAY = 0.1
ICON_DIR = os.path.dirname(__file__)

ANIMATION_RIGHT = [
    ('%s/mario/r1.png' % ICON_DIR),
    ('%s/mario/r2.png' % ICON_DIR),
    ('%s/mario/r3.png' % ICON_DIR),
    ('%s/mario/r4.png' % ICON_DIR),
    ('%s/mario/r5.png' % ICON_DIR),
]
ANIMATION_LEFT = [
    ('%s/mario/l1.png' % ICON_DIR),
    ('%s/mario/l2.png' % ICON_DIR),
    ('%s/mario/l3.png' % ICON_DIR),
    ('%s/mario/l4.png' % ICON_DIR),
    ('%s/mario/l5.png' % ICON_DIR),
]
ANIMATION_JUMP_RIGHT = [('%s/mario/jr.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP_LEFT = [('%s/mario/jl.png' % ICON_DIR, 0.1)]
ANIMATION_JUMP = [('%s/mario/j.png' % ICON_DIR, 0.1)]
ANIMATION_STAY = [('%s/mario/0.png' % ICON_DIR, 0.1)]


class Player(sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()
        self.xvel = 0
        self.startX = x
        self.startY = y
        self.yvel = 0
        self.onGround = False
        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, WIDTH, HEIGHT)
        self.image.set_colorkey(Color(COLOR))

        animation = []
        for e in ANIMATION_RIGHT:
            animation.append((e, ANIMATION_DELAY))
        self.animation_right = pyganim.PygAnimation(animation)
        self.animation_right.play()

        animation2 = []
        for j in ANIMATION_LEFT:
            animation2.append((j, ANIMATION_DELAY))
        self.animation_left = pyganim.PygAnimation(animation2)
        self.animation_left.play()

        self.animation_stay = pyganim.PygAnimation(ANIMATION_STAY)
        self.animation_stay.play()
        self.animation_stay.blit(self.image, (0, 0))

        self.animation_jump_left = pyganim.PygAnimation(ANIMATION_JUMP_LEFT)
        self.animation_jump_left.play()

        self.animation_jump_right = pyganim.PygAnimation(ANIMATION_JUMP_RIGHT)
        self.animation_jump_right.play()

        self.animation_jump = pyganim.PygAnimation(ANIMATION_JUMP)
        self.animation_jump.play()

    def update(self, left, right, up, platforms):
        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
                self.image.fill(Color(COLOR))
                self.animation_jump.blit(self.image, (0, 0))

        if left:
            self.xvel = -MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.animation_jump_left.blit(self.image, (0, 0))
            else:
                self.animation_right.blit(self.image, (0, 0))

        if right:
            self.xvel = MOVE_SPEED
            self.image.fill(Color(COLOR))
            if up:
                self.animation_jump_right.blit(self.image, (0, 0))
            else:
                self.animation_right.blit(self.image, (0, 0))

        if not (left or right):
            self.xvel = 0
            if not up:
                self.image.fill(Color(COLOR))
                self.animation_stay.blit(self.image, (0, 0))

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms)

        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms)

    def collide(self, xvel, yvel, platforms):
        for e in platforms:
            if sprite.collide_rect(self, e):
                if xvel > 0:
                    self.rect.right = e.rect.left
                if xvel < 0:
                    self.rect.left = e.rect.right
                if yvel > 0:
                    self.rect.bottom = e.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.rect.top = e.rect.bottom
                    self.yvel = 0






#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame import *
import os

__author__ = 'kran'

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
ICON_DIR = os.path.dirname(__file__)


class Platform(sprite.Sprite):

    def __init__(self, x, y):
        super(Platform, self).__init__()
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color(PLATFORM_COLOR))
        self.image = image.load("%s/blocks/platform.png" % ICON_DIR)
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame import *
from player import *
from blocks import *

__author__ = 'kran'


WIN_WIDTH = 800
WIN_HEIGHT = 640
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = "#004400"

# timer = pygame.time.Clock()


class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect)


def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + WIN_WIDTH / 2, -t + WIN_HEIGHT / 2

    l = min(0, l)
    l = max(-(camera.width-WIN_WIDTH), l)
    t = max(-(camera.height-WIN_HEIGHT), t)
    t = min(0, t)

    return Rect(l, t, w, h)


def main():
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('Super Mario')
    visible_surface = Surface((WIN_WIDTH, WIN_HEIGHT))
    visible_surface.fill(Color(BACKGROUND_COLOR))
    hero = Player(55, 55)
    left = right = False
    up = False
    entities = pygame.sprite.Group()
    platforms = []
    entities.add(hero)
    level = [
        "----------------------------------",
        "-                                -",
        "-                       --       -",
        "-                                -",
        "-            --                  -",
        "-                                -",
        "--                               -",
        "-                                -",
        "-                   ----     --- -",
        "-                                -",
        "--                               -",
        "-                                -",
        "-                            --- -",
        "-                                -",
        "-                                -",
        "-      ---                       -",
        "-                                -",
        "-   -------         ----         -",
        "-                                -",
        "-                         -      -",
        "-                            --  -",
        "-                                -",
        "-                                -",
        "----------------------------------"
    ]

    timer = pygame.time.Clock()
    x = y = 0
    for row in level:
        for col in row:
            if col == "-":
                platform_surf = Platform(x, y)
                entities.add(platform_surf)
                platforms.append(platform_surf)

            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0
    total_level_width = len(level[0])*PLATFORM_WIDTH
    total_level_height = len(level)*PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)

    while 1:
        timer.tick(60)
        for i in pygame.event.get():
            if i.type == QUIT:
                raise SystemExit("Quit")
            if i.type == KEYDOWN and i.key == K_UP:
                up = True
            if i.type == KEYDOWN and i.key == K_LEFT:
                left = True
            if i.type == KEYDOWN and i.key == K_RIGHT:
                right = True
            if i.type == KEYUP and i.key == K_UP:
                up = False
            if i.type == KEYUP and i.key == K_RIGHT:
                right = False
            if i.type == KEYUP and i.key == K_LEFT:
                left = False

        screen.blit(visible_surface, (0, 0))

        camera.update(hero)
        hero.update(left, right, up, platforms)

        for j in entities:
            screen.blit(j.image, camera.apply(j))

        pygame.display.update()


if __name__ == "__main__":
    main()



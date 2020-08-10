# -*- coding: utf-8 -*-
import settings
import pygame
from pygame.locals import *
import math

TEXT_COLOR = (248, 252, 248)
BACK_COLOR = (154, 90, 178)
SYSTEMS_WIDTH = 288
SYSTEMS_HEIGHT = 195
SYSTEM_HEIGHT = 13
N_SYSTEMS_FIT = math.trunc(SYSTEMS_HEIGHT / SYSTEM_HEIGHT)

def draw_check(surface, pos=(0,0), status=False):
    pygame.draw.lines(surface, TEXT_COLOR, False, [(pos[0], pos[1]), (pos[0], pos[1]+8), (pos[0]+8, pos[1]+8), (pos[0]+8, pos[1]), (pos[0], pos[1])])
    if status:
        pygame.draw.line(surface, TEXT_COLOR, (pos[0], pos[1]), (pos[0]+8, pos[1]+8))
        pygame.draw.line(surface, TEXT_COLOR, (pos[0]+8, pos[1]), (pos[0], pos[1]+8))

def render():
    pane = pygame.Surface((SYSTEMS_WIDTH, SYSTEM_HEIGHT*N_SYSTEMS_FIT), SRCALPHA)

    pygame.draw.rect(pane, BACK_COLOR, (0, 0+settings.selected*SYSTEM_HEIGHT, SYSTEMS_WIDTH, SYSTEM_HEIGHT))

    n = 0
    for system in settings.config:
        draw_check(pane, (5, 2+n*SYSTEM_HEIGHT), system['enabled'])
        textsurface = settings.font.render(system['name'], False, TEXT_COLOR)
        pane.blit(textsurface, (5+12, 1+n*SYSTEM_HEIGHT))
        n = n + 1

    settings.screen.blit(pane, (16, 26))

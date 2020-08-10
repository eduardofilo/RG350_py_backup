# -*- coding: utf-8 -*-
import settings
import pygame
from pygame.locals import *
import math

TEXT_COLOR = (248, 252, 248)
TEXT_COLOR_ERROR = (255,65,65)
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
    scroll_pane = pygame.Surface((SYSTEMS_WIDTH, SYSTEM_HEIGHT*len(settings.config)), SRCALPHA)

    if len(settings.config) > 0:
        pygame.draw.rect(scroll_pane, BACK_COLOR, (0, 0+settings.selected*SYSTEM_HEIGHT, SYSTEMS_WIDTH, SYSTEM_HEIGHT))
        n = 0
        for system in settings.config:
            draw_check(scroll_pane, (5, 2+n*SYSTEM_HEIGHT), system['enabled'])
            textsurface = settings.font.render(system['name'], False, TEXT_COLOR)
            scroll_pane.blit(textsurface, (5+12, 1+n*SYSTEM_HEIGHT))
            n = n + 1
        if settings.selected + settings.offset + 1 > N_SYSTEMS_FIT:
            settings.offset = N_SYSTEMS_FIT - (settings.selected + 1)
        if settings.selected + settings.offset < 0:
            settings.offset = settings.offset + 1
        pane.blit(scroll_pane, (0, settings.offset*SYSTEM_HEIGHT))
    else:
        textsurface = settings.font.render("Bad configuration file or states directories not found", False, TEXT_COLOR_ERROR)
        pane.blit(textsurface, (5, 1))
        textsurface = settings.font.render("in system. Review log file at:", False, TEXT_COLOR_ERROR)
        pane.blit(textsurface, (5, 1+SYSTEM_HEIGHT))
        textsurface = settings.font.render(settings.LOG, False, TEXT_COLOR_ERROR)
        pane.blit(textsurface, (5, 1+2*SYSTEM_HEIGHT))

    settings.screen.blit(pane, (16, 26))

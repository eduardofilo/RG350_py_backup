# -*- coding: utf-8 -*-
import settings
import pygame

BACK_COLOR = (255,255,255)
FRONT_COLOR = (255,65,65)
TEXT_COLOR = (48, 36, 56)

def render():
    pygame.draw.rect(settings.screen, BACK_COLOR, (0, 0, 320, 18))
    pygame.draw.rect(settings.screen, BACK_COLOR, (2, 18, 316, 2))
    pygame.draw.lines(settings.screen, FRONT_COLOR, False, [(0, 0), (0,17), (2,19), (317,19), (319,17), (319,0)])
    textsurface = settings.font.render('Py Backup', False, TEXT_COLOR)
    settings.screen.blit(textsurface,(10,3))
    if len(settings.config) > 0:
        textsurface = settings.font.render(str(settings.selected+1) + "/" + str(len(settings.config)), False, TEXT_COLOR)
        settings.screen.blit(textsurface, (320 - textsurface.get_width() - 10, 3))

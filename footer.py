# -*- coding: utf-8 -*-
import settings
import pygame

BACK_COLOR = (178,188,194)
TEXT_COLOR = (48, 36, 56)

def render():
    # Background
    pygame.draw.rect(settings.screen, BACK_COLOR, (0, 225, 320, 15))

    if len(settings.config) > 0:
        # Select
        textsurface = settings.font.render('select', False, TEXT_COLOR)
        x = 6
        y = 227
        up_icon  = pygame.image.load('resources/UP_button.png').convert_alpha()
        settings.screen.blit(up_icon, (x, y))
        down_icon  = pygame.image.load('resources/DOWN_button.png').convert_alpha()
        settings.screen.blit(down_icon, (x+10, y))
        settings.screen.blit(textsurface,(x+25,y))

        # Toggle
        textsurface = settings.font.render('toggle', False, TEXT_COLOR)
        x = 70
        y = 227
        a_icon  = pygame.image.load('resources/A_button.png').convert_alpha()
        settings.screen.blit(a_icon, (x, y))
        settings.screen.blit(textsurface,(x+15,y))

    # Exit
    textsurface = settings.font.render('exit', False, TEXT_COLOR)
    x = 320-10-textsurface.get_width()-15
    y = 227
    start_icon  = pygame.image.load('resources/START_button.png').convert_alpha()
    settings.screen.blit(start_icon, (x, y))
    settings.screen.blit(textsurface,(x+15,y))

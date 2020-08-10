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
        x = 6
        y = 227
        up_icon  = pygame.image.load('resources/UP_button.png').convert_alpha()
        settings.screen.blit(up_icon, (x, y))

        x = x + up_icon.get_width()
        down_icon  = pygame.image.load('resources/DOWN_button.png').convert_alpha()
        settings.screen.blit(down_icon, (x, y))

        x = x + down_icon.get_width() + 5
        textsurface = settings.font.render('select', False, TEXT_COLOR)
        settings.screen.blit(textsurface,(x,y))

        # Toggle
        x = x + textsurface.get_width() + 15
        a_icon  = pygame.image.load('resources/A_button.png').convert_alpha()
        settings.screen.blit(a_icon, (x, y))

        x = x + a_icon.get_width() + 5
        textsurface = settings.font.render('toggle', False, TEXT_COLOR)
        settings.screen.blit(textsurface,(x,y))

        # Backup
        x = x + textsurface.get_width() + 15
        b_icon  = pygame.image.load('resources/B_button.png').convert_alpha()
        settings.screen.blit(b_icon, (x, y))

        x = x + b_icon.get_width() + 5
        textsurface = settings.font.render('backup', False, TEXT_COLOR)
        settings.screen.blit(textsurface,(x,y))

        # Restore
        x = x + textsurface.get_width() + 15
        x_icon  = pygame.image.load('resources/X_button.png').convert_alpha()
        settings.screen.blit(x_icon, (x, y))

        x = x + x_icon.get_width() + 5
        textsurface = settings.font.render('restore', False, TEXT_COLOR)
        settings.screen.blit(textsurface,(x,y))

    # Exit
    start_icon  = pygame.image.load('resources/START_button.png').convert_alpha()
    textsurface = settings.font.render('exit', False, TEXT_COLOR)

    x = 320 - start_icon.get_width() - textsurface.get_width() - 5 - 10
    y = 227
    settings.screen.blit(start_icon, (x, y))

    x = x + start_icon.get_width() + 5
    settings.screen.blit(textsurface,(x,y))

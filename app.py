import pygame
from pygame.locals import *
import logging  #logging.debug(string)
import keys
import settings


def render():
    # Draw background image
    background  = pygame.image.load('resources/background.png').convert()
    settings.screen.blit(background, (0, 0))

def handle_events(events):
    for event in events:
        if event.type == pygame.KEYUP:
            if event.key == keys.RG350_BUTTON_DOWN:
                settings.selected = settings.selected + 1
                if settings.selected > len(settings.config)-1:
                    settings.selected = len(settings.config)-1
            if event.key == keys.RG350_BUTTON_UP:
                settings.selected = settings.selected - 1
                if settings.selected < 0:
                    settings.selected = 0
            if event.key == keys.RG350_BUTTON_A:
                settings.config[settings.selected]['enabled'] = not settings.config[settings.selected]['enabled']

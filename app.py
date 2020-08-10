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
            if event.key == keys.RG350_BUTTON_START:
                pass

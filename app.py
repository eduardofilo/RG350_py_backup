import pygame
import logging  #logging.debug(string)
import keys
from random import *

class App():
    def __init__(self, screen, textFont):
        self.screen = screen
        self.textFont = textFont

    def render(self):
        # Draw background image
        background  = pygame.image.load('resources/background.png')
        self.screen.blit(background, (0, 0))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == keys.RG350_BUTTON_START:
                    pass


class States():
    def __init__(self, screen, textFont):
        self.screen = screen
        self.textFont = textFont

    def render(self):
        # Draw background image
        pass


class Header():
    BACK_COLOR = (255,255,255)
    FRONT_COLOR = (255,65,65)
    TEXT_COLOR = (48, 36, 56)

    def __init__(self, screen, textFont):
        self.screen = screen
        self.textFont = textFont

    def render(self):
        # Header
        pygame.draw.rect(self.screen, self.BACK_COLOR, (0, 0, 320, 18))
        pygame.draw.rect(self.screen, self.BACK_COLOR, (2, 18, 316, 2))
        pygame.draw.lines(self.screen, self.FRONT_COLOR, False, [(0, 0), (0,17), (2,19), (317,19), (319,17), (319,0)])

        textsurface = self.textFont.render('Py States Backup', False, self.TEXT_COLOR)
        self.screen.blit(textsurface,(10,3))

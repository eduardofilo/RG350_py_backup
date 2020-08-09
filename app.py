import pygame
import logging  #logging.debug(string)
import keys
from random import *

class App():
    def __init__(self, draw_tools):
        self.draw_tools = draw_tools

    def render(self):
        # Draw background image
        background  = pygame.image.load('resources/background.png').convert()
        self.draw_tools['screen'].blit(background, (0, 0))

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == keys.RG350_BUTTON_START:
                    pass


class States():
    def __init__(self, draw_tools):
        self.draw_tools = draw_tools

    def render(self):
        pass


class Header():
    BACK_COLOR = (255,255,255)
    FRONT_COLOR = (255,65,65)
    TEXT_COLOR = (48, 36, 56)

    def __init__(self, draw_tools):
        self.draw_tools = draw_tools

    def render(self):
        pygame.draw.rect(self.draw_tools['screen'], self.BACK_COLOR, (0, 0, 320, 18))
        pygame.draw.rect(self.draw_tools['screen'], self.BACK_COLOR, (2, 18, 316, 2))
        pygame.draw.lines(self.draw_tools['screen'], self.FRONT_COLOR, False, [(0, 0), (0,17), (2,19), (317,19), (319,17), (319,0)])
        textsurface = self.draw_tools['font'].render('Py States Backup', False, self.TEXT_COLOR)
        self.draw_tools['screen'].blit(textsurface,(10,3))


class Footer():
    BACK_COLOR = (178,188,194)
    TEXT_COLOR = (48, 36, 56)

    def __init__(self, draw_tools):
        self.draw_tools = draw_tools

    def render(self):
        pygame.draw.rect(self.draw_tools['screen'], self.BACK_COLOR, (0, 225, 320, 15))
        textsurface = self.draw_tools['font'].render('exit', False, self.TEXT_COLOR)
        x = 320-10-textsurface.get_width()-15
        y = 227
        start_icon  = pygame.image.load('resources/START_button.png').convert_alpha()
        self.draw_tools['screen'].blit(start_icon, (x, y))
        self.draw_tools['screen'].blit(textsurface,(x+15,y))

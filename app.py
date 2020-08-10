import pygame
from pygame.locals import *
import logging  #logging.debug(string)
import keys


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
    TEXT_COLOR = (248, 252, 248)
    BACK_COLOR = (104, 40, 128)

    def __init__(self, draw_tools, the_config):
        self.draw_tools = draw_tools
        self.the_config = the_config

    def draw_check(self, surface, pos=(0,0), status=False):
        pygame.draw.lines(surface, self.TEXT_COLOR, False, [(pos[0], pos[1]), (pos[0], pos[1]+8), (pos[0]+8, pos[1]+8), (pos[0]+8, pos[1]), (pos[0], pos[1])])
        if status:
            pygame.draw.line(surface, self.TEXT_COLOR, (pos[0], pos[1]), (pos[0]+8, pos[1]+8))
            pygame.draw.line(surface, self.TEXT_COLOR, (pos[0]+8, pos[1]), (pos[0], pos[1]+8))

    def render(self):
        pane = pygame.Surface((288,195), SRCALPHA)

        pygame.draw.rect(pane, self.BACK_COLOR, (0, 0, 288, 13))

        n = 0
        for system in self.the_config.config:
            self.draw_check(pane, (5, 2+n*13), system['enabled'])
            textsurface = self.draw_tools['font'].render(system['name'], False, self.TEXT_COLOR)
            pane.blit(textsurface,(5+12,1+n*13))
            n = n + 1

        self.draw_tools['screen'].blit(pane, (16, 26))


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
        # Background
        pygame.draw.rect(self.draw_tools['screen'], self.BACK_COLOR, (0, 225, 320, 15))

        # Select
        textsurface = self.draw_tools['font'].render('select', False, self.TEXT_COLOR)
        x = 6
        y = 227
        up_icon  = pygame.image.load('resources/UP_button.png').convert_alpha()
        self.draw_tools['screen'].blit(up_icon, (x, y))
        down_icon  = pygame.image.load('resources/DOWN_button.png').convert_alpha()
        self.draw_tools['screen'].blit(down_icon, (x+10, y))
        self.draw_tools['screen'].blit(textsurface,(x+25,y))

        # Exit
        textsurface = self.draw_tools['font'].render('exit', False, self.TEXT_COLOR)
        x = 320-10-textsurface.get_width()-15
        y = 227
        start_icon  = pygame.image.load('resources/START_button.png').convert_alpha()
        self.draw_tools['screen'].blit(start_icon, (x, y))
        self.draw_tools['screen'].blit(textsurface,(x+15,y))

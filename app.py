import pygame
import logging
import keys
from random import *

class States():
    def __init__(self, screen):
        self.screen = screen

    def handleEvents(self, events):
        running = True
        for event in events:
            if event.type == pygame.KEYUP:
                if event.key == keys.RG350_BUTTON_START:
                    running = False
        return running

    def render(self):
        # Draw screen
        background  = pygame.image.load('resources/background.png')
        self.screen.blit(background, (0, 0))

        #pygame.draw.circle(self.screen, (0,0,255), (randint(1, 300), 50), 20, 0)

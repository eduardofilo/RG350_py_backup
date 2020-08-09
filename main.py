# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
import logging
import keys, app


# Constants
BACKGROUND_COLOR = (255,153,51)
SCREEN_W = 320
SCREEN_H = 240
FPS = 15
LOG = "/media/data/local/home/.pystatesbackup/log.txt"


# Initialization
logging.basicConfig(level=logging.DEBUG, filename=LOG, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")
successes, failures = pygame.init()
logging.debug("{0} successes and {1} failures".format(successes, failures))

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
realScreen = pygame.display.set_mode((SCREEN_W,SCREEN_H), HWSURFACE, 16)
screen = pygame.Surface((SCREEN_W,SCREEN_H))

states = app.States(screen)


# Main loop
dt = 1 / FPS * 1000     # dt is the time since last frame.
running = True
while running:
    # Event management
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    if not states.handleEvents(events):
        running = False
    states.render()

    realScreen.blit(screen, (0,0))
    pygame.display.flip()
    dt = clock.tick(FPS)

pygame.quit()
sys.exit()
quit()

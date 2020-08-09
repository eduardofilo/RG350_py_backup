# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
import logging
import keys, app


# Constants
SCREEN_W = 320
SCREEN_H = 240
FPS = 15
if len(sys.argv) > 1 and sys.argv[1]=='debug':
    LOG = "/home/edumoreno/git/rg350_pystatesbackup/log.txt"
else:
    LOG = "/media/data/local/home/.pystatesbackup/log.txt"


# Initialization
logging.basicConfig(level=logging.DEBUG, filename=LOG, filemode="a+", format="%(asctime)-15s %(levelname)-8s %(message)s")
successes, failures = pygame.init()
logging.debug("{0} successes and {1} failures".format(successes, failures))
pygame.font.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
realScreen = pygame.display.set_mode((SCREEN_W,SCREEN_H), HWSURFACE, 16)
screen = pygame.Surface((SCREEN_W,SCREEN_H))
font = pygame.font.Font('resources/pixelberry.ttf', 8)

draw_tools = {'screen': screen, 'font': font}

the_app = app.App(draw_tools)
header = app.Header(draw_tools)
states = app.States(draw_tools)
footer = app.Footer(draw_tools)


# Main loop
dt = 1 / FPS * 1000     # dt is the time since last frame.
running = True
while running:
    # Event management
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == keys.RG350_BUTTON_START:
                running = False

    the_app.handle_events(events)

    the_app.render()
    header.render()
    states.render()
    footer.render()

    realScreen.blit(screen, (0,0))
    pygame.display.flip()
    dt = clock.tick(FPS)

pygame.quit()
sys.exit()
quit()

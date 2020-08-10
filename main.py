# -*- coding: utf-8 -*-
import settings, app, header, states, footer, keys
import sys
import logging
import pygame
from pygame.locals import *


settings.init()


# Initialization
successes, failures = pygame.init()
logging.debug("{0} successes and {1} failures".format(successes, failures))
pygame.font.init()

clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
realScreen = pygame.display.set_mode((settings.SCREEN_W,settings.SCREEN_H), HWSURFACE, 16)
screen = pygame.Surface((settings.SCREEN_W,settings.SCREEN_H))
font = pygame.font.Font('resources/pixelberry.ttf', 8)

settings.screen = screen
settings.font = font

# Main loop
dt = 1 / settings.FPS * 1000     # dt is the time since last frame.
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

    app.handle_events(events)

    app.render()
    header.render()
    states.render()
    footer.render()

    realScreen.blit(screen, (0,0))
    pygame.display.flip()
    dt = clock.tick(settings.FPS)

pygame.quit()
sys.exit()
quit()

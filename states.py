import settings
import pygame
from pygame.locals import *

TEXT_COLOR = (248, 252, 248)
BACK_COLOR = (104, 40, 128)

def draw_check(surface, pos=(0,0), status=False):
    pygame.draw.lines(surface, TEXT_COLOR, False, [(pos[0], pos[1]), (pos[0], pos[1]+8), (pos[0]+8, pos[1]+8), (pos[0]+8, pos[1]), (pos[0], pos[1])])
    if status:
        pygame.draw.line(surface, TEXT_COLOR, (pos[0], pos[1]), (pos[0]+8, pos[1]+8))
        pygame.draw.line(surface, TEXT_COLOR, (pos[0]+8, pos[1]), (pos[0], pos[1]+8))

def render():
    pane = pygame.Surface((288,195), SRCALPHA)

    pygame.draw.rect(pane, BACK_COLOR, (0, 0, 288, 13))

    n = 0
    for system in settings.config:
        draw_check(pane, (5, 2+n*13), system['enabled'])
        textsurface = settings.font.render(system['name'], False, TEXT_COLOR)
        pane.blit(textsurface,(5+12,1+n*13))
        n = n + 1

    settings.screen.blit(pane, (16, 26))

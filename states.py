# -*- coding: utf-8 -*-
import settings
import pygame
from pygame.locals import *
import math

TEXT_COLOR = (248, 252, 248)
TEXT_COLOR_ERROR = (255,65,65)
BACK_COLOR = (154, 90, 178)
SYSTEMS_WIDTH = 288
SYSTEMS_HEIGHT = 195
SYSTEM_HEIGHT = 13
N_SYSTEMS_FIT = math.trunc(SYSTEMS_HEIGHT / SYSTEM_HEIGHT)

def draw_check(surface, pos=(0,0), status=False):
    pygame.draw.lines(surface, TEXT_COLOR, False, [(pos[0], pos[1]), (pos[0], pos[1]+8), (pos[0]+8, pos[1]+8), (pos[0]+8, pos[1]), (pos[0], pos[1])])
    if status:
        pygame.draw.line(surface, TEXT_COLOR, (pos[0], pos[1]), (pos[0]+8, pos[1]+8))
        pygame.draw.line(surface, TEXT_COLOR, (pos[0]+8, pos[1]), (pos[0], pos[1]+8))

def normal(pane):
    scroll_pane = pygame.Surface((SYSTEMS_WIDTH, SYSTEM_HEIGHT*len(settings.config)), SRCALPHA)
    pygame.draw.rect(scroll_pane, BACK_COLOR, (0, 0+settings.selected*SYSTEM_HEIGHT, SYSTEMS_WIDTH, SYSTEM_HEIGHT))
    n = 0
    for system in settings.config:
        draw_check(scroll_pane, (5, 2+n*SYSTEM_HEIGHT), system['enabled'])
        textsurface = settings.font.render(system['name'], False, TEXT_COLOR)
        scroll_pane.blit(textsurface, (5+12, 1+n*SYSTEM_HEIGHT))
        n = n + 1
    if settings.selected + settings.offset + 1 > N_SYSTEMS_FIT:
        settings.offset = N_SYSTEMS_FIT - (settings.selected + 1)
    if settings.selected + settings.offset < 0:
        settings.offset = settings.offset + 1
    pane.blit(scroll_pane, (0, settings.offset*SYSTEM_HEIGHT))

def empty_config_error(pane):
    textsurface = settings.font.render("Empty configuration file or states directories not found.", False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1))
    textsurface = settings.font.render("Review log file at:", False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1+SYSTEM_HEIGHT))
    textsurface = settings.font.render(settings.LOG, False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1+2*SYSTEM_HEIGHT))

def wrong_config_error(pane):
    textsurface = settings.font.render("Bad configuration file.", False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1))
    textsurface = settings.font.render("Review log file at:", False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1+SYSTEM_HEIGHT))
    textsurface = settings.font.render(settings.LOG, False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1+2*SYSTEM_HEIGHT))

def wrong_destination_directory_error(pane):
    textsurface = settings.font.render("Destination directory not found.", False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1))
    textsurface = settings.font.render("Review config file at:", False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1+SYSTEM_HEIGHT))
    textsurface = settings.font.render(settings.CONFIG_FILE, False, TEXT_COLOR_ERROR)
    pane.blit(textsurface, (5, 1+2*SYSTEM_HEIGHT))

def confirm_backup(pane):
    normal(pane)

    confirmation_box  = pygame.image.load('resources/confirm.png').convert_alpha()
    x = SYSTEMS_WIDTH / 2 - confirmation_box.get_width() / 2
    y = 101-26
    pane.blit(confirmation_box, (x, y))

def do_backup(pane):
    normal(pane)

    progress_box  = pygame.image.load('resources/progress.png').convert_alpha()
    x = SYSTEMS_WIDTH / 2 - progress_box.get_width() / 2
    y = 101-26
    pane.blit(progress_box, (x, y))

    textsurface = settings.font.render("Backing up states of:", False, TEXT_COLOR)
    x = SYSTEMS_WIDTH / 2 - textsurface.get_width() / 2
    y = 101-20
    pane.blit(textsurface, (x, y))

    textsurface = settings.font.render(settings.config[settings.system]['name'], False, TEXT_COLOR)
    x = SYSTEMS_WIDTH / 2 - textsurface.get_width() / 2
    y = 101-4
    pane.blit(textsurface, (x, y))

render_mapping = {
    0: normal,
    1: empty_config_error,
    2: wrong_config_error,
    3: wrong_destination_directory_error,
    4: confirm_backup,
    5: do_backup
}

def render():
    pane = pygame.Surface((SYSTEMS_WIDTH, SYSTEM_HEIGHT*N_SYSTEMS_FIT), SRCALPHA)
    render_mapping[settings.status](pane)
    settings.screen.blit(pane, (16, 26))

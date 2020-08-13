# -*- coding: utf-8 -*-
import settings
import pygame
from pygame.locals import *
import math

TEXT_COLOR = (248, 252, 248)
TEXT_COLOR2 = (248, 252, 0)
TEXT_COLOR_ERROR = (255 ,65, 65)
BACK_COLOR = (154, 90, 178)
UNAVAILABLE_COLOR = (100, 100, 100)
SYSTEMS_WIDTH = 288
SYSTEMS_HEIGHT = 195
SYSTEM_HEIGHT = 13
N_SYSTEMS_FIT = math.trunc(SYSTEMS_HEIGHT / SYSTEM_HEIGHT)

def draw_check(surface, pos=(0,0), status=False, available=False):
    color = TEXT_COLOR if available else UNAVAILABLE_COLOR
    pygame.draw.lines(surface, color, False, [(pos[0], pos[1]), (pos[0], pos[1]+8), (pos[0]+8, pos[1]+8), (pos[0]+8, pos[1]), (pos[0], pos[1])])
    if status:
        pygame.draw.line(surface, color, (pos[0], pos[1]), (pos[0]+8, pos[1]+8))
        pygame.draw.line(surface, color, (pos[0]+8, pos[1]), (pos[0], pos[1]+8))

def normal(pane):
    scroll_pane = pygame.Surface((SYSTEMS_WIDTH, SYSTEM_HEIGHT*len(settings.config)), SRCALPHA)
    pygame.draw.rect(scroll_pane, BACK_COLOR, (0, 0+settings.selected*SYSTEM_HEIGHT, SYSTEMS_WIDTH, SYSTEM_HEIGHT))
    n = 0
    for system in settings.config:
        draw_check(scroll_pane, (5, 2+n*SYSTEM_HEIGHT), system['enabled'], system['source_available'])
        color = TEXT_COLOR if system['backup_available'] else TEXT_COLOR_ERROR
        color = color if system['source_available'] else UNAVAILABLE_COLOR
        textsurface = settings.font.render(system['name'], False, color)
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

def confirm(pane):
    normal(pane)

    confirmation_box  = pygame.image.load('resources/popup.png').convert_alpha()
    x = SYSTEMS_WIDTH / 2 - confirmation_box.get_width() / 2
    y = 101-26
    pane.blit(confirmation_box, (x, y))

    if settings.status == 4:
        message = "Are you sure to begin backup?"
    elif settings.status == 6:
        message = "Are you sure to begin restore?"
    else:
        message = "Are you sure?"
    textsurface = settings.font.render(message, False, TEXT_COLOR)
    x = SYSTEMS_WIDTH / 2 - textsurface.get_width() / 2
    y = 101-20
    pane.blit(textsurface, (x, y))

    a_icon  = pygame.image.load('resources/A_button.png').convert_alpha()
    textsurface_a = settings.font.render("accept", False, TEXT_COLOR2)
    b_icon  = pygame.image.load('resources/B_button.png').convert_alpha()
    textsurface_b = settings.font.render("cancel", False, TEXT_COLOR2)

    x = SYSTEMS_WIDTH / 2 - (a_icon.get_width() + 5 + textsurface_a.get_width() + 10 + b_icon.get_width() + 5 + textsurface_b.get_width()) / 2
    y = 101-4
    pane.blit(a_icon, (x, y))
    x += a_icon.get_width() + 5
    pane.blit(textsurface_a, (x, y))
    x += textsurface_a.get_width() + 10
    pane.blit(b_icon, (x, y))
    x += b_icon.get_width() + 5
    pane.blit(textsurface_b, (x, y))

def do_backup(pane):
    normal(pane)

    popup_box  = pygame.image.load('resources/popup.png').convert_alpha()
    x = SYSTEMS_WIDTH / 2 - popup_box.get_width() / 2
    y = 101-26
    pane.blit(popup_box, (x, y))

    textsurface = settings.font.render("Backing up:", False, TEXT_COLOR)
    x = SYSTEMS_WIDTH / 2 - textsurface.get_width() / 2
    y = 101-20
    pane.blit(textsurface, (x, y))

    textsurface = settings.font.render(settings.config[settings.system]['name'], False, TEXT_COLOR2)
    x = SYSTEMS_WIDTH / 2 - textsurface.get_width() / 2
    y = 101-4
    pane.blit(textsurface, (x, y))

def do_restore(pane):
    normal(pane)

    popup_box  = pygame.image.load('resources/popup.png').convert_alpha()
    x = SYSTEMS_WIDTH / 2 - popup_box.get_width() / 2
    y = 101-26
    pane.blit(popup_box, (x, y))

    textsurface = settings.font.render("Restoring:", False, TEXT_COLOR)
    x = SYSTEMS_WIDTH / 2 - textsurface.get_width() / 2
    y = 101-20
    pane.blit(textsurface, (x, y))

    textsurface = settings.font.render(settings.config[settings.system]['name'], False, TEXT_COLOR2)
    x = SYSTEMS_WIDTH / 2 - textsurface.get_width() / 2
    y = 101-4
    pane.blit(textsurface, (x, y))

render_mapping = {
    0: normal,
    1: empty_config_error,
    2: wrong_config_error,
    3: wrong_destination_directory_error,
    4: confirm,
    5: do_backup,
    6: confirm,
    7: do_restore
}

def render():
    pane = pygame.Surface((SYSTEMS_WIDTH, SYSTEM_HEIGHT*N_SYSTEMS_FIT), SRCALPHA)
    render_mapping[settings.status](pane)
    settings.screen.blit(pane, (16, 26))

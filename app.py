# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import keys, settings, config
import os
import time


def render():
    # Draw background image
    background  = pygame.image.load('resources/background.png').convert()
    settings.screen.blit(background, (0, 0))

def handler_normal(key):
    if key == keys.RG350_BUTTON_DOWN:
        settings.selected += 1
        if settings.selected > len(settings.config) - 1:
            settings.selected = 0
    elif key == keys.RG350_BUTTON_UP:
        settings.selected -= 1
        if settings.selected < 0:
            settings.selected = len(settings.config) - 1
    elif key == keys.RG350_BUTTON_A:
        if settings.config[settings.selected]['source_available']:
            settings.config[settings.selected]['enabled'] = not settings.config[settings.selected]['enabled']
    elif key == keys.RG350_BUTTON_B:
        if settings.n_systems_enabled() > 0:
            settings.status = 4
    elif key == keys.RG350_BUTTON_X:
        if settings.n_backups_available() > 0:
            settings.status = 6

def handler_confirm_backup(key):
    if key == keys.RG350_BUTTON_A:
        settings.status = 5
        settings.system = settings.next_backup_system(0)
    elif key == keys.RG350_BUTTON_B:
        settings.status = 0

def handler_confirm_restore(key):
    if key == keys.RG350_BUTTON_A:
        settings.status = 7
        settings.system = settings.next_restore_system(0)
    elif key == keys.RG350_BUTTON_B:
        settings.status = 0

def handler_void(key):
    pass

handler_mapping = {
    0: handler_normal,
    1: handler_void,
    2: handler_void,
    3: handler_void,
    4: handler_confirm_backup,
    5: handler_void,
    6: handler_confirm_restore,
    7: handler_void
}

def handle_events(events):
    for event in events:
        if event.type == pygame.KEYUP:
            handler_mapping[settings.status](event.key)


def do_backup(system):
    if settings.system < len(settings.config):
        backup_file = settings.backup_filename(settings.config[system]['name'])
        my_cmd = "tar -czf '%s' %s" % (backup_file, " ".join(settings.config[system]['dirs']))
        os.system(my_cmd)
        my_cmd = "sync"
        os.system(my_cmd)
        time.sleep(0.5)
    settings.system = settings.next_backup_system(settings.system + 1)
    if settings.system < 0:
        settings.status = 0

def do_restore(system):
    if settings.system < len(settings.config):
        backup_file = settings.backup_filename(settings.config[system]['name'])
        if os.path.exists(backup_file):
            my_cmd = "tar -xzf '%s' -C /" % (backup_file)
            os.system(my_cmd)
            my_cmd = "sync"
            os.system(my_cmd)
        time.sleep(0.5)
    settings.system = settings.next_restore_system(settings.system + 1)
    if settings.system < 0:
        settings.status = 0

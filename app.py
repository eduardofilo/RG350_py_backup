# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import logging  #logging.debug(string)
import keys
import settings
import os
import time


def render():
    # Draw background image
    background  = pygame.image.load('resources/background.png').convert()
    settings.screen.blit(background, (0, 0))

def handle_events(events):
    for event in events:
        if event.type == pygame.KEYUP:
            if settings.status == 0:    # NORMAL status
                if event.key == keys.RG350_BUTTON_DOWN:
                    settings.selected = settings.selected + 1
                    if settings.selected > len(settings.config)-1:
                        settings.selected = len(settings.config)-1
                elif event.key == keys.RG350_BUTTON_UP:
                    settings.selected = settings.selected - 1
                    if settings.selected < 0:
                        settings.selected = 0
                elif event.key == keys.RG350_BUTTON_A:
                    settings.config[settings.selected]['enabled'] = not settings.config[settings.selected]['enabled']
                    settings.config_enabled = filter(lambda system : system['enabled'], settings.config)
                elif event.key == keys.RG350_BUTTON_B:
                    if len(settings.config_enabled) > 0:
                        settings.status = 4
            elif settings.status == 4:    # Confirm backup status
                if event.key == keys.RG350_BUTTON_A:
                    settings.status = 5
                    settings.system = 0
                elif event.key == keys.RG350_BUTTON_B:
                    settings.status = 0

def do_backup(system):
    if settings.system < len(settings.config_enabled):
        time.sleep(0.5)
        #myCmd = 'ls -la'
        #os.system(myCmd)
    settings.system = settings.system + 1
    if settings.system >= len(settings.config_enabled):
        settings.status = 0

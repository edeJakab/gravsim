import pygame
import pygame_gui

from engine import *

class body_button:
    def __init__(self, body, manager, cam):
        self.pos = cam.world_to_screen(body.pos)
        self.gui = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.pos, (15,15)), text = "", manager=manager)

b_buttons = []

def update_b_buttons(b_buttons, manager, cam):
    for body in bodies:
        b_buttons.append(body_button(body, manager, cam))
        

import pygame
import pygame_gui
from engine import *

class body_button:
    def __init__(self, body, uimanager, cam):
        self.body = body
        self.pos = cam.world_to_screen(body.pos)
        self.gui = pygame_gui.elements.UIButton(relative_rect=pygame.Rect(self.pos, (15,15)), text = "", manager=uimanager)

    def update_gui(self):
        self.gui.set_relative_position(self.pos)

    def kill(self):
        self.gui.kill()

b_buttons = {} 

def update_b_buttons(b_buttons, uimanager, cam):
    for body in bodies:
        if b_buttons.get(body) == None:
            b_buttons[body] = body_button(body, uimanager, cam)
        else:
            b_buttons[body].pos = cam.world_to_screen(body.pos)
            b_buttons[body].update_gui()

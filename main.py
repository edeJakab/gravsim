import pygame
import pygame_gui
from engine import *
from gui import *


# constants
SCREEN_SIZE = (1280, 720)
dt = 0
dt_multiplier = 1
frozen = False
running = True


# initializing important components
pygame.init()
uimanager = pygame_gui.UIManager(SCREEN_SIZE)
screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
cam = Camera(0.1, pygame.Vector2(100, 0))

# initializing buttons
add_body = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,30), (100,80)), text = 'add body', manager=uimanager)
clear_bodies = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,140), (100,80)), text = 'clear bodies', manager=uimanager)
freeze = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,250), (100,80)), text = 'pause', manager=uimanager)
distributed = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,360), (100,80)), text = 'distributed', manager=uimanager)
b_buttons = {}

# game loop
while running:
    dt = clock.tick(60) / 50
    dt = dt * dt_multiplier

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == add_body:
                bodies.append(Body(20000000000000000, 400, pygame.Vector2((1000, 3000)), pygame.Vector2(0, 0), pygame.Vector2(0, 0)))

            if event.ui_element == clear_bodies:
                bodies = []
                # for b_button in b_buttons.values():
                    # b_button.gui.kill()
                for body in bodies:
                    b_buttons[body].kill()
                print(len(b_buttons), flush = True)
                print(len(bodies), flush = True)

            if event.ui_element == freeze:
                if not frozen:
                    frozen = True
                else:
                    frozen = False

            if event.ui_element == distributed:
                for i in range(100, 2001, 100):
                    for j in range(100, 1001, 100):
                        bodies.append(Body(1, 40, pygame.Vector2((i, j)), pygame.Vector2(25, 0), pygame.Vector2(0, 0)))

        uimanager.process_events(event)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        cam.pos.y += 10
    if keys[pygame.K_s]:
        cam.pos.y -= 10
    if keys[pygame.K_a]:
        cam.pos.x += 10
    if keys[pygame.K_d]:
        cam.pos.x -= 10
    if keys[pygame.K_r]:
        cam.zoom *= 1.01
    if keys[pygame.K_e]:
        cam.zoom *= 0.99
    if keys[pygame.K_v]:
        dt_multiplier += 0.11
   

    screen.fill("white")
    if not frozen:
        update_bodies(bodies, dt)
    for body in bodies:
        pygame.draw.circle(screen, "red", cam.world_to_screen(body.pos), cam.scale(body.rad))
    update_b_buttons(b_buttons, uimanager, cam)
    uimanager.update(dt)
    uimanager.draw_ui(screen)
    pygame.display.flip()


    print("len(b_buttons)", len(b_buttons), flush = True)


pygame.quit()

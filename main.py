import pygame
import pygame_gui
from engine import *
from gui import *

pygame.init()
screen_size = (1280, 720)
screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()
running = True

dt = 0
dt_multiplier = 1

manager = pygame_gui.UIManager(screen_size)

cam = Camera(0.1, pygame.Vector2(100, 0))

add_body = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,30), (100,80)), text = 'add body', manager=manager)
clear_bodies = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,140), (100,80)), text = 'clear bodies', manager=manager)
freeze = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,250), (100,80)), text = 'pause', manager=manager)
distributed = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,360), (100,80)), text = 'distributed', manager=manager)

buttoney = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,460), (100,80)), text = 'LOL', manager=manager)

b_buttons = {}

frozen = False

while running:
    dt = clock.tick(60) / 50
    dt = dt * dt_multiplier

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == add_body:
                bodies.append(Body(20000000000000000, 400, pygame.Vector2((1000, 3000)), pygame.Vector2(0, 0), pygame.Vector2(0, 0)))
                print('hello', len(bodies), flush=True)
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
        if event.type == pygame_gui.UI_BUTTON_ON_HOVERED:
            if event.ui_element == buttoney:
                print("pressed", flush=True)
                b_buttons[bodies[0]].kill()

        manager.process_events(event)

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
    
    update_b_buttons(b_buttons, manager, cam)
    print(len(b_buttons), flush = True)

    manager.update(dt)
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()

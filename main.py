import pygame
import pygame_gui
from engine import *

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
dtxd = 0.55

manager = pygame_gui.UIManager((1280, 720))

cam = Camera(1, pygame.Vector2(100, 0))

bodies = []

add_body = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,30), (100,80)), text = 'add body', manager=manager)
clear_bodies = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,140), (100,80)), text = 'clear bodies', manager=manager)
freeze = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((30,250), (100,80)), text = 'pause', manager=manager)

frozen = False

while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == add_body:
                bodies.append(Body(1, 40, pygame.Vector2(300, -300), pygame.Vector2(30, 0), pygame.Vector2(0, 10)))
                print('hello', len(bodies), flush=True)
            if event.ui_element == clear_bodies:
                bodies = []
            if event.ui_element == freeze:
                if not frozen:
                    frozen = True
                else:
                    frozen = False

        manager.process_events(event)

    screen.fill("purple")

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
    
    if not frozen:
        for i in range(len(bodies)):
            bodies[i].update_state(dtxd)
            wall_collision(bodies[i], 0, 3280, 0, 1720)

    for i in range(len(bodies)):
        pygame.draw.circle(screen, "red", cam.world_to_screen(bodies[i].pos), cam.scale(bodies[i].rad))

    manager.update(dt)
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()

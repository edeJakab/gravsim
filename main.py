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

xi = 600
yi = 300
init_pos = pygame.Vector2(xi, yi)
m1 = 100000000000000
r = 200
v = (grav_constant * m1 / r) ** 0.5
ball = Body(m1, 40, init_pos, pygame.Vector2(0, 0), pygame.Vector2(0, 5000))
ball2 = Body(10, 40, pygame.Vector2(xi + r, yi), pygame.Vector2(0, v), pygame.Vector2(0, 0))

add_body = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350,275), (100,50)), text = 'say hello', manager=manager)
a21dd_body = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((650,275), (100,50)), text = 'say hello', manager=manager)

while running:

    dt = clock.tick(60) / 1000

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == add_body:
                print('hello', flush=True)

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
    
    grav_update_pair(ball, ball2)
    ball.update_state(dtxd)
    ball2.update_state(dtxd)
    wall_collision(ball, 0, 1280, 0, 720)
    wall_collision(ball2, 0, 1280, 0, 720)

    pygame.draw.circle(screen, "red", cam.world_to_screen(ball.pos), cam.scale(ball.rad))
    pygame.draw.circle(screen, "red", cam.world_to_screen(ball2.pos), cam.scale(ball2.rad))

    manager.update(dt)
    manager.draw_ui(screen)
    pygame.display.flip()

pygame.quit()

# Example file showing a circle moving on screen
import pygame

class body:
    def __init__(self, mass, pos, vel, acc):
        self.mass = mass
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.acc = pygame.Vector2(acc)
    def update_state(self, dt):
        self.pos += self.vel * dt
        self.vel += self.acc * dt

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
dtxd = 0.01


init_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
ball = body(10, init_pos, pygame.Vector2(10, 10), pygame.Vector2(100, 0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", ball.pos, 40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        ball.pos.y -= 300 * dt
    if keys[pygame.K_s]:
        ball.pos.y += 300 * dt
    if keys[pygame.K_a]:
        ball.pos.x -= 300 * dt
    if keys[pygame.K_d]:
        ball.pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
    ball.update_state(dtxd)

pygame.quit()

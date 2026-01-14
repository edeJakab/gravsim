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

class camera:
    def __init__(self, zoom, pos):
        self.zoom = zoom # compared to in-game. zoom = 1 means 1:1 correspondence
        self.pos = pygame.Vector2(pos) # position of the top left corner of the camera in in-game coordinates

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
dtxd = 0.01

camera = camera(5, pygame.Vector2(0, 0))


init_pos = pygame.Vector2(screen.get_width() / 9, screen.get_height() / 9)
ball = body(10, init_pos, pygame.Vector2(10, 10), pygame.Vector2(0, 0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", ball.pos * camera.zoom + camera.pos, 40 * camera.zoom)

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

    print (screen.get_width(), flush=True)
pygame.quit()

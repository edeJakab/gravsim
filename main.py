import pygame

class camera:
    def __init__(self, zoom, pos):
        self.zoom = zoom # compared to in-game. zoom = 1 means 1:1 correspondence
        self.pos = pygame.Vector2(pos) # position of the top left corner of the camera in in-game coordinates
    def world_to_screen(self, world_pos):
        return world_pos * camera.zoom + camera.pos
    def scale(self, rad):
        return rad * camera.zoom

class body:
    def __init__(self, mass, rad, pos, vel, acc):
        self.mass = mass
        self.rad = rad
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.acc = pygame.Vector2(acc)
    def update_state(self, dt):
        self.pos += self.vel * dt
        self.vel += self.acc * dt

def wall_collision(body, x_min, x_max, y_min, y_max):
    if body.pos.x - body.rad <= x_min or body.pos.x + body.rad >= x_max:
        body.vel.x = -body.vel.x
    if body.pos.y - body.rad <= y_min or body.pos.y + body.rad >= y_max:
        body.vel.y = -body.vel.y

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
dtxd = 0.01

camera = camera(1, pygame.Vector2(0, 0))

init_pos = pygame.Vector2(screen.get_width() / 9, screen.get_height() / 9)
ball = body(10, 40, init_pos, pygame.Vector2(2000, 1000), pygame.Vector2(0, 0))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

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
    wall_collision(ball, 0, 1280, 0, 720)
    ball.update_state(dtxd)
    print (ball.pos, flush=True)

    pygame.draw.circle(screen, "red", camera.world_to_screen(ball.pos), camera.scale(ball.rad))
    pygame.display.flip()

    dt = clock.tick(60) / 1000
pygame.quit()

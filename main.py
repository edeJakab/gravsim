import pygame

grav_constant = 6.674e-11

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
        self.vel += self.acc * dt
        self.pos += self.vel * dt

def wall_collision(body, x_min, x_max, y_min, y_max):
    if body.pos.x - body.rad <= x_min:
        body.pos.x = x_min + body.rad
        body.vel.x = -body.vel.x
    if body.pos.x + body.rad >= x_max:
        body.pos.x = x_max - body.rad
        body.vel.x = -body.vel.x
    if body.pos.y - body.rad <= y_min:
        body.pos.y = y_min + body.rad
        body.vel.y = -body.vel.y
    if body.pos.y + body.rad >= y_max:
        body.pos.y = y_max - body.rad
        body.vel.y = -body.vel.y

def grav_update(body1, body2):
    vec12 = body2.pos - body1.pos
    body1.acc = (grav_constant * body1.mass * body2.mass / (pygame.Vector2.magnitude(vec12) ** 2) ) * pygame.Vector2.normalize(vec12)
    body2.acc = (grav_constant * body1.mass * body2.mass / (pygame.Vector2.magnitude(vec12) ** 2) ) * pygame.Vector2.normalize(-vec12)

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
dtxd = 0.01

camera = camera(1, pygame.Vector2(0, 0))

init_pos = pygame.Vector2(screen.get_width() / 9, screen.get_height() / 9)
ball = body(100000000000000, 40, init_pos, pygame.Vector2(0, 0), pygame.Vector2(0, 5000))
ball2 = body(10, 40, init_pos*2, pygame.Vector2(0, 0), pygame.Vector2(0, 0))

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
    
    # grav_update(ball, ball2)
    ball.update_state(dtxd)
    ball2.update_state(dtxd)
    wall_collision(ball, 0, 1280, 0, 720)
    wall_collision(ball2, 0, 1280, 0, 720)

    pygame.draw.circle(screen, "red", camera.world_to_screen(ball.pos), camera.scale(ball.rad))
    pygame.draw.circle(screen, "red", camera.world_to_screen(ball2.pos), camera.scale(ball2.rad))
    pygame.display.flip()

    dt = clock.tick(60) / 1000
pygame.quit()

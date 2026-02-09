import pygame

grav_constant = 6.674e-11

class Camera:
    def __init__(self, zoom, pos):
        self.zoom = zoom # compared to in-game. zoom = 1 means 1:1 correspondence
        self.pos = pygame.Vector2(pos) # position of the top left corner of the camera in in-game coordinates
    def world_to_screen(self, world_pos):
        return world_pos * self.zoom + self.pos
    def scale(self, rad):
        return rad * self.zoom

class Body:
    def __init__(self, mass, rad, pos, vel, acc):
        self.mass = mass
        self.rad = rad
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.acc = pygame.Vector2(acc)
    def update_state(self, dt):
        self.pos += self.vel * dt + self.acc * dt * dt / 2
        self.vel += self.acc * dt

bodies = []

def update_gravity(bodies):
    for body1 in bodies:
        net_force = pygame.Vector2((0, 0))
        for body2 in bodies:
            r12 = body2.pos - body1.pos
            if pygame.Vector2.magnitude(r12) > 40:
                net_force += ((grav_constant * body1.mass * body2.mass) / (pygame.Vector2.magnitude(r12) ** 2) ) * pygame.Vector2.normalize(r12)
        net_acc = net_force / body1.mass
        body1.acc = net_acc

def update_bodies(bodies, dt):
    update_gravity(bodies)
    for body in bodies:
        body.update_state(dt)


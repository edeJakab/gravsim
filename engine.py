# The simulated objects are independent of the objects on screen.
# Modifying the camera only changes our view, not the simulation itself.
# This is useful because we can move our view, and zoom in/out.

import pygame

# for realistic values
grav_constant = 6.674e-11

# Gravitational forces are not updated below this distance to avoid unrealistically large accelerations.
MIN_GRAV_DISTANCE = 40

class Camera:
    def __init__(self, zoom, pos):
        # compared to in-game. zoom = 1 means 1:1 correspondence
        self.zoom = zoom 
        # position of the top left corner of the camera in in-game coordinates
        self.pos = pygame.Vector2(pos) 

    # convert world coordinates to onscreen coordinates
    def world_to_screen(self, world_pos): 
        return world_pos * self.zoom + self.pos

    # convert world length (e.g. radius) to onscreen length
    def scale(self, rad):
        return rad * self.zoom

class Body:
    def __init__(self, mass, rad, pos, vel, acc):
        self.mass = mass
        self.rad = rad
        self.pos = pygame.Vector2(pos)
        self.vel = pygame.Vector2(vel)
        self.acc = pygame.Vector2(acc)
    
    # updates the position and velocity of a body
    def update_state(self, dt):
        self.pos += self.vel * dt + self.acc * dt * dt / 2
        self.vel += self.acc * dt

# contains all the simulated bodies
bodies = []

# updates the acceleration of all bodies. only gravity is taken into account
def update_gravity(bodies):
    for body1 in bodies:
        net_force = pygame.Vector2((0, 0))
        for body2 in bodies:
            r12 = body2.pos - body1.pos
            if pygame.Vector2.magnitude(r12) >= 40:
                net_force += ((grav_constant * body1.mass * body2.mass) / (pygame.Vector2.magnitude(r12) ** 2) ) * pygame.Vector2.normalize(r12)
        net_acc = net_force / body1.mass
        body1.acc = net_acc

# updates the acceleration, then updates the position and velocity of all bodies
def update_bodies(bodies, dt):
    update_gravity(bodies)
    for body in bodies:
        body.update_state(dt)

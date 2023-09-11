import pygame, pgzrun
import math


TITLE = "Eyes"


def draw_eye(eye_x, eye_y, size):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    distance_x = mouse_x - eye_x
    distance_y = mouse_y - eye_y
    distance = math.sqrt(distance_x ** 2  +  distance_y **  2)
    distance = min(distance, size - 20)
    angle = math.atan2(distance_y, distance_x)
    angle_deg = angle * 180 / math.pi
    pupil_x = eye_x + (math.cos(angle) * distance)
    pupil_y = eye_y + (math.sin(angle) * distance)
    screen.draw.filled_circle((eye_x, eye_y), size, color=(255, 255, 255))
    screen.draw.filled_circle((pupil_x, pupil_y), 15, color=(0, 0, 100))
    # screen.draw.filled_circle((pupil_x, pupil_y), size * 0.3, color=(0, 0, 100))

def update():
    pass


template = '''distance X: %d
distance Y: %d
distance: %s
angle: %s'''



def draw():
    screen.fill((0, 0, 0))
    draw_eye(200, 200, 50)
    draw_eye(285, 200, 40)
    draw_eye(200, 200, 50)
    draw_eye(285, 200, 40)




    # screen.draw.text(template % (distance_x, distance_y, distance, angle_deg), (0, 0))






pgzrun.go()

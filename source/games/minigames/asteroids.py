import os
os.environ['SDL_video_window_pos'] = '%d,%d' % (20, 100)
import pgzrun
import math
import random

WIDTH = 800
HEIGHT = 600
PLAYER_R = 30

C_BACKGROUND = (0, 16, 0)
C_PLAYER_FILL = (0, 32, 0)
C_PLAYER_STROKE = (0, 255, 0)
C_BULLET = C_PLAYER_STROKE
C_ASTEROID_FILL = (0, 24, 8)
C_ASTEROID_STROKE = (0, 196, 64)
C_ASTEROID_STROKE_COLLISION = (255, 0, 0)
TURN_ANGLE = 10
BULLET_SPEED = 500
BULLET_RADIUS = 3



def reset(): # {{{
    global ship_x, ship_y
    global ship_speed_x, ship_speed_y
    global ship_angle
    global bullet_timer
    global bullets
    global asteroids
    global asteroid_stages
    global bullet_timer, bullet_timer_limit


    ship_x = WIDTH/2
    ship_y = HEIGHT/2
    ship_angle = 0
    ship_speed_x = 0
    ship_speed_y = 0
    bullets = []
    bullet_timer_limit = 0.005
    bullet_timer = bullet_timer_limit
    asteroid_radius = 88


    asteroids = [ # {{{
        {
            'x': 100,
            'y': 100,
            },

        {
            'x': WIDTH - 100,
            'y': 100,
            },

        {
            'x': WIDTH / 2,
            'y': HEIGHT - 100,
            },
            ] # }}}
    asteroid_stages = [ # {{{
            { 's': 120, 'r': 15 },
            { 's': 70, 'r': 30 },
            { 's': 50, 'r': 50 },
            { 's': 20, 'r': 80 },
            ]
    # }}}
    for asteroid in asteroids:
        asteroid['angle'] = random.random() * 2 * math.pi
        asteroid['c'] = C_ASTEROID_STROKE
        asteroid['stage'] = len(asteroid_stages) -1
    # }}}
def are_circles_intersecting(ax,ay,ar,bx,by,br): # {{{
    return (ax-bx)**2 + (ay-by)**2 <=(ar+br)**2
# }}}
def point_on_circle(x, y, r, a): # {{{
    px = x + math.cos(a) * (r-5)
    py = y + math.sin(a) * (r-5)
    return (px, py)
# }}}
def update(dt): # {{{
    global ship_angle
    global ship_x, ship_y
    global ship_speed_x, ship_speed_y
    global bullet_timer

    if len(asteroids) == 0: reset()

    for asteroid in asteroids:
        asteroid_speed = asteroid_stages[asteroid['stage']]['s']
        asteroid['x'] += math.cos(asteroid['angle']) * asteroid_speed * dt
        asteroid['y'] += math.sin(asteroid['angle']) * asteroid_speed * dt
        asteroid['x'] %= WIDTH
        asteroid['y'] %= HEIGHT
        if are_circles_intersecting(
            ship_x,ship_y, PLAYER_R,
            asteroid['x'], asteroid['y'], asteroid_stages[asteroid['stage']]['r']
                ):
            # asteroid['c'] = C_ASTEROID_STROKE_COLLISION
            reset()
        else: asteroid['c'] = C_ASTEROID_STROKE


    if keyboard.D: ship_angle += TURN_ANGLE * dt
    elif keyboard.A: ship_angle -= TURN_ANGLE * dt
    elif keyboard.W:
        ship_speed = 100
        ship_speed_x +=  math.cos(ship_angle) * ship_speed * dt
        ship_speed_y +=  math.sin(ship_angle) * ship_speed * dt

    ship_x += ship_speed_x * dt
    ship_y += ship_speed_y * dt
    ship_x %= WIDTH
    ship_y %= HEIGHT
    ship_angle %= 2*math.pi

    bullet_timer += dt

    if keyboard.SPACE:
        if bullet_timer >= bullet_timer_limit:
            bullet_timer = 0
            x, y = point_on_circle(ship_x, ship_y, PLAYER_R, ship_angle)
            bullets.append({
                'x': x, 'y': y,
                'a': ship_angle, 't': 4,
                })


    # Because bullets are removed from the list while it is being looped
    # through, a copy of the list is created to loop through.
    for bullet in bullets.copy():
        bullet['t'] -= dt
        if bullet['t'] <= 0:
            bullets.remove(bullet)
            continue
        bullet['x'] += math.cos(bullet['a']) * BULLET_SPEED *  dt
        bullet['y'] += math.sin(bullet['a']) * BULLET_SPEED *  dt
        # bullet['x'] %= WIDTH
        # bullet['y'] %= HEIGHT

        for asteroid in asteroids.copy():
            if are_circles_intersecting(
            bullet['x'], bullet['y'], BULLET_RADIUS,
            asteroid['x'], asteroid['y'], asteroid_stages[asteroid['stage']]['r']
            ):
                if asteroid['stage'] > 0:
                    a1  = random.random() * 2 * math.pi
                    a2  = (a1 - math.pi) % (2*math.pi)
                    asteroids.append({
                        'x': asteroid['x'], 
                        'y': asteroid['y'],
                        'angle': a1,
                        'c': C_ASTEROID_STROKE,
                        'stage': asteroid['stage']-1,
                        })

                    asteroids.append({
                        'x': asteroid['x'], 
                        'y': asteroid['y'],
                        'angle': a2,
                        'c': C_ASTEROID_STROKE,
                        'stage': asteroid['stage']-1,
                        })

                bullets.remove(bullet)
                asteroids.remove(asteroid)
                break

    # }}}
def draw(): # {{{
    global ship_angle
    screen.fill(C_BACKGROUND)





    for y in (-1, 0, 1):
        for x in (-1, 0, 1):
            offset_x = x * WIDTH
            offset_y = y * HEIGHT

            # ASTEROIDS
            for asteroid in asteroids:
                ax = asteroid['x'] + offset_x
                ay = asteroid['y'] + offset_y
                screen.draw.filled_circle((ax, ay), asteroid_stages[asteroid['stage']]['r'], color=C_ASTEROID_FILL)
                screen.draw.circle((ax, ay), asteroid_stages[asteroid['stage']]['r'], color=asteroid['c'])

            # SHIP
            point_f = point_on_circle(ship_x+offset_x, ship_y+offset_y, PLAYER_R, ship_angle)
            point_1 = point_on_circle(ship_x+offset_x, ship_y+offset_y, PLAYER_R, ship_angle + 10)
            point_2 = point_on_circle(ship_x+offset_x, ship_y+offset_y, PLAYER_R, ship_angle - 10)
            screen.draw.filled_circle((ship_x+offset_x, ship_y+offset_y), PLAYER_R, color=C_PLAYER_FILL)
            screen.draw.line(point_f, point_1, color=C_PLAYER_STROKE)
            screen.draw.line(point_1, point_2, color=C_PLAYER_STROKE)
            screen.draw.line(point_2, point_f, color=C_PLAYER_STROKE)

            # # BULLETS
            # for  bullet in bullets:
            #     screen.draw.filled_circle((
            #         bullet['x'] + offset_x,
            #         bullet['y'] + offset_y
            #         ), 3, color=C_BULLET)


    # BULLETS
    for  bullet in bullets:
        screen.draw.filled_circle(( bullet['x'], bullet['y']), BULLET_RADIUS, color=C_BULLET)
        # screen.draw.filled_circle(( bullet['x'], bullet['y']), 3, color='red')

    # screen.draw.text(
    #     'ship_angle: ' + str((ship_angle/math.pi)*180) + '\n' +
    #     'ship_x: ' + str(ship_x) + '\n' +
    #     'ship_y: ' + str(ship_y) + '\n' +
    #     'ship_speed_x: ' + str(ship_speed_x) + '\n' +
    #     'ship_speed_y: ' + str(ship_speed_y),
    # (0, 0))

    # }}}

reset()
pgzrun.go()

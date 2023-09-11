import pgzrun
import random


def new_pipe_space_y():# {{{
    # global pipe_space_y
    # global pipe_x
    pipe_space_y_min = 54
    pipe_space_y = random.randint(pipe_space_y_min, playing_area_height - pipe_space_y_min)
    # pipe_x = playing_area_width
    return pipe_space_y

# }}}

WIDTH = 300
HEIGHT = 388

playing_area_width = WIDTH
playing_area_height = HEIGHT
pipe_space_height = 160
pipe_width = 54
bird_x = 62
bird_width = 30
bird_height = 25

bird_y = 200
bird_y_speed = 200
pipe_space_y_min = 54
pipe_x = playing_area_width
pipe_space_y = random.randint(pipe_space_y_min, playing_area_height - pipe_space_y_min)


def reset():# {{{
    global upcoming_pipe
    global pipe_1_x
    global pipe_2_x
    global pipe_1_x
    global pipe_1_space_y
    global pipe_2_x
    global pipe_2_space_y
    global bird_y
    global score
    score = 0
    upcoming_pipe = 1


    pipe_1_x = playing_area_width
    pipe_2_x = pipe_1_x + ((playing_area_width + pipe_width) / 2)
    pipe_1_x = playing_area_width
    pipe_1_space_y = new_pipe_space_y()
    pipe_2_x = playing_area_width + ((playing_area_width + pipe_width) / 2)
    pipe_2_space_y = new_pipe_space_y()
    bird_y = 200
# }}}
def update(dt):# {{{
    global upcoming_pipe
    global bird_y, bird_y_speed
    global pipe_width
    global pipe_1_x, pipe_2_x
    global pipe_1_space_y, pipe_2_space_y
    global score
    
    if (upcoming_pipe == 1 and bird_x > (pipe_1_x + pipe_width)):
        score += 1
        upcoming_pipe = 2
        print(str(upcoming_pipe))

    if upcoming_pipe == 2 and bird_x > (pipe_2_x + pipe_width):
        score += 1
        upcoming_pipe = 1
        print(str(upcoming_pipe))

    bird_y_speed += 516 * dt
    bird_y += bird_y_speed * dt
    
    def move_pipe(pipe_x, pipe_space_y):
        pipe_x -= 60 * dt

        if pipe_x + pipe_width < 0:
            pipe_x = playing_area_width
            pipe_space_y = new_pipe_space_y()

        return pipe_x, pipe_space_y
    pipe_1_x, pipe_1_space_y = move_pipe(pipe_1_x, pipe_1_space_y)
    pipe_2_x, pipe_2_space_y = move_pipe(pipe_2_x, pipe_2_space_y)

    
    def is_bird_colliding_with_the_pipe(pipe_x, pipe_space_y):
        bird_collide = (
            bird_x < pipe_x + pipe_width 
            and 
            bird_x + bird_width > pipe_x 
            and 
                (
                bird_y < pipe_space_y
                or
                bird_y + bird_height > pipe_space_y + pipe_space_height
            )
        )
        return bird_collide

    if (is_bird_colliding_with_the_pipe(pipe_1_x, pipe_1_space_y) 
        or 
        is_bird_colliding_with_the_pipe(pipe_2_x, pipe_2_space_y)
        or
        bird_y > playing_area_height
        ):
        reset()





# }}}
def draw():# {{{
    def draw_pipe(pipe_x, pipe_space_y):
        # Pipe
        screen.draw.filled_rect(
                Rect((pipe_x, 0), (pipe_width, pipe_space_y)),
                color=(94, 201, 72)
                )

        screen.draw.filled_rect(
                Rect((pipe_x, pipe_space_y + pipe_space_height), (pipe_width, playing_area_height - pipe_space_y - pipe_space_height)),
                color=(94, 201, 72)
                )
    
    screen.fill((0, 0, 0))

    # Background
    screen.draw.filled_rect(
            Rect((0, 0), (playing_area_width, playing_area_height)),
            color=(35, 92, 118)
            )

    draw_pipe(pipe_1_x, pipe_1_space_y)
    draw_pipe(pipe_2_x, pipe_2_space_y)

    # Bird
    screen.draw.filled_rect(
            Rect((bird_x, bird_y), (bird_width, bird_height)),
            color=(224, 214, 68)
            )

    screen.draw.text("%d" % score, (15, 15))
# }}}
def on_key_down():# {{{
    global bird_y_speed

    if bird_y > 0:
        bird_y_speed = -165
    # global pipe_1_space_y, pipe_2_space_y
    # pipe_1_space_y = new_pipe_space_y()
    # pipe_2_space_y = new_pipe_space_y()


# }}}

reset()
pgzrun.go()

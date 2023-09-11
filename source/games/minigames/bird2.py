import pgzrun
import random
from enum import Enum

# SETTINGS {{{
GAME_SPEED = 80
C_BACKGROUND = (35, 92, 118)
ARENA_W = 800
ARENA_H = 450
WIDTH = ARENA_W #+  150
HEIGHT = ARENA_H #+  500
GRAVITY = 200 # 200

BIRD_WIDTH = 30
BIRD_HEIGHT = 25
BIRD_Y = 200
BIRD_X = 62
BIRD_INITIAL_SPEED = 200
BIRS_FLAP = -100
C_BIRD = (224, 214, 68)

PIPE_WIDTH = 54
PIPE_GAP = 160
PIPE_MARGIN = 10
C_PIPE = (94, 201, 72)

BACKGROUND = [
    ("sky", 1),
    ("clouds_1", 0.1),
    ("clouds_2", 0.3),
    ("rocks_1", 0.3),
    ("clouds_4", 0.5),
    ("rocks_2", 0.6),
    ("clouds_3", 0.7),
]

# }}}
class Game(object): # {{{
    class Background(object): # {{{
        def __init__(self, background):# {{{
            self.layers = []
            for img, speed in background:
                self.layers.append(self.Background_layer(img, speed))
            # }}}
        def draw(self):# {{{
            for layer in self.layers: layer.draw()
    # }}}
        def update(self, dt):# {{{
            for layer in self.layers: layer.update(dt)
    # }}}
        class Background_layer(object): # {{{
            def __init__(self, img, speed): # {{{
                self.img = img
                self.speed = speed
                self.slides = [Actor(img, topleft=(0, 0))]
                # }}}
            def update(self, dt): # {{{
                if self.slides[-1].right <= ARENA_W:
                    self.slides.append(Actor(self.img, topleft=(ARENA_W, 0)))
                for slide in self.slides:
                    slide.x -= GAME_SPEED * self.speed * dt
                if self.slides[0].x < -1 * ARENA_W:
                    self.slides.pop(0)
                # }}}
            def draw(self): # {{{
                for slide in self.slides:
                    slide.draw()
                # }}}
            # }}}
        # }}}
    class Bird(object): # {{{
        class State(Enum):
            NORMAL = 1
            DANGER = 2
            FLAPPING = 3

        def __init__(self, img=None): # {{{
            if img: self.sprite = Actor(img)
            self.x = BIRD_X
            self.y = BIRD_Y
            self.width = BIRD_WIDTH
            self.height = BIRD_HEIGHT
            self.colour = C_BIRD
            self.speed = BIRD_INITIAL_SPEED
            self.state = self.State.NORMAL
        # }}}
        def draw(self): # {{{
            if self.state == self.State.NORMAL: self.sprite.image = "bird"
            elif self.state == self.State.DANGER: self.sprite.image = "bird_scared"
            if self.sprite:
                self.sprite.draw()
            else:
                screen.draw.filled_rect(Rect((self.x, self.y), (self.width, self.height)), color="#333330")
                screen.draw.filled_rect(Rect((self.x+1, self.y+1), (self.width-2, self.height-2)), color=self.colour)
    # }}}
        def update(self, dt): #{{{
            self.speed += GRAVITY * dt
            self.y += self.speed * dt
            self.sprite.left = self.x
            self.sprite.top = self.y
            # }}}
        # }}}
    class Pipe(object): # {{{
        def __init__(self): # {{{
            self.gap_start = random.randint(PIPE_MARGIN, (ARENA_H - PIPE_GAP + PIPE_MARGIN))
            self.x = ARENA_W
            self.width = PIPE_WIDTH
            self.scored = False
        # }}}
        def draw(self): # {{{
            screen.draw.filled_rect(
                    Rect((self.x, 0), (self.width, self.gap_start)),
                    color=C_PIPE
                    )

            screen.draw.filled_rect(
                    Rect((self.x, self.gap_start+PIPE_GAP), (self.width, ARENA_H-(self.gap_start+PIPE_GAP))),
                    color=C_PIPE
                    )
            # }}}
        def update(self, dt): # {{{
            self.x -= GAME_SPEED * dt
            # }}}
    # }}}
    def __init__(self):  # {{{
        self.background = self.Background(BACKGROUND)
        self.reset()
    # }}}
    def reset(self):# {{{
        self.pipes = []
        self.pipes.append(self.Pipe())
        self.bird = self.Bird("bird")
        self.gravity = GRAVITY
        self.score = 0
    # }}}
    def update(self, dt): # {{{
        self.background.update(dt)
        self.bird.update(dt)
        if self.bird.y > ARENA_H: self.reset()
        elif self.bird.y > ARENA_H - 150: self.bird.state = self.bird.State.DANGER
        else: self.bird.state = self.bird.State.NORMAL

        if ARENA_W - self.pipes[-1].x > random.randint(250, 320):
            self.pipes.append(self.Pipe())
        for pipe in self.pipes:
            pipe.update(dt)
            if pipe.x + pipe.width < self.bird.x and not pipe.scored:
                self.score += 1
                pipe.scored = True
                self.bird.state = self.bird.State.NORMAL
            if pipe.x-self.bird.width - 30 <= self.bird.x <= pipe.x + pipe.width + 30: 
                self.bird.state = self.bird.State.DANGER
            if pipe.x-self.bird.width <= self.bird.x <= pipe.x + pipe.width:
                if not (pipe.gap_start <= self.bird.y <= (pipe.gap_start + PIPE_GAP - self.bird.width)):
                    self.reset()
                    # pass
        if self.pipes[0].x < -1*PIPE_WIDTH:
            self.pipes.pop(0)



    # }}}
    def draw(self): # {{{
        screen.fill((0, 0, 0))
        screen.draw.filled_rect(Rect((0, 0), (ARENA_W, ARENA_H)), color=C_BACKGROUND)

        self.background.draw()

        for pipe in self.pipes:
            pipe.draw()
        self.bird.draw()
        screen.draw.text(
            "%d" % self.score, 
            topleft=(10, 10), 
            color=(250, 250, 250), 
            fontsize=40,
            owidth=0.4,
            ocolor="#b0b0b0",
            # shadow=(2, 2),
            # scolor="#202020"
            )
        # Actor("rocks_1").draw()
    # }}}
    def send_key(self, key):# {{{
        if key in [keys.A, keys.S]:
            if self.bird.y > 40:
                self.bird.speed = BIRS_FLAP
# }}}
    # }}}
# BOILERPLATE {{{
def on_key_down(key): game.send_key(key)
def update(dt): game.update(dt)
def draw(): game.draw() # }}}
game = Game()
pgzrun.go()

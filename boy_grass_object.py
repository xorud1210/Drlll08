from pico2d import *
import random


# Game object class here
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

    def update(self): pass


class Boy:
    def __init__(self):
        self.frame = 0
        self.image = load_image('run_animation.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class BigBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball41x41.png')
        self.speed = random.randint(10,20)

    def update(self):
        if self.y > 55 + 41 // 2:
            self.y -= self.speed
        else:
            self.y = 55 + 41 // 2

    def draw(self):
        self.image.draw(self.x, self.y, 41, 41)
class SmallBall:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 599
        self.image = load_image('ball21x21.png')
        self.speed = random.randint(10, 20)

    def update(self):
        if self.y > 55 + 21 // 2:
            self.y -= self.speed
        else:
            self.y = 55 + 21 // 2

    def draw(self):
        self.image.draw(self.x, self.y, 21, 21)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global balls
    global world

    running = True
    world = []

    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team
    balls = [BigBall() if random.randint(0,1) == 0 else SmallBall() for i in range(20)]
    world += balls

def update_world():
    for o in world:
        o.update()


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()  # game_logic
    render_world()  # draw game world
    delay(0.05)

# finalization code

close_canvas()

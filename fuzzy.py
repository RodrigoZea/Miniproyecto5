import random
import math
import matplotlib.pyplot as plt
import game_object
import fuzzy_logic
import pygame
from pygame.locals import(
    KEYDOWN,
    K_ESCAPE,
    QUIT
)
from constants import *

# pygame
pygame.init()
screen = pygame.display.set_mode([SCREEN_DIM, SCREEN_DIM])

# game objects
background = pygame.image.load("img/field.png")
ball = game_object.GameObject(sprite_path="img/ball.png")
ball.rot = 0.0
robot = game_object.GameObject(sprite_path="img/robot.bmp")
goal = pygame.Surface((GOAL_WIDTH, GOAL_HEIGHT))
goal.fill(C_BLACK)
message_font = pygame.font.SysFont(None, 30)

# game state
game_running = True
ball_shot = False

while game_running:
    # quit event, click or key
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                game_running = False

    # white screen    
    #screen.blit(background, (0, 0))
    screen.fill(C_WHITE)

    # fuzzy loop
    if not ball_shot:
        dist, angle = fuzzy_logic.fuzzy_loop(ball, robot)

    # the robot reaches the ball
    if not ball_shot and dist <= BALL_MIN_DIST:
        dist_font = pygame.font.SysFont(None, 30)
        dist_surf = dist_font.render('Robot reached the ball!', True, (C_BLACK))
        screen.blit(dist_surf, (5, 30))

        # direction to goal
        rnd_rot_dev = math.pi / 6.0 * random.random()
        if random.random() <= 0.5:
            rnd_rot_dev *= -1.0
        ball.set_dir(rad=(math.pi / 2.0 + rnd_rot_dev))
        ball.speed = BALL_SPEED
        ball_shot = True


    # ball bounces on wall
    if ball.pos.x < 60 or ball.pos.x > 740:
        ball.rotate(math.pi)
    if ball.pos.y < 60 or ball.pos.y > 740:
        ball.rotate(math.pi)

    # reduce ball speed and stop ball if necessary
    if ball_shot:
        ball.speed -= BALL_FRICTION
        ball.move(ball.speed)
        if ball.speed < 0.1:
            ball.speed = 0.0
            ball_shot = False

    # draw game objects
    screen.blit(ball.surf, (ball.pos.x, ball.pos.y))
    screen.blit(robot.surf, (robot.pos.x, robot.pos.y))
    screen.blit(goal, (SCREEN_DIM / 2 - GOAL_WIDTH / 2, SCREEN_DIM - GOAL_HEIGHT))

    # debug messages
    message_surf = message_font.render(f'Distance is {dist:.{3}f}', True, (C_BLACK))
    screen.blit(message_surf, (5, 5))

    pygame.display.flip()

pygame.quit()
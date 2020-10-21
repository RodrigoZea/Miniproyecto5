import math

# game
TIME_DELTA  = 1.0 / 30
MOVE_SLOW   = 1
MOVE_NORMAL = 5
MOVE_FAST   = 10
ROT_SLOW    = 0.0
ROT_NORMAL  = math.pi / 6.0 
ROT_FAST    = math.pi / 3.0
BALL_MIN_DIST = 5.0
BALL_SPEED = 75.0
BALL_FRICTION = 0.5

# pygame
SCREEN_DIM  = 800
C_WHITE = (255, 255, 255)
C_BLUE = (0, 0, 255)
C_BLACK = (0, 0, 0)
BALL_RADIUS = 10
GOAL_WIDTH = 100
GOAL_HEIGHT = 10

# math
MAX_DIST      = math.sqrt(SCREEN_DIM ** 2 + SCREEN_DIM ** 2)
HALF_MAX_DIST = MAX_DIST / 2.0
PI_2          = math.pi / 2.0
PI3_2         = 3.0 * math.pi / 2.0
PI_6          = math.pi / 6.0
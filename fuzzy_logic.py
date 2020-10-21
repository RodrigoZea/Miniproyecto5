from constants import *

# Membership functions for distance
def d_close(x):
    if x <= 2:
        return 1.0
    elif x > HALF_MAX_DIST:
        return 0.0
    return -0.197197430123091 * x + 1.39439486024618

def d_medium(x):
    if x <= HALF_MAX_DIST:
        return 0.141421512474792 * x
    return -0.141421312474633 * x + 1.99999858578688

def d_far(x):
    if x <= HALF_MAX_DIST:
        return 0.0
    elif x > SCREEN_DIM:
        return 1.0
    return 0.341420445621966 * x - 2.41420445621966

def a_close(x):
    if x <= PI_6:
        return 1.0
    elif x >= PI_2:
        return 0.0
    return -0.954929658365891 * x + 1.49999999990451

def a_medium(x):
    if x <= PI_2:
        return 0.636619772284456 * x
    return -0.636619772284456 * x + 2

def a_far(x):
    if x <= PI_2:
        return 0.0
    elif x >= PI3_2:
        return 1.0
    return 0.318309886243549 * x - 0.500000000159155

def fuzzy_loop(ball, robot):
    dist = robot.pos.distance(ball.pos)
    v2b = robot.pos.dir_to(ball.pos)
    angle = robot.dir.angle(v2b)

    # run through membership functions
    dist_f = [d_close(dist), d_medium(dist), d_far(dist)]
    rot_f = [a_close(angle), a_medium(angle), a_far(angle)]

    # inference rules
    rules = []
    # if distance is close and direction is close -> slow forward
    rules.append(min(dist_f[0], rot_f[0]))
    # if distance is close and direction is medium -> rotate normal and move slowly
    rules.append(min(dist_f[0], rot_f[1]))
    # if distance is close and direction is far off -> rotate hard and move slowly
    rules.append(min(dist_f[0], rot_f[2]))
    # if distance is medium and direction is close -> normal forward
    rules.append(min(dist_f[1], rot_f[0])) 
    # if distance is medium and direction is medium -> rotate normal and move normal
    rules.append(min(dist_f[1], rot_f[1]))
    # if distance is medium and direction is far off -> rotate hard and move normal
    rules.append(min(dist_f[1], rot_f[2]))
    # if distance is far and direction is close -> fast forward
    rules.append(min(dist_f[2], rot_f[0]))
    # if distance is far and direction is medium -> rotate normal and move fast
    rules.append(min(dist_f[2], rot_f[1]))
    # if distance is far and direction is far off -> rotate hard and move fast
    rules.append(min(dist_f[2], rot_f[2]))

    # maximum rule find index
    max_index = 0
    max_value = -1
    for i in range(len(rules)):
        if rules[i] > max_value:
            max_value = rules[i]
            max_index = i
    
    action = actions[max_index]
    robot.rotate(rad=action[1], clockwise=(robot.pos.y >= ball.pos.y))
    robot.move(speed=action[0])

    return dist, angle

"""
    Inference Rules 
    Distance/
    Direction |      close      |         medium         |            far              |
    -----------------------------------------------------------------------------------|
       close  |  slow forward   | rotate and move slowly | rotate hard and move slowly |  
    -----------------------------------------------------------------------------------|
       medium | normal forward  | rotate and move normal | rotate hard and move normal |
    -----------------------------------------------------------------------------------|
       far    | fast forward    | rotate and move fast   | rotate hard and move fast   |
    -----------------------------------------------------------------------------------|

    Movement and rotation speeds
    -------------------------------------------------------
    | Move Slow   | 0.5 u/s | No Rotate     |  0 degrees  |
    |-----------------------|---------------|-------------|
    | Move Normal | 1 u/s   | Rotate Normal |  20 degrees |
    ------------------------|---------------|-------------|
    | Move Fast   | 3 u/s   | Rotate Fast   |  60 degrees |
    |-----------------------|---------------|-------------|
"""
actions = [
    [MOVE_SLOW, ROT_SLOW], [MOVE_SLOW, ROT_NORMAL], [MOVE_SLOW, ROT_FAST],
    [MOVE_NORMAL, ROT_SLOW], [MOVE_NORMAL, ROT_NORMAL], [MOVE_NORMAL, ROT_FAST],
    [MOVE_FAST, ROT_SLOW], [MOVE_FAST, ROT_NORMAL], [MOVE_FAST, ROT_FAST]
]

debug_actions = [
    'slow forward', 'rotate normal and move slowly', 'rotate hard and move slowly',
    'normal forward', 'rotate normal and move normal', 'rotate hard and move normal',
    'fast forward', 'rotate normal and move fast', 'rotate hard and move fast'
]

action_history = {}
for action in debug_actions:
    action_history[action] = 0
'''
    config file to define global variables

    actually ran into some issues when I tried to import methods from functions.py here, the function init() used to be here.
    my guess is I caused some sort of circular importing error

    Kris 18/5/20 - 20/5/20 
'''
from graphics import *

# global WIDTH
# global HEIGHT
# global CYCLE
# global window
WIDTH = 1600 #1800    # width of window
HEIGHT = 800   # height of window
enemy_CYCLE = 400000    # time per cycle IN MICROSECONDS
            #or 20000 for speed boost
window = GraphWin('Space Invaders', WIDTH, HEIGHT) # give title and dimensions
window.setBackground("black")

#protagonist and their shots
PROTAGONIST_STARTING_x = WIDTH / 2
PROTAGONIST_STARTING_y = HEIGHT - 30
PROTAGONIST_SHIFT = 12                  # the amount the protagonist shifts by per keystroke
SHOT_LENGTH = 36                        # length of bullet shot
SHOT_COOLDOWN = 400000                 # cooldown between each shot IN MICROSECONDS
SHOT_MOVEMENT_COOLDOWN = 75000                  # time before shot moves
SHOT_SHIFT = 60
shots = []

#enemy
TOP_LEFT_enemy_x = 90            # starting positions of the top left enemy, since all the other enemies are just shifed certain widths from the top left enemy
TOP_LEFT_enemy_y = 78
GAP_BETWEEN_enemies = 150
enemy_SHIFT = 15                     # the amount a enemy shifts by when it moves
SHIFTS_PER_LEVEL = 7                  # number of times the enemies will shift until they change their height

#explosion
BOOM_DELAY = 100000


 ################################################################
### DUDE GET RID OF THE BOOLEAN VALUE FOR EXPLOSION AND DO
explosion_points = []
explosions = []
explosion_timings = []

### ONE LIST FOR LIST OF EXPLOSIONS
### ANOTHER LIST FOR TIMES datetime.now() to check C:

     ################################# NOTE: ############# READ###############



'''
    sexy config file to define global variables and shit

    actually ran into some issues when I tried to import methods from functions.py here, the function init() used to be here.
    my guess is I caused some sort of circular importing error, look into this when you can (reminder for myself)

    Kris 18/5/20 - 20/5/20 (yeah that's right it's a non-american date you fuckers)
'''
from graphics import *

# global WIDTH
# global HEIGHT
# global CYCLE
# global window
WIDTH = 1600 #1800    # width of window
HEIGHT = 800   # height of window
CUNT_CYCLE = 400000    # time per cycle IN MICROSECONDS
            #or 20000 for speed boost
window = GraphWin('Gaming XD', WIDTH, HEIGHT) # give title and dimensions
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

#cunt
TOP_LEFT_CUNT_x = 90            # starting positions of the top left cunt, since all the other cunts are just shifed certain widths from the top left cunt
TOP_LEFT_CUNT_y = 78
GAP_BETWEEN_CUNTS = 150
CUNT_SHIFT = 15                     # the amount a cunt shifts by when it moves
SHIFTS_PER_LEVEL = 7                  # number of times the cunts will shift until they change their height

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



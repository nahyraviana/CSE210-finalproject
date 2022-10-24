from game.casting.color import Color

# --------------------------------------------------------------------------------------------------
# GENERAL GAME CONSTANTS
# --------------------------------------------------------------------------------------------------

# GAME
GAME_NAME = "Pong"
FRAME_RATE = 60

# SCREEN
SCREEN_WIDTH = 1040
SCREEN_HEIGHT = 680
CENTER_X = SCREEN_WIDTH / 2
CENTER_Y = SCREEN_HEIGHT / 2

# FIELD
FIELD_TOP = 60
FIELD_BOTTOM = SCREEN_HEIGHT
FIELD_LEFT = 0
FIELD_RIGHT = SCREEN_WIDTH

# FONT
FONT_FILE = "pong/assets/fonts/game.otf"
FONT_SMALL = 20
FONT_LARGE = 30

# SOUND
BOUNCE_SOUND = "pong/assets/sounds/boing.wav"
WELCOME_SOUND = "pong/assets/sounds/start.wav"
OVER_SOUND = "pong/assets/sounds/over.wav"

# TEXT
ALIGN_CENTER = 0
ALIGN_LEFT = 1
ALIGN_RIGHT = 2

# COLORS
BLACK = Color(0, 0, 0)
WHITE = Color(255, 255, 255)
PURPLE = Color(255, 0, 255)

# KEYS
UP = "w","i"
DOWN = "s","k"
ENTER = "enter"


# SCENES
NEW_GAME = 0
TRY_AGAIN = 1
NEXT_LEVEL = 2
IN_PLAY = 3
GAME_OVER = 4



# -------------------------------------------------------------------------------------------------- 
# SCRIPTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# PHASES
INITIALIZE = 0
LOAD = 1
INPUT = 2
UPDATE = 3
OUTPUT = 4
UNLOAD = 5
RELEASE = 6

# -------------------------------------------------------------------------------------------------- 
# CASTING CONSTANTS
# -------------------------------------------------------------------------------------------------- 

# STATS
STATS_GROUP1 = "stat1"
STATS_GROUP2 = "stat2"

# HUD
HUD_MARGIN = 15
SCORE_GROUP = "score1","score2"
SCORE_FORMAT = "Player one:{}","PLAYER TWO: {}"

# BALL
BALL_GROUP = "balls"
BALL_IMAGE = "pong/assets/images/000.png"
BALL_WIDTH = 35
BALL_HEIGHT = 35
BALL_VELOCITY = 6

# RACKET
RACKET_GROUP = "racket1","racket2",
RACKET_IMAGES = {
    "l": ["pong/assets/images/100.png"],
    "r" : ["pong/assets/images/101.png"]
}
RACKET_WIDTH =  28
RACKET_HEIGHT =  125
RACKET_RATE = 6
RACKET_VELOCITY = 7

# DIALOG
DIALOG_GROUP = "dialogs"
ENTER_TO_START = "PRESS ENTER TO START"
PREP_TO_LAUNCH = "PREPARING TO LAUNCH"
WAS_GOOD_GAME = "GAME OVER!"
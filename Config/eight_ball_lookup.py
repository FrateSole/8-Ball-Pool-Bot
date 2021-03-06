'''Eight Ball Lookup Module'''

# Base Configurations

BASE_PATH = 'Config\\Images\\'
BALL_PATH = BASE_PATH + 'Balls\\'

MID_CONFIDENCE = 0.5
HIGH_CONFIDENCE = 0.7

BALL_RADIUS = 10
BALL_DIAMETER = BALL_RADIUS * 2.2

HOLE_RADIUS = 20
BORDER_DISTANCE = 15

MIDDLE_HOLE_RADIUS = int(BORDER_DISTANCE * 1.2)
CORNER_HOLE_RADIUS = int(BORDER_DISTANCE * 2.6)

MIDDLE_BORDER_RADIUS = int(BORDER_DISTANCE * 0.8)
CORNER_BORDER_RADIUS = int(BORDER_DISTANCE * 2.8)

# URL

URL = 'https://www.miniclip.com/games/8-ball-pool-multiplayer/en/focus/'

# Miniclip Image Checking

MODAL_WAIT = 30

BACK_BUTTON = BASE_PATH + 'BackButton.PNG'
CLOSE_BUTTON = BASE_PATH + 'CloseButton.PNG'
MENU_BUTTON = BASE_PATH + 'MenuButton.PNG'

# Output Path

TRAINING_FOLDER = 'Testing\\Examples\\'

HOLE_TRAINING_PATH = 'Parameters\\Holes\\'
BALL_TRAINING_PATH = 'Parameters\\Balls\\'

# Pop Up Text

MONITOR_ONE_TEXT = 'Make sure the web browser is opened on monitor one'

ALREADY_LOGGED_IN = 'User has already logged in'
SUCCESSFUL_LOGIN = 'You have successfully logged in'
ERROR_DURING_LOGIN = 'An error was encountered during log in'

ALREADY_OPENED_GAME = 'Game is already opened'

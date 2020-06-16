BAUDRATE = 115200
CMD_TURNING_2WD = "2wd"
CMD_RESETALARM = "reset"
CMD_STOP = "stop"
CMD_ROTATE = "rotate"

DELAY_TIME_STOP_MOTOR = 1.0
RUN_STOP = 0.0
TURNING_MAX = 90
TURNING_MIN = -90

SPEED_MIN = 0.5
SPEED_MEDIUM = 1.0
SPEED_MAX = 1.5

COMMAND_DRIVE = 0
COMMAND_STEERCURVE = 1
COMMAND_STEERPARA = 2
COMMAND_SPINSTEER = 4
COMMAND_TWOSTEERPARA = 5
COMMAND_ROTATE = 3
COMMAND_CHANGESPEED = 7
COMMAND_RELEASE = 8
COMMAND_RESETALARM = 9
COMMAND_NEW_CURVE = 'k'
COMMAND_ONE_WHEEL_CURVE = 'l'
COMMAND_NEW_SPEED = 'm'

# Direction constant
FORWARD = 'w'
LEFT = 'a'
RIGHT = 'd'
BACK = 's'
UPPER_LEFT = 'q'
UPPER_RIGHT = 'e'
LOWER_LEFT = 'z'
LOWER_RIGHT = 'c'
ROTATE_LEFT = 'm'
ROTATE_RIGHT = 'n'
FRONT_LEFT_MIN = 't'
FRONT_RIGHT_MIN = 'i'
FRONT_LEFT_MEDIUM = 'y'
FRONT_RIGHT_MEDIUM = 'u'
FRONT_LEFT_MAX = 'h'
FRONT_RIGHT_MAX = 'j'
STOP = 'x'
SLOW_TO_STOP = 'o'
SPEED_LEVEL_SLOW = 'r'
SPEED_LEVEL_MEDIUM = 'f'
SPEED_LEVEL_FAST = 'v'
RED_STOP = 'xx'

# NFC values
CODE_UNAVAILABLE = 'NONE'
CODE_STOP = 'STOP'
CODE_WAIT_DOOR = 'WAIT'
CODE_START_POINT = 'START'
CODE_A_POINT = 'A'
CODE_B_POINT = 'B'
CODE_C_POINT = 'C'
CODE_D_POINT = 'D'
CODE_E_POINT = 'E'
CODE_F_POINT = 'F'
CODE_ROTATE_LEFT = 'ROTATELEFT'
CODE_ROTATE_RIGHT = 'ROTATERIGHT'
CODE_GO_LEFT = 'GOLEFT'
CODE_GO_RIGHT = 'GORIGHT'
CODE_NAV_MODE = 'CMD_NAV'
CODE_NAV_TRANSFORM = 'CMD_NAV_TRANS'
CODE_LINE_TRACE_MODE = 'CMD_LINE'

# value for open door
IR_OPEN_DOOR = 'o'
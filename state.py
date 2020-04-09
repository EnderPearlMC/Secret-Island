from enum import Enum


# Enum which contains the game state
class State(Enum):
    # Shows the main menu
    MAIN_MENU = 0
    # Shows the second menu
    SECOND_MENU = 1

    ##########################
    #      HISTORY MODE      #
    ##########################

    # Shows help to explain the game
    HISTORY_MODE_START_HELP = 3

    # Shows the main map
    HISTORY_MODE_MAIN_MAP = 4

    # Shows the current region's menu
    HISTORY_MODE_REGION_MENU = 5

    # Shows the current region's city
    HISTORY_MODE_REGION_CITY = 6

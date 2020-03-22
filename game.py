from menus.historyMode.HMHelp1Menu import HMHelp1Menu
from menus.mainMenu import MainMenu
from menus.secondMenu import SecondMenu
from state import State
from gameData import GameData
from entities.playerEntity import PlayerEntity
import os
import pygame


# class which instance everything of the game and main systems
class Game:

    # construct method
    # @params screen : screen variable stored in main.py
    def __init__(self, screen):
        # main_menu | Stores MainMenu class
        self.main_menu = MainMenu(self)
        # second_menu | Stores SecondMenu class
        self.second_menu = SecondMenu(self)
        # state | Stores game state
        self.state = State.MAIN_MENU
        # game_data | Stores GameData class
        self.game_data = GameData()
        # player | Stores the main player
        self.player = PlayerEntity(self)
        self.player.rect.x = 600
        self.player.rect.y = 600
        # key_pressed | Stores keys and if they are pressed
        self.keys_pressed = {}

        ##########################
        #      HISTORY MODE      #
        ##########################

        # hm_help1_menu | Stores the first help of history mode
        self.hm_help1_menu = HMHelp1Menu(self)

    # updates everything of the game
    # @params screen : screen variable stored in main.py to get size of the window
    def update(self, screen):
        if self.state == State.MAIN_MENU:
            self.main_menu.update(screen, self)
        if self.state == State.SECOND_MENU:
            self.second_menu.update(screen, self)

        ##########################
        #      HISTORY MODE      #
        ##########################

        if self.state == State.HISTORY_MODE_START_HELP:
            self.hm_help1_menu.update(screen, self)

        if os.path.exists('files/player.yaml'):
            self.game_data.data_player = self.game_data.get_player_file_data()

        self.game_data.make_datas_as_file()

    # updates everything of the game when video resize
    # @params screen : screen variable stored in main.py to get size of the window
    # @param blocks_size : The size of the blocks
    def update_video_resize(self, screen, blocks_size):
        if self.state == State.SECOND_MENU:
            pass

    # updates the player
    def update_player(self):
        self.player.update()
        if self.keys_pressed.get(97):
            self.player.reset_velocity()
            self.player.change_velocity(-3, -1.5)
        elif self.keys_pressed.get(100):
            self.player.reset_velocity()
            self.player.change_velocity(3, 1.5)
        elif self.keys_pressed.get(119):
            self.player.reset_velocity()
            self.player.change_velocity(1.5, -3)
        elif self.keys_pressed.get(115):
            self.player.reset_velocity()
            self.player.change_velocity(-1.5, 3)
        else:
            self.player.reset_velocity()
        self.player.game = self

    def play_file(self, path):
        pygame.mixer.init()
        pygame.mixer.music.load(path)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.4)
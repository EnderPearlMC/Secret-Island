from menus.historyMode.HMHelp1Menu import HMHelp1Menu
from menus.historyMode.HMMainMap import HMMainMap
from menus.mainMenu import MainMenu
from menus.secondMenu import SecondMenu
from state import State
from gameData import GameData
from entities.playerEntity import PlayerEntity
from regions.regionManager import RegionManager
from regions.regionPlains1 import RegionPlains1
from regions.regionMountains1 import RegionMountains1
from regions.regionMountains2 import RegionMountains2
import os
import pygame


# class which instances everything of the game and main systems
class Game:

    # construct method
    # @params screen : screen variable stored in main.py
    # @params screen : game_infos variable stored in main.py
    def __init__(self, screen, game_infos):

        self.game_infos = game_infos

        self.deltaTime = 0

        # main_menu | Stores MainMenu class
        self.main_menu = MainMenu(self)
        # second_menu | Stores SecondMenu class
        self.second_menu = SecondMenu(self)
        # state | Stores game state
        if self.game_infos['start_mode'] == "release":
            self.state = State.MAIN_MENU
        elif self.game_infos['start_mode'] == "debug" or self.game_infos['start_mode'] == "debug-music":
            self.state = self.game_infos['start_point']
        # game_data | Stores GameData class
        self.game_data = GameData()
        # player | Stores the main player
        self.player = PlayerEntity()
        # key_pressed | Stores keys and if they are pressed
        self.keys_pressed = {}

        self.font = pygame.font.SysFont("Arial", 20)

        # version_text | Stores version text
        self.version_text = self.font.render(self.game_infos["version"], True, (255, 255, 255))

        ##########################
        #      HISTORY MODE      #
        ##########################

        # hm_help1_menu | Stores the first help of history mode
        self.hm_help1_menu = HMHelp1Menu(self)

        # hm_main_map | Stores the main map of the history mode
        self.hm_main_map = HMMainMap(self)

        # region_manager | Stores the region manager
        self.region_manager = RegionManager()

        self.add_regions()

    def play_file(self, path):
        if self.game_infos['start_mode'] == "release" or self.game_infos['start_mode'] == "debug-music":
            pygame.mixer.init()
            pygame.mixer.music.load(path)
            pygame.mixer.music.play()
            pygame.mixer.music.set_volume(0.4)

    # adds the regions of the history mode
    def add_regions(self):

        self.region_manager.add_region(RegionPlains1())
        self.region_manager.add_region(RegionMountains1())
        self.region_manager.add_region(RegionMountains2())
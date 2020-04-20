import random

import pygame


# class which stores every part of the Main Menu and all systems of it
class MainMenu:

    # construct method
    def __init__(self, game):

        # font | Main font
        self.font = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 35)
        # font2 | Second font
        self.font2 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 45)
        # font3 | Third font
        self.font3 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 70)
        # font4 | 4th font
        self.font4 = pygame.font.SysFont("Arial", 20)

        # play music
        pygame.mixer.music.stop()
        game.play_file("assets/musics/music1.mp3")

        # add menu's elements
        self.add_elements()

    # add elements of the menu
    def add_elements(self):
        # background | Stores background image
        self.background = pygame.image.load("assets/images/mainMenu/background.jpg")
        self.sun = pygame.image.load("assets/images/sunlight.png")
        # title | Stores title text
        self.title = self.font3.render("GAME", True, (46, 204, 113))
        # play_button | Stores play button image
        self.play_button = pygame.image.load("assets/images/button.png")
        # play_button_rect | Stores play button rect
        self.play_button_rect = self.play_button.get_rect()
        # play_button_text | Stores play button text
        self.play_button_text = self.font2.render("PLAY", True, (255, 255, 255))
        # coin_amount_text | Stores coin amount text
        self.coin_amount_text = self.font.render("", True, (255, 255, 255))
        # coin | Stores coin image
        self.coin = pygame.image.load("assets/images/mainMenu/coin.png")
        # buy_coins_text | Stores buy coins text
        self.buy_coins_text = self.font2.render("+", True, (255, 255, 255))
        # pseudo_text | Stores pseudo text
        self.pseudo_text = self.font.render("", True, (255, 255, 255))
        # level_text | Stores level text
        self.level_text = self.font2.render("", True, (255, 255, 255))
        # settings_button | Stores settings button image
        self.settings_button = pygame.image.load("assets/images/button.png")
        # settings_button_rect | Stores settings button's rect
        self.settings_button_rect = self.settings_button.get_rect()
        # settings_button_text | Stores settings button text
        self.settings_button_text = self.font.render("SETTINGS", True, (255, 255, 255))
        # pseudo_text | Stores pseudo text
        self.loading_text = self.font.render("Loading...", True, (46, 204, 113))

    # @params screen : screen variable stored in main.py to get size of the window
    # @params game : screen variable stored in main.py to get game instance
    def update(self, screen, game):

        # render title text
        self.title = self.font3.render("SECRET ISLAND", True, (46, 204, 113))
        # render coin amount text
        self.coin_amount_text = self.font.render(str(game.game_data.data_player["money"]), True, (255, 255, 255))
        # render coin amount text
        self.buy_coins_text = self.font.render("+", True, (46, 204, 113))
        # render pseudo text
        self.pseudo_text = self.font.render(game.game_data.data_player["name"], True, (255, 255, 255))
        # render level text
        self.level_text = self.font2.render("Level " + str(game.game_data.data_player["level"]), True, (225, 255, 255))

        # reload background image
        self.background = pygame.image.load("assets/images/mainMenu/background.jpg")
        self.sun = pygame.image.load("assets/images/sunlight.png")
        # set the size of it
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))
        self.sun = pygame.transform.scale(self.sun, (screen.get_width(), screen.get_height()))

        # render play button text
        self.play_button_text = self.font2.render("PLAY", True, (255, 255, 255))

        # reload coin image
        self.coin = pygame.image.load("assets/images/mainMenu/coin.png")
        # set the size of it
        self.coin = pygame.transform.scale(self.coin, (50, 50))

        # render menu button text
        self.settings_button_text = self.font.render("SETTINGS", True, (255, 255, 255))

        # render loading text
        self.loading_text = self.font.render("Loading...", True, (255, 255, 255))

    # detects if play button is clicked
    def is_play_button_pressed(self, pos):
        # if button clicked
        if self.play_button_rect.collidepoint(pos):
            return True
        else:
            return False

    def hover(self, pos, screen):
        # if play button hovered
        if self.play_button_rect.collidepoint(pos):
            # reload play button image
            self.play_button = pygame.image.load("assets/images/buttonPressed.png")
            # set the size of it
            self.play_button = pygame.transform.scale(self.play_button,
                                                      (int(screen.get_width() / 3.5), int(screen.get_height() / 5)))
            # get rect of play button
            self.play_button_rect = self.play_button.get_rect()
            # set pos
            self.play_button_rect.x = int(screen.get_width() / 2 - self.play_button.get_width() / 2)
            self.play_button_rect.y = int(screen.get_height() - screen.get_height() / 5)
        else:
            # reload play button image
            self.play_button = pygame.image.load("assets/images/button.png")
            # set the size of it
            self.play_button = pygame.transform.scale(self.play_button,
                                                      (int(screen.get_width() / 3.5), int(screen.get_height() / 5)))
            # get rect of play button
            self.play_button_rect = self.play_button.get_rect()
            # set pos
            self.play_button_rect.x = int(screen.get_width() / 2 - self.play_button.get_width() / 2)
            self.play_button_rect.y = int(screen.get_height() - screen.get_height() / 5)

        if self.settings_button_rect.collidepoint(pos):
            # reload menu button image
            self.settings_button = pygame.image.load("assets/images/buttonPressed.png")
            # set the size of it
            self.settings_button = pygame.transform.scale(self.settings_button, (270, 80))
            # get its rect
            self.settings_button_rect = self.settings_button.get_rect()
            self.settings_button_rect.x = 7
            self.settings_button_rect.y = 10
        else:
            # reload menu button image
            self.settings_button = pygame.image.load("assets/images/button.png")
            # set the size of it
            self.settings_button = pygame.transform.scale(self.settings_button, (270, 80))
            # get its rect
            self.settings_button_rect = self.settings_button.get_rect()
            self.settings_button_rect.x = 7
            self.settings_button_rect.y = 10

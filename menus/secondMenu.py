import pygame


# class which stores every part of the Second Menu and all systems of it
class SecondMenu:

    # construct method
    def __init__(self, game):

        self.game = game

        # font | Main font
        self.font = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 35)
        # font2 | Second font
        self.font2 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 45)
        # font3 | Third font
        self.font3 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 70)
        # font4 | 4th font
        self.font4 = pygame.font.SysFont("Arial", 20)

        ################################
        #             CARDS            #
        ################################
        self.history_mode_card = {}

        # add menu's elements
        self.add_elements()

    # executed once menu started
    def init(self):
        # play music
        pygame.mixer.music.stop()
        self.game.play_file("assets/musics/music1.mp3")

    # add elements of the menu
    def add_elements(self):
        # background | Stores background image
        self.background = pygame.image.load("assets/images/secondMenu/secondMenuBackground.jpg")
        # version_text | Stores version text
        self.version_text = self.font4.render("Version alpha 0.0.1", True, (255, 255, 255))
        # select_text | Stores select text
        self.select_text = self.font3.render("Select where you wanna go", True, (255, 255, 255))

        ################################
        #           FILL CARDS         #
        ################################
        self.card1 = pygame.image.load('assets/images/card.png')

    # @params screen : screen variable stored in main.py to get size of the window
    # @params game : screen variable stored in main.py to get game instance
    def update(self, screen, game):
        # reload background image
        self.background = pygame.image.load("assets/images/secondMenu/secondMenuBackground.jpg")
        # set the size of it
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))
        # render version text
        self.version_text = self.font4.render("Version alpha 0.0.1", True, (255, 255, 255))
        # render select text
        self.select_text = self.font2.render("Select where you wanna go", True, (255, 255, 255))

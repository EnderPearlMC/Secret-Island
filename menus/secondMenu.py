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
        self.current_card = self.history_mode_card

    # executed once menu started
    def init(self, screen):
        # play music
        pygame.mixer.music.stop()
        self.game.play_file("assets/musics/music1.mp3")
        self.add_elements(screen)

    # add elements of the menu
    def add_elements(self, screen):
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
        self.card1 = pygame.transform.scale(self.card1, (int(screen.get_width() / 4.2), int(screen.get_height() / 2)))
        self.card1_rect = self.card1.get_rect()
        self.card1_image = pygame.image.load('assets/images/secondMenu/cards/temple.jpg')
        self.card1_image_rect = self.card1_image.get_rect()
        self.card1_button = pygame.image.load('assets/images/button.png')
        self.card1_button = pygame.transform.scale(self.card1_button,
                                                   (int(self.card1.get_width() - 20), int(self.card1.get_height() / 4)))
        self.card1_button_rect = self.card1_button.get_rect()
        self.card1_button_text = self.font.render("HISTORY MODE", True, (255, 255, 255))
        self.card1_button_text_rect = self.card1_button_text.get_rect()
        self.history_mode_card[0] = {self.card1: self.card1_rect}
        self.history_mode_card[1] = {self.card1_image: self.card1_image_rect}
        self.history_mode_card[2] = {self.card1_button: self.card1_button_rect}
        self.history_mode_card[3] = {self.card1_button_text: self.card1_button_text_rect}

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

        ################################
        #          UPDATE CARDS        #
        ################################
        self.card1 = pygame.image.load('assets/images/card.png')
        self.card1 = pygame.transform.scale(self.card1, (int(screen.get_width() / 4.2), int(screen.get_height() / 2)))
        self.card1_rect = self.card1.get_rect()
        self.card1_image = pygame.image.load('assets/images/secondMenu/cards/temple.jpg')
        self.card1_image = pygame.transform.scale(self.card1_image,
                                                  (int(self.card1.get_width()), int((self.card1.get_height() / 2.3))))
        self.card1_image_rect = self.card1_image.get_rect()
        self.card1_button_text = self.font.render("HISTORY MODE", True, (255, 255, 255))
        self.card1_button_text = pygame.transform.scale(self.card1_button_text, (
        int(self.card1_button.get_width() - 80), int(self.card1_button.get_height() - 20)))
        self.card1_button_text_rect = self.card1_button_text.get_rect()
        self.history_mode_card[0] = {self.card1: self.card1_rect}
        self.history_mode_card[1] = {self.card1_image: self.card1_image_rect}
        self.history_mode_card[3] = {self.card1_button_text: self.card1_button_text_rect}

        for key, val in self.current_card.items():
            for surface, rect in val.items():
                if surface == self.card1_image:
                    rect.x = screen.get_width() / 2.5
                    rect.y = (screen.get_height() / 3.5) + 25
                elif surface == self.card1_button:
                    rect.x = self.card1_rect.x + 10
                    rect.y = self.card1_rect.y + self.card1.get_width() / 1.5
                elif surface == self.card1_button_text:
                    rect.x = self.card1_button_rect.x + 40
                    rect.y = self.card1_button_rect.y + 10
                else:
                    rect.x = screen.get_width() / 2.5
                    rect.y = screen.get_height() / 3.5

    # detects if history mode button is clicked
    def is_history_mode_button_pressed(self, pos):
        print(self.card1_button_rect.x, self.card1_button_rect.y)
        # if button clicked
        for key, val in self.current_card.items():
            for surface, rect in val.items():
                if rect == self.card1_button_rect:
                    if rect.collidepoint(pos):
                        return True
                    else:
                        return False

    def hover(self, pos, screen):
        # hover card1 button
        if self.card1_button_rect.collidepoint(pos):
            self.card1_button = pygame.image.load('assets/images/buttonPressed.png')
            self.card1_button = pygame.transform.scale(self.card1_button, (
                int(self.card1.get_width() - 20), int(self.card1.get_height() / 4)))
            self.card1_button_rect = self.card1_button.get_rect()
            self.history_mode_card[2] = {self.card1_button: self.card1_button_rect}
        else:
            self.card1_button = pygame.image.load('assets/images/button.png')
            self.card1_button = pygame.transform.scale(self.card1_button, (
                int(self.card1.get_width() - 20), int(self.card1.get_height() / 4)))
            self.card1_button_rect = self.card1_button.get_rect()
            self.history_mode_card[2] = {self.card1_button: self.card1_button_rect}

import pygame


# class which creates a popup
class Popup:

    # construct method
    # @param title : The title of the popup
    # @param text : The text of the popup (List of line)
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.is_closed = False

        # font | Main font
        self.font = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 35)
        # font2 | Second font
        self.font2 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 25)
        # font3 | Third font
        self.font3 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 70)
        # font4 | 4th font
        self.font4 = pygame.font.SysFont("Arial", 20)

        # description_texts | Stores description lines
        self.description_texts = []

        self.load()

    # loads all the compoenents of the popup
    def load(self):

        # load
        self.background = pygame.image.load('assets/images/popup.png')
        self.title_text = self.font.render(self.title, True, (255, 255, 255))

        self.font2.set_underline(True)
        self.continue_text = self.font2.render("Continue", True, (9, 132, 227))
        self.continue_text_rect = self.continue_text.get_rect()

        for t in self.text:
            d = self.font2.render(t, True, (255, 255, 255))
            self.description_texts.append(d)
                

    # draws the popup
    # @param screen : The surface where the popup will be drawn
    def draw_popup(self, screen):
        
        if not self.is_closed:

            self.font2.set_underline(False)

            self.background = pygame.image.load('assets/images/popup.png')
            self.background = pygame.transform.scale(self.background, (int(screen.get_width() / 2.5), int(screen.get_height() / 2)))

            self.continue_text_rect.x = screen.get_width() / 2 - self.background.get_width() / 2.5
            self.continue_text_rect.y = screen.get_height() / 2 + self.background.get_height() / 3.5

            self.description_texts.clear()
            for t in self.text:
                d = self.font2.render(t, True, (255, 255, 255))
                self.description_texts.append(d)
            for d in range(0, len(self.description_texts)):
                self.description_texts[d] = pygame.transform.scale(self.description_texts[d], (self.background.get_width() - 100, 30))

            # draw
            screen.blit(self.background, (screen.get_width() / 2 - self.background.get_width() / 2, screen.get_height() / 2 - self.background.get_height() / 2))
            screen.blit(self.title_text, (screen.get_width() / 2 - self.background.get_width() / 2.5, screen.get_height() / 2 - self.background.get_height() / 2.5))

            for idx, val in enumerate(self.description_texts):
                screen.blit(val, (screen.get_width() / 2 - self.background.get_width() / 2.5, idx * 30 + screen.get_height() / 2 - self.background.get_height() / 4))

            screen.blit(self.continue_text, (screen.get_width() / 2 - self.background.get_width() / 2.5,
                                          screen.get_height() / 2 + self.background.get_height() / 3.5))

    def click(self, e):
        if e.button == 1:
            if self.continue_text_rect.collidepoint(pygame.mouse.get_pos()):
                self.is_closed = True
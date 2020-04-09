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
        self.title_text = self.font.render(self.title, True, (46, 204, 113))

        for t in self.text:
            d = self.font2.render(t, True, (0, 0, 0))
            self.description_texts.append(d)
                

    # draws the popup
    # @param screen : The surface where the popup will be drawn
    def draw_popup(self, screen):
        
        if not self.is_closed:

            # draw
            pygame.draw.rect(screen, (255, 255, 255), (0, 0, 400, 300))
            screen.blit(self.title_text, (10, 10))

            for idx, val in enumerate(self.description_texts):
                screen.blit(val, (10, idx * 30 + 50))
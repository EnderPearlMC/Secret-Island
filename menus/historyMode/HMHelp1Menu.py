import pygame


# class which stores every part of the Help menu 1 in history mode and all systems of it
class HMHelp1Menu:

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

        # add menu's elements
        self.add_elements()

        # p_order | Stores the order of the paragraphs
        self.p_order = [self.p1, self.p2, self.p3, self.p4, self.p5, self.p6, self.p7, self.p8]

        # current_paragraph | Stores the current paragraph which is shown
        self.current_paragraph = 0

    # add elements of the menu
    def add_elements(self):
        # background | Stores background image
        self.background = pygame.image.load("assets/images/historyMode/help1Background.jpg")
        # title | Stores title text
        self.title = self.font3.render("Welcome!", True, (255, 255, 255))
        # next_p_text | Stores the text to say to the user "press enter to continue"
        self.next_p_text = self.font.render("Press Enter to continue!", True, (238, 82, 83))

        """
            Paragraphs
        """
        self.p1 = self.font2.render("You'll play a character who lives...", True, (238, 82, 83))
        self.p2 = self.font2.render("...on an island.", True, (238, 82, 83))
        self.p3 = self.font2.render("This island contains many regions...", True, (238, 82, 83))
        self.p4 = self.font2.render("...where you could build, fight...", True, (238, 82, 83))
        self.p5 = self.font2.render("with peoples. Someone (you don't know)...", True, (238, 82, 83))
        self.p6 = self.font2.render("...asked you to explore this island...", True, (238, 82, 83))
        self.p7 = self.font2.render("...to see what is there.", True, (238, 82, 83))
        self.p8 = self.font2.render("Are you ready?", True, (238, 82, 83))

    # @params screen : screen variable stored in main.py to get size of the window
    # @params game : screen variable stored in main.py to get game instance
    def update(self, screen, game):
        # reload background image
        self.background = pygame.image.load("assets/images/historyMode/help1Background.jpg")
        # set the size of it
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))
        # render title
        self.title = self.font3.render("Welcome !", True, (255, 255, 255))

        """
            Paragraphs
        """
        self.p1 = self.font2.render("You'll play a character who lives...", True, (238, 82, 83))
        self.p2 = self.font2.render("...in Japan.", True, (238, 82, 83))
        self.p3 = self.font2.render("This land contain cities where...", True, (238, 82, 83))
        self.p4 = self.font2.render("...you could build, fight with peoples...", True, (238, 82, 83))
        self.p5 = self.font2.render("Someone (you don't know) asked...", True, (238, 82, 83))
        self.p6 = self.font2.render("...you to explore this land...", True, (238, 82, 83))
        self.p7 = self.font2.render("...to see what is there.", True, (238, 82, 83))
        self.p8 = self.font2.render("Are you ready?", True, (238, 82, 83))


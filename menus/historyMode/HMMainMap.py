import pygame


# class which stores all components of the main map and all systems of it
class HMMainMap:

    # construct method
    # @params game : screen variable stored in main.py to get game instance
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

        # regions | Stores every region of the map with its informations
        self.regions = [
            {
                "id": 1,
                "name": "Plains",
                "description": [
                    "The first region !",
                    "Just an infinite plain.",
                    "You can find trees",
                    "Only if you're lucky"
                ],
                "unlocked": False,
                "image": None,
                "rect": None
            },
            {
                "id": 2,
                "name": "Mountains",
                "description": [
                    "Can you climb it ?",
                    "Improve your climbing",
                    "skills !"
                ],
                "unlocked": False,
                "image": None,
                "rect": None
            },
            {
                "id": 3,
                "name": "Mountains 2",
                "description": [
                    "Once again !",
                    "Let's see if",
                    "you can still",
                    "climb !"
                ],
                "unlocked": False,
                "image": None,
                "rect": None
            }
        ]

        # descriptions | Stores a list which contains every paragraph of the description of a region
        self.descriptions = []
        # description_shown | True : the description is shown / False : the description is not shown anymore
        self.description_shown = False
        # locked_shown | True : It's written that the region is locked
        self.locked_shown = False
        # cross | Stores cross image
        self.cross = pygame.transform.scale(pygame.image.load('assets/images/cross.png'), (40, 40))

        # locked_text | Stores locked text
        self.locked_text = self.font.render("This region is locked !", True, (192, 57, 43))

        # go_button_text | Stores go button
        self.go_button = pygame.transform.scale(pygame.image.load('assets/images/button.png'), (100, 60))
        self.go_button_rect = self.go_button.get_rect()
        # go_button_text | Stores go button text
        self.go_button_text = self.font.render("GO", True, (255, 255, 255))

        # selected_region | Selected region
        self.selected_region = None

        if self.game.game_infos['start_mode'] == "debug-music":
            self.init()

        # add menu's elements
        self.add_elements()

    # executed once menu started
    def init(self):
        # play music
        pygame.mixer.music.stop()
        self.game.play_file("assets/musics/nature.mp3")

    # add elements of the menu
    def add_elements(self):
        # background | Stores background image
        self.background = pygame.image.load('assets/images/historyMode/mainMap.png')

    # @params screen : screen variable stored in main.py to get size of the window
    # @params game : screen variable stored in main.py to get game instance
    def update(self, screen, game):

        # REGIONS
        # for every region
        for r in self.regions:

            # set if it is unlocked
            if r['id'] <= game.game_data.data_player['history_mode']['region']['current_region']:
                r['unlocked'] = True

            if r['unlocked']:
                r['image'] = pygame.image.load('assets/images/unlocked.png')
                r['image'] = pygame.transform.scale(r['image'], (50, 50))
            else:
                r['image'] = pygame.image.load('assets/images/lock.png')
                r['image'] = pygame.transform.scale(r['image'], (50, 50))

            r['rect'] = r['image'].get_rect()

            # set size
            if r['id'] == 1:
                r['rect'].x = screen.get_width() / 2.9
                r['rect'].y = screen.get_height() / 1.2
            elif r['id'] == 2:
                r['rect'].x = screen.get_width() / 4.2
                r['rect'].y = screen.get_height() / 1.4
            elif r['id'] == 3:
                r['rect'].x = screen.get_width() / 3.4
                r['rect'].y = screen.get_height() / 1.7

        # reload background image
        self.background = pygame.image.load('assets/images/historyMode/mainMap.png')
        # set the size of it
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))

        # reload cross image
        self.cross = pygame.transform.scale(pygame.image.load('assets/images/cross.png'), (40, 40))

        self.cross_rect = self.cross.get_rect()

        if self.description_shown:
            self.cross_rect.x = screen.get_width() / 2 - self.cross.get_width() / 2
            self.cross_rect.y = len(self.descriptions) * 50 + (screen.get_height() / 2.5 - self.cross.get_height())

            self.go_button_rect.x = screen.get_width() / 2 - self.go_button.get_width() / 2
            self.go_button_rect.y = (screen.get_height() / 2.5 - self.go_button.get_height()) - 60

        elif self.locked_shown:
            self.cross_rect.x = screen.get_width() / 2 - self.cross.get_width() / 2
            self.cross_rect.y = 50 + (screen.get_height() / 2 - self.cross.get_height())

    # When click
    # @param pos : the position of the mouse
    def on_click(self, pos):

        for r in self.regions:
            if r['unlocked']:
                if r['rect'].collidepoint(pos):
                    self.selected_region = None
                    self.description_shown = False
                    self.show_description(r)
            else:
                if r['rect'].collidepoint(pos):
                    self.selected_region = None
                    self.description_shown = False
                    self.locked_shown = True

        # verify if cross clicked
        if self.description_shown:
            if self.cross_rect.collidepoint(pos):
                self.description_shown = False
        if self.locked_shown:
            if self.cross_rect.collidepoint(pos):
                self.locked_shown = False

    # shows the description of a region and draw a go button
    # @param region : The region that will be used
    def show_description(self, region):
        self.selected_region = region['id']
        self.locked_shown = False
        if not self.description_shown:
            self.descriptions.clear()
            self.descriptions.append(self.font2.render(region['name'], True, (46, 204, 113)))
            for p in region['description']:
                des = self.font.render(p, True, (255, 255, 255))
                self.descriptions.append(des)
            self.description_shown = True

    # return which region go button is clicked
    # @param pos : the position of the mouse
    def is_go_button_clicked(self, pos):

        return self.go_button_rect.collidepoint(pos)

    # When hovered
    # @param pos : the position of the mouse
    def hover(self, pos):

        if self.go_button_rect.collidepoint(pos):
            self.go_button = pygame.transform.scale(pygame.image.load('assets/images/buttonPressed.png'), (100, 60))
            self.go_button_rect = self.go_button.get_rect()
        else:
            self.go_button = pygame.transform.scale(pygame.image.load('assets/images/button.png'), (100, 60))
            self.go_button_rect = self.go_button.get_rect()

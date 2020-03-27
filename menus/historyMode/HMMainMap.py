import pygame


# class which stores all components of the main map and all systems of it
class HMMainMap:

    # construct method
    # @params game : screen variable stored in main.py to get game instance
    def __init__(self):
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

        # add menu's elements
        self.add_elements()

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

        # background | Stores background image
        self.background = pygame.image.load('assets/images/historyMode/mainMap.png')
        # set the size of it
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))

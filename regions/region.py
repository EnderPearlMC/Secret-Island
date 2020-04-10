import abc
import pygame
from state import State


# class which owns every system of a region
class Region():

    __metaclass__ = abc.ABCMeta

    # ABSTRACT METHODS
    
    @abc.abstractmethod
    def id(self):
        """
            Must return the id of the region (int)
        """
        raise NotImplementedError('You must implement this method')
    
    @abc.abstractmethod
    def name(self):
        """
            Must return the name of the region (string)
        """
        raise NotImplementedError('You must implement this method')

    @abc.abstractmethod
    def yaml_name(self):
        """
            Must return the name of the yaml path of the region (string)
        """
        raise NotImplementedError('You must implement this method')
    
    @abc.abstractmethod
    def description(self):
        """
            Must return the description of the region (List)
        """
        raise NotImplementedError('You must implement this method')

    @abc.abstractmethod
    def menu_settings(self):
        """
            Must return the settings of the region menu (Dictionnary)

            {
                "background-path": string
            }

        """
        raise NotImplementedError('You must implement this method')

    @abc.abstractmethod
    def quests(self):
        """ 
            Must return the quests of the region menu (List of dictionnaries)

            [
                {
                    "id": int,
                    "name": string,
                    "x": int, (this number will be divided with the screen size)
                    "y": int, (this number will be divided with the screen size too)
                    "unlocked": bool,
                    "finished": bool
                }
            ]

        """
        raise NotImplementedError('You must implement this method')

    @abc.abstractmethod
    def update_draw(self, screen):
        """
            Must return the code that will be executed every frame
        """
        raise NotImplementedError('You must implement this method')

    # ================================================================ #
    # ================================================================ #

    # construct method
    def __init__(self, city):

        self.city = city

        # font | Main font
        self.font = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 35)
        # font2 | Second font
        self.font2 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 45)
        # font3 | Third font
        self.font3 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 70)
        # font4 | 4th font
        self.font4 = pygame.font.SysFont("Arial", 20)

        # description_paragraphs | Stores all the paragraphs of the description
        self.description_paragraphs = []

        # create
        self.background = pygame.image.load(self.menu_settings()['background-path']) 
        self.name_text = self.font2.render(self.name(), True, (46, 204, 113))
        self.return_button = pygame.image.load('assets/images/back.png')

        # city_button | Stores the image of the button to go in the city
        self.city_button = pygame.image.load('assets/images/historyMode/cities/cityButton.png')
        # city_button_text | Stores the text which is below the city button
        self.city_button_text = self.font4.render("Your city !", True, (255, 255, 255))

        # get rects
        self.return_button_rect = self.return_button.get_rect()
        self.return_button_rect.x = 0
        self.return_button_rect.y = 0

        self.city_button_rect = self.city_button.get_rect()
        self.city_button_rect.x = 0
        self.city_button_rect.y = 0

        # add description paragraphs
        for d in self.description():
            paragraph = self.font.render(d, True, (255, 255, 255))
            self.description_paragraphs.append(paragraph)

    # draws the menu
    # @param screen : the screen surface
    # @param game : the instance of the class Game
    def draw_menu(self, screen, game):

        # reload
        self.background = pygame.image.load(self.menu_settings()['background-path']) 
        self.name_text = self.font2.render(self.name(), True, (46, 204, 113))
        self.return_button = pygame.image.load('assets/images/back.png')
        self.city_button = pygame.image.load('assets/images/historyMode/cities/cityButton.png')
        self.city_button_text = self.font4.render("Your city !", True, (255, 255, 255))

        # resize
        self.background = pygame.transform.scale(self.background, (screen.get_width(), screen.get_height()))
        self.name_text = pygame.transform.scale(self.name_text, (int(screen.get_width() / 5.5), int(screen.get_height() / 8)))
        self.return_button = pygame.transform.scale(self.return_button, (int(screen.get_width() / 15), int(screen.get_height() / 13)))
        self.city_button = pygame.transform.scale(self.city_button, (70, 70))

        # get rects
        self.return_button_rect = self.return_button.get_rect()
        self.return_button_rect.x = 0
        self.return_button_rect.y = screen.get_height() / 1.13

        self.city_button_rect = self.city_button.get_rect()
        self.city_button_rect.x = screen.get_width() / 1.4
        self.city_button_rect.y = screen.get_height() / 2.3

        for i in range(0, len(self.description_paragraphs)):
            self.description_paragraphs[i] = self.font.render(self.description()[i], True, (255, 255, 255))
            self.description_paragraphs[i] = pygame.transform.scale(self.description_paragraphs[i], (int(screen.get_width() / 5.5), 40))

        # ================================================== #
        #                       QUESTS                       #
        # ================================================== #
        
        self.quests_var = self.quests()

        for q in self.quests_var:
            
            # set if it is unlocked
            if q['id'] == game.game_data.data_player['history_mode']['region'][self.yaml_name()]['current_quest']:
                q['unlocked'] = True
            if game.game_data.data_player['history_mode']['region'][self.yaml_name()]['current_quest'] > q['id']:
                q['unlocked'] = False
                q['finished'] = True
            if game.game_data.data_player['history_mode']['region'][self.yaml_name()]['current_quest'] < q['id']:
                q['unlocked'] = False

            # load its image
            if q['unlocked']:
                q['image'] = pygame.transform.scale(pygame.image.load('assets/images/unlocked.png'), (50, 50))
            if not q['unlocked']:
                q['image'] = pygame.transform.scale(pygame.image.load('assets/images/lock.png'), (50, 50))
            if q['finished']:
                q['image'] = pygame.transform.scale(pygame.image.load('assets/images/cross2.png'), (50, 50))
            
            # get its rect
            q['rect'] = q['image'].get_rect()

            # set its position    
            q['rect'].x = screen.get_width() / q['x']
            q['rect'].y = screen.get_height() / q['y']

            # set a text with its name if it is unlocked or finished
            if q['unlocked'] or q['finished']:
                q['text'] = self.font4.render(q['name'], True, (255, 255, 255))
            else:
                q['text'] = None

        # draw
        screen.blit(self.background, (0, 0))
        screen.blit(self.name_text, (0, 0))
        screen.blit(self.return_button, self.return_button_rect)
        screen.blit(self.city_button, self.city_button_rect)
        screen.blit(self.city_button_text, (self.city_button_rect.x, self.city_button_rect.y + 75))

        for idx, val in enumerate(self.description_paragraphs):
            screen.blit(val, (screen.get_width() / 100, idx * 50 + 90))

        for q in self.quests_var:
            screen.blit(q['image'], q['rect'])

            if q['text'] is not None:
                screen.blit(q['text'], (q['rect'].x - q['text'].get_width() / 3, q['rect'].y + 60))

        self.update_draw(screen)

    # when click event
    # @param pos : the position of the mouse
    def is_return_button_clicked(self, pos):
        # if return button clicked
        return self.return_button_rect.collidepoint(pos)

    # when click event
    # @param pos : the position of the mouse
    def is_city_button_clicked(self, pos):
        # if city button clicked
        return self.city_button_rect.collidepoint(pos)

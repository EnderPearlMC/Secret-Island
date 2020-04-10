import pygame
import abc


# class which owns every system of a city
class City:
    __metaclass__ = abc.ABCMeta

    # ABSTRACT METHODS

    @abc.abstractmethod
    def name(self):
        """
            Must return the name of the city
        """
        raise NotImplementedError('You must implement this method')

    @abc.abstractmethod
    def yaml_name(self):
        """
            Must return the name of the yaml path of the region (string)
        """
        raise NotImplementedError('You must implement this method')

    @abc.abstractmethod
    def plots(self):
        """
            Must return the plots of the city (List of Dictionnaries)

            [
                {
                    "id": int,
                    "cells": [
                        {
                            "x_cell": int,
                            "y_cell": int
                        }
                    ]
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
    def __init__(self):

        # font | Main font
        self.font = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 35)
        # font2 | Second font
        self.font2 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 45)
        # font3 | Third font
        self.font3 = pygame.font.Font("assets/fonts/PermanentMarker.ttf", 70)
        # font4 | 4th font
        self.font4 = pygame.font.SysFont("Arial", 20)

        self.loaded = False

        """
            FOR THE TILE MAP
        """

        # TILES_SIZE | Stores the size of the tiles
        self.TILES_SIZE = 80
        # tiles_images | Stores the images of the tiles
        self.tiles_images = []

        # camera
        # camera_pos | Stores the position of the camera
        self.camera_pos = [0, 0]
        # can_camera_move | True : the camera can be moved / False : not
        self.can_camera_move = True
        # is_mouse_button_down | True : the mouse button is down / False : the mouse button is up
        self.is_mouse_button_down = False
        # is_camera_moving | True : the user is moving the camera / False : not
        self.is_camera_moving = False
        # initial_mouse_pos | The position of the mouse before moving it when the user moves the camera
        self.initial_mouse_pos = [0, 0]
        self.initial_camera_pos = [0, 0]

        """
            FOR THE BUILD CATEGORIES
        """
        self.build_categories = [
            {
                "name": "Ground",
                "image_path": "assets/images/historyMode/cities/groundCategoryImg.png",
                "items": [
                    {
                        "name": "Grass"
                    }
                ]
            }
        ]

        # =================================================== #

        self.add_tiles_images()

        # create
        # background | Stores the background image
        self.return_button = pygame.image.load('assets/images/back.png')

        # BUILD PANEL
        # build_panel | Stores the panel that contains all the build tools
        self.build_panel = pygame.image.load('assets/images/historyMode/cities/cityBuildPanel.png').convert()
        self.build_panel_minimize = pygame.image.load('assets/images/minimizeButton.png')

        self.cursor_image = pygame.transform.scale(pygame.image.load("assets/images/cursor.png"), (50, 50))

        # get rects
        self.return_button_rect = self.return_button.get_rect()

        self.build_panel_rect = self.build_panel.get_rect()
        self.build_panel_minimize_rect = self.build_panel_minimize.get_rect()

        # BUILD CATEGORIES
        for c in self.build_categories:

            # add image
            c['image'] = pygame.image.load(c['image_path'])

            # add button image to the category
            c['button_image'] = pygame.image.load('assets/images/historyMode/cities/buildCategoryButton.png')

            # get rects of the buttons
            c['button_rect'] = c['button_image'].get_rect()

    def draw_city(self, screen, game):

        pygame.mouse.set_visible(False)

        # Move camera

        if self.is_mouse_button_down:
            if pygame.mouse.get_pos() != self.initial_mouse_pos:
                self.is_camera_moving = True
            else:
                self.is_camera_moving = False

        if self.is_camera_moving and self.can_camera_move:
            diff_x = pygame.mouse.get_pos()[0] - self.initial_mouse_pos[0]
            diff_y = pygame.mouse.get_pos()[1] - self.initial_mouse_pos[1]

            self.camera_pos[0] = self.initial_camera_pos[0] + diff_x
            self.camera_pos[1] = self.initial_camera_pos[1] + diff_y

        if not self.loaded:
            # resize
            self.return_button = pygame.transform.scale(self.return_button,
                                                        (int(screen.get_width() / 15), int(screen.get_height() / 13)))

            # BUILD PANEL
            self.build_panel = pygame.transform.scale(self.build_panel,
                                                      (int(screen.get_width() - 20), int(screen.get_height() / 4.5)))
            self.build_panel_minimize = pygame.transform.scale(self.build_panel_minimize, (
                int(screen.get_width() / 34), int(screen.get_height() / 29)))

            # BUILD CATEGORIES
            for c in self.build_categories:
                # resize
                c['button_image'] = pygame.transform.scale(c['button_image'],
                                                           (int(screen.get_width() / 8), int(screen.get_height() / 6)))
                # resize
                c['image'] = pygame.transform.scale(c['image'],
                                                    (int(c['button_image'].get_width() / 1.2),
                                                     int(c['button_image'].get_height() / 1.1)))

            self.loaded = True

        # get rects
        self.return_button_rect = self.return_button.get_rect()
        self.return_button_rect.x = 0
        self.return_button_rect.y = 10

        self.build_panel_rect = self.build_panel.get_rect()
        self.build_panel_rect.x = 10
        self.build_panel_rect.y = screen.get_height() - self.build_panel.get_height()

        self.build_panel_minimize_rect = self.build_panel_minimize.get_rect()
        self.build_panel_minimize_rect.x = screen.get_width() - self.build_panel_minimize.get_width() - 25
        self.build_panel_minimize_rect.y = screen.get_height() / 1.26

        # BUILD CATEGORIES
        for c in self.build_categories:
            c['button_rect'] = c['button_image'].get_rect()
            c['button_rect'].x = self.build_panel_rect.x + 15
            c['button_rect'].y = self.build_panel_rect.y + self.build_panel.get_height() / 1.3

        # draw
        screen.fill((52, 152, 219))

        self.draw_map(screen, game)

        screen.blit(self.return_button, self.return_button_rect)

        # BUILD PANEL
        screen.blit(self.build_panel, self.build_panel_rect)
        screen.blit(self.build_panel_minimize, self.build_panel_minimize_rect)

        # BUILD CATEGORIES
        for c in self.build_categories:
            screen.blit(c['button_image'], c['button_rect'])
            screen.blit(c['image'], (c['button_rect'].x / 1.2, c['button_rect'].y / 1.2))

        screen.blit(self.cursor_image, pygame.mouse.get_pos())

        self.update_draw(screen)

    def update_screen_resize(self, screen):
        # reload
        self.return_button = pygame.image.load('assets/images/back.png')

        self.build_panel = pygame.image.load('assets/images/historyMode/cities/cityBuildPanel.png').convert()
        self.build_panel_minimize = pygame.image.load('assets/images/minimizeButton.png')

        # resize
        self.return_button = pygame.transform.scale(self.return_button,
                                                    (int(screen.get_width() / 15), int(screen.get_height() / 13)))

        # BUILD PANEL
        self.build_panel = pygame.transform.scale(self.build_panel,
                                                  (int(screen.get_width() - 20), int(screen.get_height() / 4.5)))
        self.build_panel_minimize = pygame.transform.scale(self.build_panel_minimize, (
            int(screen.get_width() / 34), int(screen.get_height() / 29)))

        # BUILD CATEGORIES
        for c in self.build_categories:
            # reload
            c['button_image'] = pygame.image.load('assets/images/historyMode/cities/buildCategoryButton.png')
            c['image'] = pygame.image.load(c['image_path'])

            # resize
            c['button_image'] = pygame.transform.scale(c['button_image'],
                                                       (int(screen.get_width() / 8), int(screen.get_height() / 6)))
            c['image'] = pygame.transform.scale(c['image'],
                                                (int(c['button_image'].get_width() / 1.2),
                                                 int(c['button_image'].get_height() / 1.1)))

    # draws the tile map
    def draw_map(self, screen, game):
        # draw map
        for idx, val in enumerate(
                game.game_data.data_player['history_mode']['region'][self.yaml_name()]['city']['map']):
            for idx2, val2 in enumerate(val):
                if val2 > 0:
                    screen.blit(self.tiles_images[val2 - 1], (
                        idx2 * self.TILES_SIZE + self.camera_pos[0], idx * self.TILES_SIZE + self.camera_pos[1]))

    # when hover event
    def hover(self, pos):
        if self.build_panel_rect.collidepoint(pos):
            self.can_camera_move = False
        else:
            self.can_camera_move = True

    # when click event
    # @param pos : the position of the mouse
    def is_return_button_clicked(self, pos):
        # if return button clicked
        return self.return_button_rect.collidepoint(pos)

    # when mouse button down
    def mouse_button_down(self, e, pos):
        if e.button == 3:
            self.initial_mouse_pos = pygame.mouse.get_pos()
            self.initial_camera_pos[0] = self.camera_pos[0]
            self.initial_camera_pos[1] = self.camera_pos[1]
            self.is_mouse_button_down = True

    # when mouse button up
    def mouse_button_up(self, e, pos):
        if e.button == 3:
            self.is_mouse_button_down = False
            self.is_camera_moving = False

    # when scroll up
    def scroll_up(self):
        if self.TILES_SIZE < 150:
            self.TILES_SIZE += 5
            self.add_tiles_images()

    # when scroll down
    def scroll_down(self):
        if self.TILES_SIZE > 10:
            self.TILES_SIZE -= 5
            self.add_tiles_images()

    def add_tiles_images(self):
        self.tiles_images = [
            pygame.transform.scale(pygame.image.load("assets/images/historyMode/cities/tiles/grass.png").convert(),
                                   (self.TILES_SIZE, self.TILES_SIZE)),
            pygame.transform.scale(pygame.image.load("assets/images/historyMode/cities/tiles/dirt.png").convert(),
                                   (self.TILES_SIZE, self.TILES_SIZE))
        ]

import os
import pygame

from state import State


# class which stores the application
class App:

    def load(self):

        # ==========================================
        #   VARIABLES
        # ==========================================

        # game_infos | Stores informations about the game
        self.game_infos = {
            "version": "Alpha 0.0.2",
            "author": "EnderPearl MC and ProGamerXbox",
            "start_mode": "debug",
            "start_point": State.HISTORY_MODE_MAIN_MAP
        }

        if self.game_infos['start_mode'] == "release":
            self.main_menu_on = False
        elif self.game_infos['start_mode'] == "debug" or self.game_infos['start_mode'] == "debug-music":
            self.main_menu_on = True

    def update(self, screen, game):
        if os.path.exists('files/player.yaml'):
            game.game_data.data_player = game.game_data.get_player_file_data()

        game.game_data.make_datas_as_file()

        if game.state == State.MAIN_MENU:
            game.main_menu.update(screen, game)
        if game.state == State.SECOND_MENU:
            game.second_menu.update(screen, game)

        # update version text
        self.version_text = game.font.render(self.game_infos["version"], True, (255, 255, 255))

        ##########################
        #      HISTORY MODE      #
        ##########################

        if game.state == State.HISTORY_MODE_START_HELP:
            game.hm_help1_menu.update(screen, game)
        elif game.state == State.HISTORY_MODE_MAIN_MAP:
            game.hm_main_map.update(screen, game)

        if game.state != State.HISTORY_MODE_REGION_CITY:
            pygame.mouse.set_visible(True)

    def update_video_resize(self, screen, game):
        if game.state == State.HISTORY_MODE_REGION_CITY:
            game.region_manager.current_region.city.update_screen_resize(screen)

    def draw(self, screen, game):
        # if game state is mainmenu
        if game.state == State.MAIN_MENU:
            # draw main menu
            screen.blit(game.main_menu.background, (0, 0))
            screen.blit(game.main_menu.sun, (0, 0))
            # draw title text
            screen.blit(game.main_menu.title,
                        (screen.get_width() / 2 - game.main_menu.title.get_width() / 2, screen.get_height() / 3))
            # draw play button
            screen.blit(game.main_menu.play_button, game.main_menu.play_button_rect)
            # draw play button text
            screen.blit(game.main_menu.play_button_text, (
                game.main_menu.play_button_rect.x + game.main_menu.play_button.get_width() / 3,
                game.main_menu.play_button_rect.y + game.main_menu.play_button.get_height() / 4))
            # draw coin amount text
            screen.blit(game.main_menu.coin_amount_text,
                        (int(screen.get_width() - game.main_menu.coin_amount_text.get_width() - 60), 5))
            # draw coin image
            screen.blit(game.main_menu.coin,
                        (int((screen.get_width() - 120) - game.main_menu.coin_amount_text.get_width()), 5))
            # draw buy coins text
            screen.blit(game.main_menu.buy_coins_text, (int((screen.get_width() - 120) + 76), 5))
            # draw pseudo text
            screen.blit(game.main_menu.pseudo_text,
                        (10, screen.get_height() - game.main_menu.pseudo_text.get_height() - 5))
            # draw level text
            screen.blit(game.main_menu.level_text, (20, 90))
            # draw settings button image
            screen.blit(game.main_menu.settings_button, game.main_menu.settings_button_rect)
            # draw settings button text
            screen.blit(game.main_menu.settings_button_text, (50, 23))
        # if game state is second menu
        elif game.state == State.SECOND_MENU:
            # draw background image
            screen.blit(game.second_menu.background, (0, 0))
            # draw select text
            screen.blit(game.second_menu.select_text, (screen.get_width() / 3.3, 40))

            # CARDS
            for key, val in game.second_menu.current_card.items():
                for surface, rect in val.items():
                    screen.blit(surface, rect)

        ##########################
        #      HISTORY MODE      #
        ##########################

        # if game state is history mode start help
        elif game.state == State.HISTORY_MODE_START_HELP:
            # draw background image
            screen.blit(game.hm_help1_menu.background, (0, 0))
            # draw title text
            screen.blit(game.hm_help1_menu.title, (20, 20))
            # draw next paragraph text
            screen.blit(game.hm_help1_menu.next_p_text, (20, screen.get_height() / 1.5))

            """
                Paragraph
            """
            screen.blit(game.hm_help1_menu.p_order[game.hm_help1_menu.current_paragraph], (20, screen.get_height() / 2))

        # if game state is history mode main map
        elif game.state == State.HISTORY_MODE_MAIN_MAP:
            # draw background image
            screen.blit(game.hm_main_map.background, (0, 0))

            # draw regions
            for r in game.hm_main_map.regions:
                if r['id'] == game.game_data.data_player['history_mode']['region']['current_region']:
                    screen.blit(r['light_around'], r['light_around_rect'])

                screen.blit(r['image'], r['rect'])

            # draw description
            if game.hm_main_map.description_shown:

                # draw go button
                screen.blit(game.hm_main_map.go_button, game.hm_main_map.go_button_rect)

                # draw go button text
                screen.blit(game.hm_main_map.go_button_text,
                            (game.hm_main_map.go_button_rect.x + 20, game.hm_main_map.go_button_rect.y + 5))

                for idx, val in enumerate(game.hm_main_map.descriptions):
                    screen.blit(val, (int(screen.get_width() / 2 - val.get_width() / 2),
                                      int(idx * 50 + (screen.get_height() / 2.5 - val.get_height()))))

                # draw close cross
                screen.blit(game.hm_main_map.cross, game.hm_main_map.cross_rect)

            # draw locked error
            if game.hm_main_map.locked_shown:
                screen.blit(game.hm_main_map.locked_text, (
                    screen.get_width() / 2 - game.hm_main_map.locked_text.get_width() / 2,
                    0 * 50 + (screen.get_height() / 2 - game.hm_main_map.locked_text.get_height())))
                # draw close cross
                screen.blit(game.hm_main_map.cross, game.hm_main_map.cross_rect)

        # if game state is history mode region menu
        elif game.state == State.HISTORY_MODE_REGION_MENU:
            game.region_manager.draw_region_menu(screen, game)

        # if game state is history mode region city
        elif game.state == State.HISTORY_MODE_REGION_CITY:
            screen.fill((255, 255, 255))
            game.region_manager.draw_region_city(screen, game)

        # draw version text
        if game.state == State.HISTORY_MODE_REGION_CITY:
            screen.blit(game.version_text, (5,
                                            screen.get_height() - game.version_text.get_height()))
        else:
            screen.blit(game.version_text, (screen.get_width() - game.version_text.get_width(),
                                            screen.get_height() - game.version_text.get_height()))

    def hover(self, screen, game):
        # hovers things of the menus
        if game.state == State.MAIN_MENU:
            game.main_menu.hover(pygame.mouse.get_pos(), screen)
        if game.state == State.SECOND_MENU:
            game.second_menu.hover(pygame.mouse.get_pos(), screen)
        if game.state == State.HISTORY_MODE_MAIN_MAP:
            game.hm_main_map.hover(pygame.mouse.get_pos())
        if game.state == State.HISTORY_MODE_REGION_CITY:
            game.region_manager.current_region.city.hover(pygame.mouse.get_pos())

    # add fade in animation
    def fade_in(self, w, h, speed, screen, game):
        f = pygame.Surface((w, h))
        f.fill((0, 0, 0))

        i = 300
        while i >= 0:
            f.set_alpha(i)
            self.draw(screen, game)
            screen.blit(f, (0, 0))
            pygame.display.flip()
            i -= speed

    # add fade out animation
    def fade_out(self, w, h, speed, screen, game):
        f = pygame.Surface((w, h))
        f.fill((0, 0, 0))

        i = 0
        while i <= 300:
            f.set_alpha(i)
            self.draw(screen, game)
            screen.blit(f, (0, 0))
            pygame.display.flip()
            i += speed

    def mouse_button_up(self, e, screen, game):

        if game.state == State.HISTORY_MODE_MAIN_MAP:
            game.hm_main_map.on_click(pygame.mouse.get_pos())
        if game.state == State.HISTORY_MODE_REGION_CITY:
            game.region_manager.current_region.city.mouse_button_up(e, pygame.mouse.get_pos())

        if game.state == State.MAIN_MENU:
            if game.main_menu.is_play_button_pressed(pygame.mouse.get_pos()):
                self.fade_out(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
                game.state = State.SECOND_MENU
                game.second_menu.init(screen)
                self.update(screen, game)
                self.fade_in(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
        elif game.state == State.SECOND_MENU:
            if game.second_menu.is_history_mode_button_pressed(pygame.mouse.get_pos()):
                if game.game_data.data_player['history_mode']['adv_help'] == 1:
                    self.fade_out(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
                    game.state = State.HISTORY_MODE_START_HELP
                    self.update(screen, game)
                    self.fade_in(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
                else:
                    self.fade_out(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
                    game.state = State.HISTORY_MODE_MAIN_MAP
                    game.hm_main_map.init()
                    self.update(screen, game)
                    self.fade_in(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
        elif game.state == State.HISTORY_MODE_MAIN_MAP:
            if game.hm_main_map.is_go_button_clicked(pygame.mouse.get_pos()):
                game.region_manager.load_region(game.hm_main_map.selected_region)
                game.state = State.HISTORY_MODE_REGION_MENU
        elif game.state == State.HISTORY_MODE_REGION_MENU:
            game.region_manager.current_region.mouse_button_up(e)
            if game.region_manager.current_region.is_return_button_clicked(pygame.mouse.get_pos()):
                game.state = State.HISTORY_MODE_MAIN_MAP
                game.hm_main_map.init()
                game.region_manager.unload_current_region()
                game.hm_main_map.description_shown = False
                self.update(screen, game)
            elif game.region_manager.current_region.is_city_button_clicked(pygame.mouse.get_pos()):
                game.state = State.HISTORY_MODE_REGION_CITY
                game.region_manager.current_region.city.TILES_SIZE = 80
                game.region_manager.current_region.city.add_tiles_images()
                game.region_manager.current_region.city.camera_pos = [0, 0]
                self.update(screen, game)
        elif game.state == State.HISTORY_MODE_REGION_CITY:
            if game.region_manager.current_region.city.is_return_button_clicked(pygame.mouse.get_pos()):
                game.state = State.HISTORY_MODE_REGION_MENU
                self.update(screen, game)

    def key_up(self, e, screen, game):
        if game.state == State.HISTORY_MODE_START_HELP:
            if e.key == pygame.K_RETURN:
                if game.hm_help1_menu.current_paragraph + 1 < len(game.hm_help1_menu.p_order):
                    game.hm_help1_menu.current_paragraph += 1
                else:
                    game.game_data.data_player['history_mode']['adv_help'] = 2
                    game.game_data.make_datas_as_file()
                    self.fade_out(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
                    game.state = State.HISTORY_MODE_MAIN_MAP
                    game.hm_main_map.init()
                    self.update(screen, game)
                    self.fade_in(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
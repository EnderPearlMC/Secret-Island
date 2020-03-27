import pygame

from game import Game
from state import State

# init pygame
pygame.init()

# create window
screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
# set title of it
pygame.display.set_caption("Game")

# ==========================================
#   VARIABLES
# ==========================================

# game_infos | Stores informations about the game
game_infos = {
    "version": "Alpha 0.0.2",
    "author": "EnderPearl MC and ProGamerXbox"
}

# running | true : the window is running / false : the window doesn't run anymore
running = True
# game | Stores class Games
game = Game(screen, game_infos)
# blocks_size | Stores the size of the blocks that will be generated
blocks_size = (100, 116)

main_menu_on = True


# add fade in animation
def fade_in(w, h, speed):
    f = pygame.Surface((w, h))
    f.fill((0, 0, 0))

    i = 300
    while i >= 0:
        f.set_alpha(i)
        draw()
        screen.blit(f, (0, 0))
        pygame.display.flip()
        i -= speed


# add fade out animation
def fade_out(w, h, speed):
    f = pygame.Surface((w, h))
    f.fill((0, 0, 0))

    i = 0
    while i <= 300:
        f.set_alpha(i)
        draw()
        screen.blit(f, (0, 0))
        pygame.display.flip()
        i += speed


# draws everything of the game
def draw():

    # if game state is mainmenu
    if game.state == State.MAIN_MENU:
        # draw main menu
        screen.blit(game.main_menu.background, (0, 0))
        # draw title text
        screen.blit(game.main_menu.title, (screen.get_width() / 2.4, screen.get_height() / 3))
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
        screen.blit(game.main_menu.pseudo_text, (10, screen.get_height() - game.main_menu.pseudo_text.get_height() - 5))
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
        screen.blit(game.hm_help1_menu.p_order[game.hm_help1_menu.current_paragraph], (20, screen.get_height() / 2))

    # if game state is history mode main map
    elif game.state == State.HISTORY_MODE_MAIN_MAP:
        # draw background image
        screen.blit(game.hm_main_map.background, (0, 0))

        # draw regions
        for r in game.hm_main_map.regions:
            screen.blit(r['image'], r['rect'])

    # draw version text
    screen.blit(game.version_text, (screen.get_width() - game.version_text.get_width(),
                                    screen.get_height() - game.version_text.get_height()))


# works when mouse click is up
def mouse_button_up():
    if game.state == State.MAIN_MENU:
        if game.main_menu.is_play_button_pressed(pygame.mouse.get_pos()):
            fade_out(screen.get_width(), screen.get_height(), 4)
            game.state = State.SECOND_MENU
            game.second_menu.init(screen)
            game.update(screen)
            fade_in(screen.get_width(), screen.get_height(), 4)
    elif game.state == State.SECOND_MENU:
        if game.second_menu.is_history_mode_button_pressed(pygame.mouse.get_pos()):
            if game.game_data.data_player['history_mode']['adv_help'] == 1:
                fade_out(screen.get_width(), screen.get_height(), 4)
                game.state = State.HISTORY_MODE_START_HELP
                game.update(screen)
                fade_in(screen.get_width(), screen.get_height(), 4)
            else:
                fade_out(screen.get_width(), screen.get_height(), 4)
                game.update(screen)
                game.state = State.HISTORY_MODE_MAIN_MAP
                fade_in(screen.get_width(), screen.get_height(), 4)


# works when key up event
def key_up(e):
    if game.state == State.HISTORY_MODE_START_HELP:
        if e.key == pygame.K_RETURN:
            if game.hm_help1_menu.current_paragraph + 1 < len(game.hm_help1_menu.p_order):
                game.hm_help1_menu.current_paragraph += 1
            else:
                game.game_data.data_player['history_mode']['adv_help'] = 2
                game.game_data.make_datas_as_file()
                fade_out(screen.get_width(), screen.get_height(), 4)
                game.state = State.HISTORY_MODE_MAIN_MAP
                game.update(screen)
                fade_in(screen.get_width(), screen.get_height(), 4)


# Main loop which updates all parts of the game
while running:

    # hovers things of the menus
    if game.state == State.MAIN_MENU:
        game.main_menu.hover(pygame.mouse.get_pos(), screen)
    if game.state == State.SECOND_MENU:
        game.second_menu.hover(pygame.mouse.get_pos(), screen)

    # update window
    pygame.display.flip()
    # update everything of the game
    game.update(screen)

    # draw elements
    draw()

    # get events
    for e in pygame.event.get():

        # if cross is pressed
        if e.type == pygame.QUIT:
            # set running to False
            running = True
            # close window
            pygame.quit()

        # if mouse up
        if e.type == pygame.MOUSEBUTTONUP:
            mouse_button_up()

        # if key down
        if e.type == pygame.KEYDOWN:
            # set the key as True in the key pressed dictionary
            game.keys_pressed[e.key] = True

        # if key up
        if e.type == pygame.KEYUP:
            # set the key as False in the key pressed dictionary
            game.keys_pressed[e.key] = False

            key_up(e)

        # if window resizable
        if e.type == pygame.VIDEORESIZE:

            # recreate window with new dimensions
            screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)
            # assign new size for the size of the blocks
            if screen.get_width() < 1280 and screen.get_width() > 800:
                blocks_size = (80, 96)
            elif screen.get_width() < 800:
                blocks_size = (60, 76)
            else:
                blocks_size = (100, 116)
            if screen.get_height() < 720 and screen.get_height() > 600:
                blocks_size = (80, 96)
            elif screen.get_height() < 600:
                blocks_size = (60, 76)
            else:
                blocks_size = (100, 116)

            # update
            game.update_video_resize(screen, blocks_size)

    if not main_menu_on:
        fade_in(screen.get_width(), screen.get_height(), 2)
        main_menu_on = True

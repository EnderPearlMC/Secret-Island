import pygame

from app import App
from game import Game
from state import State

# init pygame
pygame.init()

# create window
screen = pygame.display.set_mode((1000, 600), pygame.RESIZABLE)
# set title of it
pygame.display.set_caption("Secret Island")
pygame.display.set_icon(pygame.image.load('assets/images/logo.png'))

# running | true : the window is running / false : the window doesn't run anymore
running = True

clock = pygame.time.Clock()
FPS = 60

# app | Stores the application
app = App()
app.load()
# game | Stores class Games
game = Game(screen, app.game_infos)

# Main loop which updates all parts of the game
while running:

    # update window
    pygame.display.flip()

    game.deltaTime = clock.tick(FPS) / 100

    # hover
    app.hover(screen, game)

    # update everything of the game
    app.update(screen, game)

    # draw elements
    app.draw(screen, game)

    # get events
    for e in pygame.event.get():

        # if cross is pressed
        if e.type == pygame.QUIT:
            # set running to False
            running = False
            # close window
            pygame.quit()

        # if mouse down
        if e.type == pygame.MOUSEBUTTONDOWN:
            if game.state == State.HISTORY_MODE_REGION_CITY:
                game.region_manager.current_region.city.mouse_button_down(e, pygame.mouse.get_pos())
                if e.button == 4:
                    game.region_manager.current_region.city.scroll_up()
                elif e.button == 5:
                    game.region_manager.current_region.city.scroll_down()

        # if mouse up
        if e.type == pygame.MOUSEBUTTONUP:
            app.mouse_button_up(e, screen, game)

        # if key down
        if e.type == pygame.KEYDOWN:
            # set the key as True in the key pressed dictionary
            game.keys_pressed[e.key] = True

        # if key up
        if e.type == pygame.KEYUP:
            # set the key as False in the key pressed dictionary
            game.keys_pressed[e.key] = False

            app.key_up(e, screen, game)

        # if window resizable
        if e.type == pygame.VIDEORESIZE:
            # recreate window with new dimensions
            screen = pygame.display.set_mode((e.w, e.h), pygame.RESIZABLE)

            # update
            app.update_video_resize(screen, game)

    if not app.main_menu_on:
        app.fade_in(screen.get_width(), screen.get_height(), 4 * game.deltaTime, screen, game)
        app.main_menu_on = True

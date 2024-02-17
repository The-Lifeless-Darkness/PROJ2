from config import fetch_configuration
from button import Button
from updater import Updater

import pygame
import sys
import pyautogui
import webbrowser
from threading import Thread

configuration = fetch_configuration()

try:
    configuration.fetch_resources()
except Exception as e:
    pyautogui.alert("Can't fetch launcher resources. Exit")
    sys.exit()

pygame.init()
pygame.display.set_caption(configuration.window_title)
background = pygame.image.load(configuration.background_image_save_name)
WIDTH, HEIGHT = background.get_width(), background.get_height()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
updating = False


def update():
    global updating

    updater = Updater(configuration)
    updater.update_game()

    updating = False


def launch():
    global updating

    if not updating:
        updating = True

        thread = Thread(target=update)
        thread.start()


buttons = [
    Button(
        'Launch',
        WIDTH - 400,
        HEIGHT - 100,
        200,
        50,
        configuration.launch_background_color,
        configuration.launch_background_color_hover,
        configuration.launch_text_color,
        configuration.launch_text_color_hover,
        launch),
    Button(
        'Version Info',
        WIDTH - 350,
        HEIGHT - 175,
        150,
        40,
        configuration.version_info_background_color,
        configuration.version_info_background_color_hover,
        configuration.version_info_text_color,
        configuration.version_info_text_color_hover,
        lambda: webbrowser.open(configuration.version_info_url)),
    Button(
        'YouTube',
        WIDTH - 125,
        50,
        100,
        25,
        configuration.youtube_background_color,
        configuration.youtube_background_color_hover,
        configuration.youtube_text_color,
        configuration.youtube_text_color_hover,
        lambda: webbrowser.open(configuration.youtube_url),
        24),
    Button(
        'Twitter',
        WIDTH - 125,
        125,
        100,
        25,
        configuration.twitter_background_color,
        configuration.twitter_background_color_hover,
        configuration.twitter_text_color,
        configuration.twitter_text_color_hover,
        lambda: webbrowser.open(configuration.twitter_url),
        24),
    Button(
        'Discord',
        WIDTH - 125,
        200,
        100,
        25,
        configuration.discord_background_color,
        configuration.discord_background_color_hover,
        configuration.discord_text_color,
        configuration.discord_text_color_hover,
        lambda: webbrowser.open(configuration.discord_url),
        24),
    Button(
        'Reddit',
        WIDTH - 125,
        275,
        100,
        25,
        configuration.reddit_background_color,
        configuration.reddit_background_color_hover,
        configuration.reddit_text_color,
        configuration.reddit_text_color_hover,
        lambda: webbrowser.open(configuration.reddit_url),
        24),
    Button(
        'Game Site',
        WIDTH - 125,
        350,
        100,
        25,
        configuration.game_site_background_color,
        configuration.game_site_background_color_hover,
        configuration.game_site_text_color,
        configuration.game_site_text_color_hover,
        lambda: webbrowser.open(configuration.game_site_url),
        24),
    Button(
        'Telegram',
        WIDTH - 125,
        425,
        100,
        25,
        configuration.telegram_background_color,
        configuration.telegram_background_color_hover,
        configuration.telegram_text_color,
        configuration.telegram_text_color_hover,
        lambda: webbrowser.open(configuration.telegram_url),
        24),
]


# Game loop
running = True
while running:
    # Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))

    for button in buttons:
        button.draw(screen)

    pygame.display.flip()

pygame.quit()
sys.exit()

from dataclasses import dataclass
from typing import List, Optional
import requests


@dataclass
class GameVersion:
    """
    This class represents the game version details.
    """

    current_version: int
    """
    The current version of the game
    """

    download_archive_url: str
    """
    The URL where the game can be downloaded
    """


@dataclass
class Config:
    """
    This class represents the game data which includes various properties related to the game.
    """

    game_version: GameVersion
    """
    The game version details
    """

    background_image_url: str
    """
    The URL of the background image
    """

    background_image_save_name: str
    """
    The name to save the background image
    """

    launch_background_color: List[int]
    """
    The RGB values of the launch background color
    """

    launch_background_color_hover: List[int]
    """
    The RGB values of the hover state of the launch background color
    """

    launch_text_color: List[int]
    """
    The RGB values of the launch text color
    """

    launch_text_color_hover: List[int]
    """
    The RGB values of the hover state of the launch text color
    """

    version_info_background_color: List[int]
    """
    The RGB values of the version info background color
    """

    version_info_background_color_hover: List[int]
    """
    The RGB values of the hover state of the version info background color
    """

    version_info_text_color: List[int]
    """
    The RGB values of the version info text color
    """

    version_info_text_color_hover: List[int]
    """
    The RGB values of the hover state of the version info text color
    """

    youtube_background_color: List[int]
    """
    The RGB values of the YouTube button background color
    """

    youtube_background_color_hover: List[int]
    """
    The RGB values of the hover state of the YouTube button background color
    """

    youtube_text_color: List[int]
    """
    The RGB values of the YouTube button text color
    """

    youtube_text_color_hover: List[int]
    """
    The RGB values of the hover state of the YouTube button text color
    """

    twitter_background_color: List[int]
    """
    The RGB values of the Twitter button background color
    """

    twitter_background_color_hover: List[int]
    """
    The RGB values of the hover state of the Twitter button background color
    """

    twitter_text_color: List[int]
    """
    The RGB values of the Twitter button text color
    """

    twitter_text_color_hover: List[int]
    """
    The RGB values of the hover state of the Twitter button text color
    """

    discord_background_color: List[int]
    """
    The RGB values of the Discord button background color
    """

    discord_background_color_hover: List[int]
    """
    The RGB values of the hover state of the Discord button background color
    """

    discord_text_color: List[int]
    """
    The RGB values of the Discord button text color
    """

    discord_text_color_hover: List[int]
    """
    The RGB values of the hover state of the Discord button text color
    """

    reddit_background_color: List[int]
    """
    The RGB values of the Reddit button background color
    """

    reddit_background_color_hover: List[int]
    """
    The RGB values of the hover state of the Reddit button background color
    """

    reddit_text_color: List[int]
    """
    The RGB values of the Reddit button text color
    """

    reddit_text_color_hover: List[int]
    """
    The RGB values of the hover state of the Reddit button text color
    """

    game_site_background_color: List[int]
    """
    The RGB values of the game site button background color
    """

    game_site_background_color_hover: List[int]
    """
    The RGB values of the hover state of the game site button background color
    """

    game_site_text_color: List[int]
    """
    The RGB values of the game site button text color
    """

    game_site_text_color_hover: List[int]
    """
    The RGB values of the hover state of the game site button text color
    """

    telegram_background_color: List[int]
    """
    The RGB values of the telegram button background color
    """

    telegram_background_color_hover: List[int]
    """
    The RGB values of the hover state of the telegram button background color
    """

    telegram_text_color: List[int]
    """
    The RGB values of the telegram button text color
    """

    telegram_text_color_hover: List[int]
    """
    The RGB values of the hover state of the telegram button text color
    """

    youtube_url: str
    """
    The URL of the YouTube page
    """

    twitter_url: str
    """
    The URL of the Twitter page
    """

    discord_url: str
    """
    The URL of the Discord page
    """

    reddit_url: str
    """
    The URL of the Reddit page
    """

    telegram_url: str
    """
    The URL of the Telegram page
    """

    game_site_url: str
    """
    The URL of the game site
    """

    version_info_url: str
    """
    The URL of the version info page
    """

    launch_cmdline: str
    """
    The command line to launch the game
    """

    window_title: str
    """
    The title of launcher window
    """

    def fetch_resources(self):
        """
        Downloads an background image
        """

        response = requests.get(self.background_image_url)
        response.raise_for_status()

        with open(self.background_image_save_name, 'wb') as file:
            file.write(response.content)


def fetch_configuration() -> Optional[Config]:
    """
    Downloads the JSON data from the specified URL and parses it into a GameData instance.
    :returns: A GameData instance if the download and parsing are successful, None otherwise.
    """
    try:
        response = requests.get("http://45.154.35.74:8080/YGame/launcher.json")
        response.raise_for_status()

        data = response.json()
        game_data = Config(**data)
        game_data.game_version = GameVersion(**game_data.game_version)

        return game_data
    except Exception as e:
        return None
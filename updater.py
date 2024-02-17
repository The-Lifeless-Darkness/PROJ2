import os
import shutil
import urllib.request
import zipfile
from config import Config


class Updater:
    """
    Updates and launches game
    """

    def __init__(self, config: Config):
        """
        Initializes updater
        :param config: latest fetched config
        """
        self.config = config

    @staticmethod
    def __get_installed_versions():
        """
        Returns all installed game versions
        """
        versions_dir = 'versions'

        return [int(name) for name in os.listdir(versions_dir) if os.path.isdir(os.path.join(versions_dir, name))]

    def update_game(self):
        """
        Main updating method. Checks latest version and updates it if need. Launches game.
        """
        latest_installed_version = max(self.__get_installed_versions(), default=0)

        if latest_installed_version is None or latest_installed_version < self.config.game_version.current_version:
            self.__clear_versions_directory()
            self.__download_and_unpack_game()

        self.__run_game()

    @staticmethod
    def __clear_versions_directory():
        """
        Cleans versions directory content from previous versions
        """
        versions_dir = 'versions'
        for filename in os.listdir(versions_dir):
            file_path = os.path.join(versions_dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')

    def __download_and_unpack_game(self):
        """
        Downloads archive with game and unpacks it to versions directory
        """

        urllib.request.urlretrieve(self.config.game_version.download_archive_url, 'game.zip')

        with zipfile.ZipFile('game.zip', 'r') as zip_ref:
            zip_ref.extractall(f'versions/{self.config.game_version.current_version}')

        os.remove('game.zip')

    def __run_game(self):
        """
        Launches game
        """

        os.system(self.config.launch_cmdline)
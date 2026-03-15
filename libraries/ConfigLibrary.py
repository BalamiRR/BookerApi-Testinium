import configparser
import os
from robot.api.deco import keyword
from robot.api import logger

class ConfigLibrary:

    ROBOT_LIBRARY_SCOPE = "GLOBAL"

    def __init__(self, config_path=None):
        self.config = configparser.ConfigParser()
        if config_path is None:
            # Pipeline'da CI_PROJECT_DIR'dan oku, yoksa local path kullan
            project_dir = os.environ.get("CI_PROJECT_DIR", os.getcwd())
            config_path = os.path.join(project_dir, "libraries", "config.ini")
        self.config.read(config_path)
        logger.info(f"Config loaded from: {config_path}")

    @keyword("Get Base URL")
    def get_base_url(self):
        url = self.config.get("API", "base_url")
        logger.info(f"Base URL: {url}")
        return url

    @keyword("Get Timeout")
    def get_timeout(self):
        return self.config.getint("API", "timeout")

    @keyword("Get Environment")
    def get_environment(self):
        return self.config.get("ENV", "environment")

    @keyword("Get Config Value")
    def get_config_value(self, section, key):
        value = self.config.get(section, key)
        logger.info(f"Config [{section}][{key}] = {value}")
        return value

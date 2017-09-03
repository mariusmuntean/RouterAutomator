import os

from BasePlatformInitializer import BasePlatformInitializer
from Logger import Logger


class DesktopLinuxPlatformInitializer(BasePlatformInitializer):
    def initialize(self):
        # Make sure there is a DISPLAY environment variable and that it is set correctly
        if not 'DISPLAY' in os.environ:
            Logger.logInfo("Env variable DISPLAY is missing. Setting it to ':0'")
            os.environ['DISPLAY'] = ':0'

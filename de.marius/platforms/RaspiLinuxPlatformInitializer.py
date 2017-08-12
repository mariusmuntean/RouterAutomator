import os

from BasePlatformInitializer import BasePlatformInitializer


class RaspiLinuxPlatformInitializer(BasePlatformInitializer):
    def initialize(self):
        # Make sure there is a DISPLAY environment variable and that it is set correctly
        if not 'DISPLAY' in os.environ:
            print("Env variable DISPLAY is missing. Setting it to ':0'")
            os.environ['DISPLAY'] = ':0'
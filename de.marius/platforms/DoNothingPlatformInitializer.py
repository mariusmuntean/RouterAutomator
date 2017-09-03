from BasePlatformInitializer import BasePlatformInitializer
from Logger import Logger


class DoNothingPlatformInitializer(BasePlatformInitializer):
    def initialize(self):
        Logger.logInfo("No initialization needed for this platform")

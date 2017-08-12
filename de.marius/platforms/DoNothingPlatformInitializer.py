from BasePlatformInitializer import BasePlatformInitializer


class DoNothingPlatformInitializer(BasePlatformInitializer):
    def initialize(self):
        print("No initialization needed for this platform")
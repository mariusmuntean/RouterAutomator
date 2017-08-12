from abc import ABC, abstractclassmethod


class BasePlatformInitializer(ABC):
    @abstractclassmethod
    def initialize(self):
        """
        Perform platform-specific initialization
        """
        pass

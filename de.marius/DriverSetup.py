import platform
import sys
from enum import Enum

from Logger import Logger
from platforms.raspbian.RaspbianGeckoDriverCopy import RaspbianGeckDriverCopy

from BasePlatformInitializer import BasePlatformInitializer
from platforms.linux.DesktopLinuxPlatformInitializer import DesktopLinuxPlatformInitializer
from platforms.linux.DesktopLinuxGeckoDriverCopy import LinuxGeckDriverCopy
from platforms.macOS.MacOSGeckoDriverCopy import MacOSGeckDriverCopy
from platforms.DoNothingPlatformInitializer import DoNothingPlatformInitializer
from platforms.raspbian.RaspbianPlatformInitializer import RaspbianPlatformInitializer


class Platform(Enum):
    """
    Represents the OS and CPU architecture as a 'Platform'
    """
    macOS = 1
    win_32 = 2
    win_64 = 3
    linux_32 = 4
    raspbian = 5


class DriverSetup():
    def init(self):
        """
        Makes sure the platform-specific web driver is available to Selenium and that any platform-specific initialization is performed
        """
        currentPlatform = self.getCurrentPlatform()
        Logger.logInfo("Discovered platform: " + str(currentPlatform))

        geckoDriverCopy = self.getGeckoDriverCopy(currentPlatform)
        self.driverPath = geckoDriverCopy.copy()

        platformInitializer = self.getPlatformInitializer(currentPlatform)
        platformInitializer.initialize()

    def getCurrentPlatform(self) -> Platform:
        """
        Determines the current platform (operating system and CPU architecture)

        :return: An Enum value from Platform
        """
        if sys.platform == "darwin":
            (release, version, machine) = platform.mac_ver()
            return Platform.macOS

        if sys.platform == "linux":
            (distName, version, id) = platform.linux_distribution()
            if distName == "debian":
                return Platform.raspbian
            else:
                return Platform.linux_32
        # Untested
        if sys.platform == "win32":
            # distName, version, id = platform._linux_distribution()
            return Platform.win32

    def getGeckoDriverCopy(self, platform: Platform):
        """
        Given a supported platform it returns a concrete instance of BaseGeckoDriverCopy
        :param platform: The current platform
        :return: an instance of BaseGeckoDriverCopy
        """
        if platform == Platform.macOS:
            return MacOSGeckDriverCopy()
        elif platform == Platform.linux_32:
            return LinuxGeckDriverCopy()
        elif platform == Platform.raspbian:
            return RaspbianGeckDriverCopy()

    def getPlatformInitializer(self, platform: Platform) -> BasePlatformInitializer:
        if platform == Platform.macOS:
            return DoNothingPlatformInitializer()
        elif platform == Platform.linux_32:
            return DesktopLinuxPlatformInitializer()
        elif platform == Platform.raspbian:
            return RaspbianPlatformInitializer()
        else:
            return DoNothingPlatformInitializer()

    def getDriverPath(self) -> str:
        return self.driverPath

from enum import Enum

import sys
import platform

from LinuxGeckoDriverCopy import LinuxGeckDriverCopy
from MacOSGeckoDriverCopy import MacOSGeckDriverCopy


class Platform(Enum):
    macOS = 1
    win64 = 2
    win32 = 3
    linux = 4
    arm7hf = 5


class DriverSetup():
    def getCurrentPlatform(self):
        """
        Determines the current platform(operating system)

        :return: An Enum value from Platform
        """
        if sys.platform == "darwin":
            (release, version, machine) = platform.mac_ver()
            print("macOS: " + release)
            return Platform.macOS

        if sys.platform == "linux":
            (distName, version, id) = platform._linux_distribution()
            print("Linux " + distName)
            if distName == "raspbian":
                return Platform.arm7hf
            else:
                return Platform.linux

        if sys.platform == "win32":
            distName, version, id = platform._linux_distribution()
            return Platform.win32

    def getGeckoDriverCopy(self, platform):
        """
        Given a supported platform it returns a concrete instance of BaseGeckoDriverCopy
        :param platform: The current platform
        :return: an instance of BaseGeckoDriverCopy
        """
        if platform == Platform.macOS:
            return MacOSGeckDriverCopy()
        elif platform == Platform.linux:
            return LinuxGeckDriverCopy()

    def init(self):
        """
        Makes sure the platform-specific web driver is available to Selenium
        """
        currentPlatform = self.getCurrentPlatform()
        geckoDriverCopy = self.getGeckoDriverCopy(currentPlatform)
        geckoDriverCopy.copy()

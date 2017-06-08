import platform
from enum import Enum
from sys import platform

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
        if platform == "darwin":
            return Platform.macOS

        if platform == "linux":
            distName, version, id = platform._linux_distribution()
            print("Linux", platform._linux_distribution())
            if distName == "raspbian":
                return Platform.arm7hf
            else:
                return Platform.linux

        if platform == "win32":
            distName, version, id = platform._linux_distribution()
            return Platform.win32

    def getGeckoDriverCopy(self, platform):
        if platform == Platform.macOS:
            return MacOSGeckDriverCopy()
        elif platform == Platform.linux:
            return LinuxGeckDriverCopy()

    def init(self):
        # Put the platform-specific driver in the PATH
        currentPlatform = self.getCurrentPlatform()
        geckoDriverCopy = self.getGeckoDriverCopy(currentPlatform)
        geckoDriverCopy.copy()

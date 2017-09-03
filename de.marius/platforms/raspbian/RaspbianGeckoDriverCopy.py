import os
import subprocess
from pathlib import Path

from BaseGeckoDriverCopy import BaseGeckoDriverCopy
from Logger import Logger


class RaspbianGeckDriverCopy(BaseGeckoDriverCopy):
    def copy(self):

        expectedDriverPath = self.getDriverPath()
        Logger.logInfo("Using the gecko driver from: " + expectedDriverPath)

        gekoDriver = Path(expectedDriverPath)

        filePermissions = "755"
        os.chmod(expectedDriverPath, int(filePermissions, 8))

        # if not gekoDriver.is_file():
        #     shutil.copyfile("drivers/gecko/linux64/geckodriver", expectedDriverPath)
        #     os.chmod(expectedDriverPath, 0o755)

        return expectedDriverPath

    def getDriverPath(self):
        output = subprocess.Popen(['cat', '/proc/cpuinfo'], stdout=subprocess.PIPE).communicate()[0]
        if output.find("ARMv6".encode()) != -1:
            return "drivers/gecko/arm6hf/geckodriver"
        else:
            return "drivers/gecko/arm7hf/geckodriver"
            # return "drivers/chrome/arm6/chromedriver"

import os
import shutil
from pathlib import Path

from BaseGeckoDriverCopy import BaseGeckoDriverCopy


class MacOSGeckDriverCopy(BaseGeckoDriverCopy):
    def copy(self):
        expectedDriverPath = "/usr/local/bin/geckodriver"
        gekoDriver = Path(expectedDriverPath)
        if not gekoDriver.is_file():
            shutil.copyfile("drivers/gecko/macOS/geckodriver", expectedDriverPath)
            filePermissions = "755"
            os.chmod(expectedDriverPath, int(filePermissions, 8))
            print("Gecko driver was copied to "
                  + expectedDriverPath
                  + " and its permissions were set to " + filePermissions)
        else:
            print("Gecko driver already present")

        return expectedDriverPath

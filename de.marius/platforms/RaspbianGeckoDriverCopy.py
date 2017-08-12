import os
from pathlib import Path

from BaseGeckoDriverCopy import BaseGeckoDriverCopy


class RaspbianGeckDriverCopy(BaseGeckoDriverCopy):
    def copy(self):
        expectedDriverPath = "drivers/gecko/arm6hf/geckodriver"
        gekoDriver = Path(expectedDriverPath)

        filePermissions = "755"
        os.chmod(expectedDriverPath, int(filePermissions, 8))

        # if not gekoDriver.is_file():
        #     shutil.copyfile("drivers/gecko/linux64/geckodriver", expectedDriverPath)
        #     os.chmod(expectedDriverPath, 0o755)

        return expectedDriverPath
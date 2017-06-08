import os
import shutil
from pathlib import Path

from BaseGeckoDriverCopy import BaseGeckoDriverCopy


class LinuxGeckDriverCopy(BaseGeckoDriverCopy):
    def copy(self):
        expectedDriverPath = "/usr/local/bin/geckodriver"
        gekoDriver = Path(expectedDriverPath)
        if not gekoDriver.is_file():
            shutil.copyfile("drivers/geko/macOS/geckodriver", expectedDriverPath)
            os.chmod(expectedDriverPath, 0o755)
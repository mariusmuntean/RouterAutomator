from BaseGeckoDriverCopy import BaseGeckoDriverCopy


class Win64GeckoDriverCopy(BaseGeckoDriverCopy):
    def copy(self) -> str:
        return "drivers/gecko/win64/geckodriver.exe"
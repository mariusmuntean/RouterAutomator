from BaseGeckoDriverCopy import BaseGeckoDriverCopy


class Win32GeckoDriverCopy(BaseGeckoDriverCopy):
    def copy(self) -> str:
        return "drivers/gecko/win32/geckodriver.exe"
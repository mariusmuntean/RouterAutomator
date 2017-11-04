import sys

from abc import ABC, abstractmethod

sys.path.append("../../selenium-3.4.3")

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BaseRouter(ABC):
    def __init__(self, webDriver: webdriver, webinterfaceUrl: str):
        self.webinterfaceUrl = webinterfaceUrl # type: str
        self.webdriver = webDriver  # type: webdriver
        self.driverWait = WebDriverWait(self.webdriver, 200) # type: WebDriverWait

    @abstractmethod
    def logIn(self, username, password):
        """
        Logs into the router's webinterface with the given credentials

        :param username:
        :param password:
        """
        pass

    @abstractmethod
    def reboot(self, password):
        """
        Reboots the router. First call logIn()
        :param password:
        """
        pass

    @abstractmethod
    def logOut(self):
        """
        Logs out of the router#s webinterface
        """
        pass

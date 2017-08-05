import sys

from abc import ABC, abstractmethod

sys.path.append("../../selenium-3.4.3")

from selenium import webdriver


class BaseRouter(ABC):
    def __init__(self, webDriver: webdriver, webinterfaceUrl):
        self.webinterfaceUrl = webinterfaceUrl
        self.webdriver = webDriver  # type: webdriver

    @abstractmethod
    def logIn(self, username, password):
        """
        Logs into the router's webinterface with the given credentials

        :param username:
        :param password:
        """
        pass

    @abstractmethod
    def reboot(self):
        """
        Reboots the router. First call logIn()
        """
        pass

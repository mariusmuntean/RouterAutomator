import sys

from routers.ArcherC2 import ArcherC2
from routers.ArcherC7 import ArcherC7
from routers.BaseRouter import BaseRouter
from selenium.common.exceptions import NoSuchElementException

sys.path.append("selenium-3.4.3")

from selenium import webdriver


class RouterFactory():
    def __init__(self, webdriver: webdriver, webinterfaceUrl):
        self.webinterfaceUrl = webinterfaceUrl
        self.webdriver = webdriver

    def isArcherC7(self) -> bool:
        try:
            c7 = "Model No. Archer C7" in self.webdriver.find_element_by_class_name("topLogo").text
        except NoSuchElementException:
            c7 = False
        return c7

    def isArcherC2(self):
        try:
            print(self.webdriver.find_element_by_id("mnum").text)
            c2 = "Model No. Archer C2" == self.webdriver.find_element_by_id("mnum").text
        except NoSuchElementException:
            c2 = False
        return c2

    def getRouter(self) -> BaseRouter:
        self.webdriver.get(self.webinterfaceUrl)
        if self.isArcherC7():
            return ArcherC7(self.webdriver, self.webinterfaceUrl)
        if self.isArcherC2():
            return ArcherC2(self.webdriver, self.webinterfaceUrl)

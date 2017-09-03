import sys

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from routers.ArcherC2 import ArcherC2
from routers.ArcherC7 import ArcherC7
from routers.BaseRouter import BaseRouter
from selenium.common.exceptions import NoSuchElementException, TimeoutException

sys.path.append("selenium-3.4.3")

from selenium import webdriver


class RouterFactory():
    def __init__(self, webdriver: webdriver, webinterfaceUrl):
        self.webinterfaceUrl = webinterfaceUrl
        self.webdriver = webdriver

    def isArcherC7(self) -> bool:
        try:
            wait = WebDriverWait(self.webdriver, 5)
            c7 = "Model No. Archer C7" in wait.until(EC.presence_of_element_located((By.CLASS_NAME, "topLogo"))).text
        except NoSuchElementException:
            c7 = False
        except TimeoutException:
            c7 = False
        return c7

    def isArcherC2(self):
        try:
            wait = WebDriverWait(self.webdriver, 5)
            c2 = "Model No. Archer C2" in wait.until(EC.presence_of_element_located((By.ID, "mnum"))).text
        except NoSuchElementException:
            c2 = False
        except TimeoutException:
            c2 = False
        return c2

    def getRouter(self) -> BaseRouter:
        self.webdriver.get(self.webinterfaceUrl)
        if self.isArcherC7():
            return ArcherC7(self.webdriver, self.webinterfaceUrl)
        if self.isArcherC2():
            return ArcherC2(self.webdriver, self.webinterfaceUrl)

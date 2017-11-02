import sys


sys.path.append("../../selenium-3.4.3")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from routers.ArcherC2 import ArcherC2
from routers.ArcherC7 import ArcherC7
from routers.OpenWrtLuCi import OpenWrtLuCi
from routers.BaseRouter import BaseRouter

sys.path.append("selenium-3.4.3")

from selenium.common.exceptions import NoSuchElementException, TimeoutException


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

    def isOpenWrtLuCi(self):
        try:
            wait = WebDriverWait(self.webdriver, 5)
            footer = wait.until(EC.presence_of_element_located((By.TAG_NAME,'footer')))
            hyperlink = footer.find_element(By.TAG_NAME,'a')
            return "Powered by LuCI" in hyperlink.text

            # Powered by LuCI
        except NoSuchElementException:
            luci = False
        except TimeoutError:
            luci = False
        return luci

    def getRouter(self) -> BaseRouter:
        self.webdriver.get(self.webinterfaceUrl)
        if self.isArcherC7():
            return ArcherC7(self.webdriver, self.webinterfaceUrl)
        if self.isArcherC2():
            return ArcherC2(self.webdriver, self.webinterfaceUrl)
        if self.isOpenWrtLuCi():
            return OpenWrtLuCi(self.webdriver, self.webinterfaceUrl)

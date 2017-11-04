import sys

sys.path.append("../../selenium-3.4.3")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from routers.ArcherC2 import ArcherC2
from routers.ArcherC7 import ArcherC7
from routers.OpenWrtLuCi import OpenWrtLuCi
from routers.CiscoEPC3925 import CiscoEPC3925
from routers.BaseRouter import BaseRouter

sys.path.append("selenium-3.4.3")

from selenium.common.exceptions import NoSuchElementException, TimeoutException

from selenium import webdriver


class RouterFactory():
    def __init__(self, webdriver: webdriver, webinterfaceUrl):
        self.webinterfaceUrl = webinterfaceUrl
        self.webdriver = webdriver
        self.wait = WebDriverWait(self.webdriver, 2)

    def isArcherC7(self) -> bool:
        try:
            c7 = "Model No. Archer C7" in self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "topLogo"))).text
        except NoSuchElementException:
            c7 = False
        except TimeoutException:
            c7 = False
        return c7

    def isArcherC2(self):
        try:
            c2 = "Model No. Archer C2" in self.wait.until(EC.presence_of_element_located((By.ID, "mnum"))).text
        except NoSuchElementException:
            c2 = False
        except TimeoutException:
            c2 = False
        return c2

    def isOpenWrtLuCi(self):
        try:
            footer = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, 'footer')))
            hyperlink = footer.find_element(By.TAG_NAME, 'a')
            return "Powered by LuCI" in hyperlink.text

            # Powered by LuCI
        except NoSuchElementException:
            luci = False
        except TimeoutException:
            luci = False
        return luci

    def isCiscoEPC3925(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='Lmodel' and text()[contains(.,'EPC3925')]]")))
            # self.wait.until(EC.presence_of_element_located((By.XPATH, "//td[@class='Lmodel' and contains(text()='EPC3925')]")))
            cisco = True
        except NoSuchElementException:
            cisco = False
        except TimeoutException:
            cisco = False
        return cisco

    def getRouter(self) -> BaseRouter:
        self.webdriver.get(self.webinterfaceUrl)
        if self.isArcherC7():
            return ArcherC7(self.webdriver, self.webinterfaceUrl)
        if self.isArcherC2():
            return ArcherC2(self.webdriver, self.webinterfaceUrl)
        if self.isOpenWrtLuCi():
            return OpenWrtLuCi(self.webdriver, self.webinterfaceUrl)
        if self.isCiscoEPC3925():
            return CiscoEPC3925(self.webdriver, self.webinterfaceUrl)

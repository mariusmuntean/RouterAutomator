import sys

from routers.ArcherC7 import ArcherC7
from routers.BaseRouter import BaseRouter

sys.path.append("selenium-3.4.3")

from selenium import webdriver

from DriverSetup import DriverSetup

DriverSetup().init()

webInterfaceUrl = "http://192.168.0.3/";


class RouterFactory():
    def __init__(self, webdriver: webdriver, webinterfaceUrl):
        self.webinterfaceUrl = webinterfaceUrl
        self.webdriver = webdriver

    def getRouter(self) -> BaseRouter:
        self.webdriver.get(self.webinterfaceUrl)
        if "Model No. Archer C7" in self.webdriver.find_element_by_class_name("topLogo").text:
            return ArcherC7(self.webdriver, self.webinterfaceUrl)


driver = webdriver.Firefox()

router = RouterFactory(driver, webInterfaceUrl).getRouter()
router.logIn("admin", "admin")
router.reboot()

# Scratchpad
# driver.switch_to_frame()

driver.close()

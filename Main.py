import sys

import time

sys.path.append("selenium-3.4.3")

from routers.RouterFactory import RouterFactory
from selenium import webdriver
from DriverSetup import DriverSetup

DriverSetup().init()

webInterfaceUrl = "http://192.168.0.2/";
username = "admin"
password = "admin"

driver = webdriver.Firefox()

time.sleep(5)
router = RouterFactory(driver, webInterfaceUrl).getRouter()
router.logIn(username, password)
router.reboot()

# Scratchpad
# driver.switch_to_frame()

driver.close()

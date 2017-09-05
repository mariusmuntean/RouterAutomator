import time

import sys
sys.path.append("../../selenium-3.4.3")

from Logger import Logger
from routers.BaseRouter import BaseRouter
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ArcherC2(BaseRouter):
    def logIn(self, username: str, password: str):
        usernameInput = self.webdriver.find_element_by_id("userName")
        usernameInput.clear()
        usernameInput.send_keys(username)

        passwordInput = self.webdriver.find_element_by_id("pcPassword")
        passwordInput.clear()
        passwordInput.send_keys(password)

        loginButton = self.webdriver.find_element_by_id("loginBtn")
        loginButton.click()
        time.sleep(2)

    def reboot(self):
        wait = WebDriverWait(self.webdriver, 200)

        menuFrame = wait.until(EC.presence_of_element_located((By.NAME, "bottomLeftFrame")))
        self.webdriver.switch_to_frame(menuFrame)

        wait.until(EC.presence_of_element_located((By.ID, "menu_tools"))).click()
        time.sleep(2)

        rebootSubMenuItem = wait.until(EC.presence_of_element_located((By.ID, "menu_restart")))
        rebootSubMenuItem.click()
        time.sleep(2)

        self.webdriver.switch_to_default_content()
        mainFrame = wait.until(EC.presence_of_element_located((By.NAME, "mainFrame")))
        self.webdriver.switch_to_frame(mainFrame)

        wait.until(EC.presence_of_element_located((By.ID, "button_reboot"))).click()
        time.sleep(1)

        self.webdriver.switch_to_alert().accept()
        Logger.logInfo("Router rebooting")

        time.sleep(4)

    def logOut(self):
        wait = WebDriverWait(self.webdriver, 200)

        menuFrame = wait.until(EC.presence_of_element_located((By.NAME, "bottomLeftFrame")))
        self.webdriver.switch_to_frame(menuFrame)

        wait.until(EC.presence_of_element_located((By.ID, "menu_logout"))).click()

        self.webdriver.switch_to_alert().accept()

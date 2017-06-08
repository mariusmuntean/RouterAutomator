import time

from routers.BaseRouter import BaseRouter

from selenium import webdriver
from selenium.webdriver.common.by import By


class ArcherC7(BaseRouter):
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
        menuFrame = self.webdriver.find_element_by_name("bottomLeftFrame")
        self.webdriver.switch_to_frame(menuFrame)

        systemToolsMenuItem = self.webdriver.find_element_by_id("a64")
        systemToolsMenuItem.click()
        time.sleep(2)

        rebootSubMenuItem = self.webdriver.find_element_by_id("a70")
        rebootSubMenuItem.click()
        time.sleep(2)

        self.webdriver.switch_to_default_content()
        mainFrame = self.webdriver.find_element_by_name("mainFrame")
        self.webdriver.switch_to_frame(mainFrame)

        rebootButton = self.webdriver.find_element_by_id("reboot")
        rebootButton.click()
        time.sleep(1)

        self.webdriver.switch_to_alert().accept()
        time.sleep(4)

        print("Router rebooting")

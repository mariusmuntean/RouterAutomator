import time

from routers.BaseRouter import BaseRouter

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        # time.sleep(2)

    def reboot(self):
        # f = open("/home/pi/RouterAutomator/page.html", 'w+')
        # f.write(self.webdriver.page_source)

        menuFrame = self.webdriver.find_element_by_name("bottomLeftFrame")
        self.webdriver.switch_to_frame(menuFrame)

        # wait = WebDriverWait(self.webdriver, 100)
        # wait.until(EC.presence_of_element_located((By.ID, "menu_tools"))).click()

        systemToolsMenuItem = self.webdriver.find_element_by_id("menu_tools")
        # systemToolsMenuItem = self.webdriver.find_element_by_xpath("//*[contains(text(), 'System Tools')]")
        systemToolsMenuItem.click()
        # time.sleep(2)

        rebootSubMenuItem = self.webdriver.find_element_by_id("menu_restart")
        rebootSubMenuItem.click()
        # time.sleep(2)

        self.webdriver.switch_to_default_content()
        mainFrame = self.webdriver.find_element_by_name("mainFrame")
        self.webdriver.switch_to_frame(mainFrame)

        rebootButton = self.webdriver.find_element_by_id("button_reboot")
        rebootButton.click()
        # time.sleep(1)

        self.webdriver.switch_to_alert().accept()
        print("Router rebooting")

        time.sleep(4)


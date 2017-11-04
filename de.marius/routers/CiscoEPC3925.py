from routers.BaseRouter import BaseRouter

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert


class CiscoEPC3925(BaseRouter):
    def logOut(self):
        logOffTab = self.driverWait.until(EC.presence_of_element_located((By.ID,'div_maintab_8'))) # type: WebElement
        logOffTab.click()

    def logIn(self, username, password):
        usernameInput = self.driverWait.until(EC.presence_of_element_located((By.NAME, 'username_login')))  # type: WebElement
        usernameInput.click()
        usernameInput.clear()
        usernameInput.send_keys(username)

        passwordInput = self.driverWait.until(EC.presence_of_element_located((By.ID, 'password_login')))  # type: WebElement
        passwordInput.clear()
        passwordInput.click()
        passwordInput.send_keys(password)

        logInButton = self.driverWait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='login' and @type='submit']")))  # type: WebElement
        logInButton.click()

    def reboot(self, password):
        # Click the Administration tab
        administrationTab = self.driverWait.until(EC.presence_of_element_located((By.ID,'div_maintab_5'))) # type: WebElement
        administrationTab.click()

        # Click the Device restart subtab
        deviceRestartSubTab = self.driverWait.until(EC.presence_of_element_located((By.ID, "div_subtab_3"))) # type: WebElement
        deviceRestartSubTab.click()

        # Fill in the administrator password
        adminPasswordInput = self.driverWait.until(EC.presence_of_element_located((By.ID,'devicerestrat_Password_check'))) # type: Input
        adminPasswordInput.send_keys(password)

        # Click Device Restart button
        deviceRestartButton = self.driverWait.until(EC.presence_of_element_located((By.NAME,'mtenRestore'))) # type: WebElement
        deviceRestartButton.click()

        # Confirm in the Alert that pops up
        confirmationAlert = self.driverWait.until(EC.alert_is_present()) # type: Alert
        confirmationAlert.accept()

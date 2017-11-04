import sys

sys.path.append("../../selenium-3.4.3")

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from routers.BaseRouter import BaseRouter


class OpenWrtLuCi(BaseRouter):
    def logIn(self, username, password):
        usernameInput = self.driverWait.until(EC.presence_of_element_located((By.NAME, "luci_username")))

        usernameInput.click()
        usernameInput.clear()
        usernameInput.send_keys(username)

        passwordInput = self.driverWait.until(EC.presence_of_element_located((By.NAME, "luci_password")))

        passwordInput.click()
        passwordInput.clear()
        passwordInput.send_keys(password)

        loginButton = self.driverWait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and contains(@class,'cbi-button')]")))
        loginButton.click()

    def reboot(self, password):
        rebootUrl = self.webinterfaceUrl + "/cgi-bin/luci/admin/system/reboot"
        self.webdriver.get(rebootUrl)

        rebootButton = self.driverWait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='button' and contains(@class,'cbi-button')]")))
        rebootButton.click()

    def logOut(self):
        logoutUrl = self.webinterfaceUrl + "/cgi-bin/luci/admin/logout"
        self.webdriver.get(logoutUrl)

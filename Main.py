import sys
import time

sys.path.append("selenium-3.4.3")

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from DriverSetup import DriverSetup

DriverSetup().init()

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
time.sleep(3)
assert "No results found." not in driver.page_source
time.sleep(5)
driver.close()

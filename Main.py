import sys

import time
import os
from configparser import ConfigParser

sys.path.append("de.marius")

from routers.BaseRouter import BaseRouter

sys.path.append("selenium-3.4.3")

from routers.RouterFactory import RouterFactory
from selenium import webdriver
from DriverSetup import DriverSetup


def initConfig():
    config = ConfigParser()
    configPath = os.path.join(os.getcwd(), "Config.ini")
    config.read(filenames=configPath)
    sections = config.sections();
    if len(sections) == 0 or (not sections.__contains__("actions")):
        print("Config file is empty. Bye!")
        quit()
    if len(config.items("actions")) == 0:
        print("Nothing to do. Bye!")
        quit()
    return config


def handleRouterTask(router: BaseRouter, username: str, password: str, task: str):
    # ToDo: this can be done a lot nicer

    if task == 'login':
        router.logIn(username, password)
    elif task == 'reboot':
        router.reboot()


def performActions(driverPath: str, config: ConfigParser, actions):
    for action in actions:
        webInterfaceUrl = config.get(action, "routerIP")
        username = config.get(action, "username")
        password = config.get(action, "password")
        tasks = config.get(action, "tasks")
        tasks = [task.strip() for task in tasks.split(',')]
        print("IP: " + webInterfaceUrl
              + " username: " + username
              + " password: " + password
              + " tasks: " + tasks.__str__())

        driver = webdriver.Firefox(executable_path=driverPath)
        router = RouterFactory(driver, webInterfaceUrl).getRouter()
        for task in tasks:
            handleRouterTask(router, username, password, task)
            time.sleep(1)
        driver.close()


# Initialize the webdriver
driverSetup = DriverSetup()
driverSetup.init()

# Parse the Config
config = initConfig()

# Run any active actions
activeActionTuples = filter(lambda action: action[1] == 'true', config.items("actions"))
activeActionNames = map(lambda action: action[0], activeActionTuples)
performActions(driverSetup.getDriverPath(), config, activeActionNames)

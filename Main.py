import os
import sys
from configparser import ConfigParser


sys.path.append("de.marius")
sys.path.append("selenium-3.4.3")

from routers.BaseRouter import BaseRouter


from routers.RouterFactory import RouterFactory
from selenium import webdriver
from DriverSetup import DriverSetup
from Logger import Logger, LogLevel


def initConfig():
    config = ConfigParser()
    configPath = os.path.join(os.getcwd(), "Config.ini")
    config.read(filenames=configPath)
    sections = config.sections();
    if len(sections) == 0 or (not sections.__contains__("actions")):
        Logger.logInfo("Config file is empty. Bye!")
        quit()
    if len(config.items("actions")) == 0:
        Logger.logInfo("Nothing to do. Bye!")
        quit()
    return config


def handleRouterTask(router: BaseRouter, username: str, password: str, task: str):
    # ToDo: this can be done a lot nicer

    if task == 'login':
        router.logIn(username, password)
    elif task == 'reboot':
        router.reboot()
    elif task == 'logout':
        router.logOut()


def performActions(driverPath: str, config: ConfigParser, actions):
    Logger.logInfo("")
    for action in actions:
        Logger.logInfo("Performing action: " + action)
        webInterfaceUrl = config.get(action, "routerIP")
        username = config.get(action, "username")
        password = config.get(action, "password")
        tasks = config.get(action, "tasks")
        tasks = [task.strip() for task in tasks.split(',')]
        Logger.logInfo("IP: " + webInterfaceUrl
                       + " username: " + username
                       + " password: " + password
                       + " tasks: " + tasks.__str__())

        driver = webdriver.Firefox(executable_path=driverPath)
        router = RouterFactory(driver, webInterfaceUrl).getRouter()
        for task in tasks:
            handleRouterTask(router, username, password, task)
            Logger.logInfo("Performed task: " + task)
        driver.close()
        Logger.logInfo("Finished action: " + action)
    Logger.logInfo("##### Router Automator Done #####")
    Logger.logInfo("")


# Initialize logging
Logger.init("RouterAutomator.log", LogLevel.INFO)

# Initialize the webdriver
Logger.logInfo("")
Logger.logInfo("####### Router Automator #######")
driverSetup = DriverSetup()
driverSetup.init()

# Parse the Config
config = initConfig()

# Run any active actions
activeActionTuples = filter(lambda action: action[1] == 'true', config.items("actions"))
activeActionNames = map(lambda action: action[0], activeActionTuples)
performActions(driverSetup.getDriverPath(), config, activeActionNames)

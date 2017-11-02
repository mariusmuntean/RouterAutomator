import os
import sys
sys.path.append("de.marius")
sys.path.append("selenium-3.4.3")


from configparser import ConfigParser

from selenium.common.exceptions import WebDriverException


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
            tryHandleRouterTask(password, router, task, username)
        driver.close()
        Logger.logInfo("Finished action: " + action)
        Logger.logInfo("")
    Logger.logInfo("##### Router Automator Done #####")
    Logger.logInfo("")


def tryHandleRouterTask(password, router, task, username):
    try:
        handleRouterTask(router, username, password, task)
    except WebDriverException as wde:
        Logger.logError("Performing task '" + task + "' produced exception: " + wde.__str__())
    except:
        Logger.logError("Unknown exception while performing task '" + task + "'")
    finally:
        Logger.logInfo("Performed task: " + task)


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

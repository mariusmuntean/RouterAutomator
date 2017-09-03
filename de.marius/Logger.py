import logging
from enum import Enum


class LogLevel(Enum):
    INFO = 1
    DEBUG = 2
    WARNING = 3
    ERROR = 4


class Logger:
    @staticmethod
    def init(logFileName: str, logLevel: LogLevel):
        """
        Initialize the logging in RouterAutomator.

        :param logFileName: The name of the log file, i.e. "whatHappens.log".
        :param logLevel: The logging level. See the LogLevel enum
        """
        if logFileName == None:
            logFileName = "RouterAutomator.log"

        internalLoggingLevel = logging.INFO
        if logLevel == LogLevel.DEBUG:
            internalLoggingLevel = logging.DEBUG
        elif logLevel == LogLevel.INFO:
            internalLoggingLevel = logging.INFO
        elif logLevel == LogLevel.WARNING:
            internalLoggingLevel = logging.WARNING
        elif logLevel == LogLevel.ERROR:
            internalLoggingLevel = logging.ERROR

        logging.basicConfig(filename=logFileName, level=internalLoggingLevel, format='%(asctime)s %(message)s')

    @staticmethod
    def log(logLevel: LogLevel, message: str):
        """
        Logs the provided message with the provided logging level
        :param logLevel: The logging level to use while logging
        :param message: The message to be logged
        """
        if logLevel == LogLevel.DEBUG:
            logging.debug(message)
        elif logLevel == LogLevel.INFO:
            logging.info(message)
        elif logLevel == LogLevel.WARNING:
            logging.warning(message)
        elif logLevel == LogLevel.ERROR:
            logging.error(message)

        print(message)

    @staticmethod
    def logDebug(message: str):
        """
        Logs a message with the log level DEBUG

        :param message: The message to be logged
        """
        Logger.log(LogLevel.DEBUG, message)

    @staticmethod
    def logInfo(message: str):
        """
        Logs a message with the log level INFO

        :param message: The message to be logged
        """
        Logger.log(LogLevel.INFO, message)

    @staticmethod
    def logWarning(message: str):
        """
        Logs a message with the log level WARNING

        :param message: The message to be logged
        """
        Logger.log(LogLevel.WARNING, message)

    @staticmethod
    def logError(message: str):
        """
        Logs a message with the log level ERROR

        :param message: The message to be logged
        """
        Logger.log(LogLevel.ERROR, message)

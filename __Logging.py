from datetime import datetime
import logging
import os
from appium import webdriver
from __Utils import get_logpath

final_directory = get_logpath()
loggerPath = final_directory + datetime.now().strftime('/YouTube_Automation_%H_%M_%S_%d_%m_%Y.log')

logger = logging.getLogger(loggerPath)
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh = logging.FileHandler(loggerPath)
fh.setLevel(logging.DEBUG)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.ERROR)

# create formatter and add it to the handlers
logging.Formatter
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add the handlers to logger
logger.addHandler(ch)
logger.addHandler(fh)

class log():

    def set_logpath(self):
        loggerPath=self

    def warn(msg):
        logger.warning(msg)

    def error(msg):
        logger.error(msg)

    def info(msg):
        logger.info(msg)

    def debug(msg):
        logger.debug(msg)

    def screenshotpath(filename):
        return final_directory+"/"+filename+".png"

    def starttestcase(msg):
        logger.info("----------------------------------------------------------------------------------------")
        logger.info("                                 Test Case Start                                        ")
        logger.info("                      Test Case Name : " + msg + "                                      ")
        logger.info("----------------------------------------------------------------------------------------")

    def stoptestcase(self):
        logger.info("----------------------------------------------------------------------------------------")
        logger.info("                                 Test Case End                                          ")
        logger.info("----------------------------------------------------------------------------------------")

    def markTestPass (msg):
        logger.info("Test Case Pass" + msg)

    def markTestfail(msg):
        logger.error("Test Case fail " + msg)

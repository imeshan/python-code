import os
import unittest
from pyunitreport import HTMLTestRunner
from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from __Logging import log
from __Utils import parseCapabilities

class Login(unittest.TestCase):

    def setUp(self):
        ueCap = parseCapabilities()
        appiumserverurl = 'http://'+ueCap[3]+':'+ueCap[4]+'/wd/hub'
        log.info("Using Appium Server Url" + appiumserverurl)

        desired_caps = {'platformName': ueCap[0], 'platformVersion': ueCap[1], 'deviceName': ueCap[2],
                        'appPackage': 'com.google.android.youtube', 'appActivity': '.HomeActivity'}

        log.info(desired_caps)
        self.driver = webdriver.Remote(appiumserverurl, desired_caps)
        sleep(10)

    def test_login(self):
        log.starttestcase("test_login")
        ell = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Account']")
        actions = TouchAction(self.driver)
        actions.tap(ell)
        actions.perform()

        log.debug("Account page is Visiable")
        sleep(5)
        self.driver.save_screenshot(log.screenshotpath("Accoun page"))
        w = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView").is_displayed()
        sleep(5)
        log.debug("Switch Account")
        self.driver.save_screenshot(log.screenshotpath("Switch account"))

        sw = self.driver.find_element_by_xpath("	/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]/android.widget.RelativeLayout/android.widget.TextView")
        actions = TouchAction(self.driver)
        actions.tap(sw)
        actions.perform()
        sleep(5)
        log.debug("Added accounts visiable")
        self.driver.save_screenshot(log.screenshotpath("Added accounts"))
        #Select Added Account

        #(1) Atleast 2 Account should be added in You Tube app for account switching.
        #(2) Change the content-desc in xpath below with your Account channel name Ex: "Eshan varma"

        ac = self.driver.find_element_by_xpath("//android.widget.LinearLayout[@content-desc='Eshan varma']")
        actions = TouchAction(self.driver)
        actions.tap(ac)
        actions.perform()
        log.debug("selected the added accout, account changed")
        sleep(5)
        self.driver.save_screenshot(log.screenshotpath("Account changed screenshot"))


        #Sign Out
        ell= self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Account']")
        actions = TouchAction(self.driver)
        actions.tap(ell)
        actions.perform()
        log.debug("Switch Account")
        sleep(5)
        self.driver.save_screenshot(log.screenshotpath("Switch account"))
        w = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView").is_displayed()
        log.debug("Account page displayed")
        sw = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]")
        actions = TouchAction(self.driver)
        actions.tap(sw)
        actions.perform()
        sleep(5)
        sg = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView")
        actions = TouchAction(self.driver)
        actions.tap(sg)
        actions.perform()
        log.debug("Account is in sign out mode")
        sleep(5)
        self.driver.save_screenshot(log.screenshotpath("sign out mode"))
        log.stoptestcase(self)

    def tearDown(self):
        self.driver.quit()

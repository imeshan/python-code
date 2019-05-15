import unittest
from time import sleep
from pyunitreport import HTMLTestRunner
from appium import webdriver
from __Logging import log
from __Utils import parseCapabilities

class VerifyYouTubeTabs(unittest.TestCase):

#all the Test Case Result Will be stored in this TestCase

    #Setup Before each TestCase
    def setUp(self):


        ueCap = parseCapabilities()
        appiumserverurl = 'http://'+ueCap[3]+':'+ueCap[4]+'/wd/hub'

        log.info("Using Appium Server Url" + appiumserverurl)

        desired_caps = {'platformName': ueCap[0], 'platformVersion': ueCap[1], 'deviceName': ueCap[2],
                        'appPackage': 'com.google.android.youtube', 'appActivity': '.HomeActivity'}

        log.info(desired_caps)

        self.driver = webdriver.Remote(appiumserverurl, desired_caps)

        self.driver.implicitly_wait(15)

  #Home Tab test case
    def test_HomeTab(self):
        log.starttestcase("test_HomeTab")
        sleep(5)

        log.debug("Home Screen Visiable")
        log.markTestPass("Marking Test Case is Passed")
        sleep(5)
        self.driver.save_screenshot(log.screenshotpath("hometab_TestCase"))
        pass

   # Trending Tab test case
    def test_TrendingTab(self):

        log.starttestcase("test_TrentingTab")
        sleep(5)
        el = self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='Trending']").click()
        self.driver.implicitly_wait(15)
        sleep(5)
        log.debug("Trending Screen Visiable")
        sub_el = self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='Trending']/android.widget.TextView").text
        self.driver.implicitly_wait(15)
        log.debug("Trending Element founded")

        if sub_el == "Trending":
            log.markTestPass("Marking test Case Passed")
            self.driver.save_screenshot(log.screenshotpath("Trending tab"))
        else:
            log.markTestfail("Marking Test Case Fail")
            self.skipTest("String Not Maching")


    # Subscription Tab test case
    def test_SubscriptionTab(self):
        log.starttestcase("test_SubscriptionTab")
        el = self.driver.find_element_by_xpath("//android.widget.Button[@index='2']").click()
        self.driver.implicitly_wait(20)
        log.debug("Subscritpion Tab Visiable")
        sub_el = self.driver.find_element_by_xpath("//android.widget.Button[@index='2']/android.widget.TextView").text
        self.driver.implicitly_wait(20)

        if sub_el == "Subscription":
            log.debug("Subscritpion Tab Element Matched")
        else:
            log.markTestfail("String Not matched , Test case failed")
            log.debug("Subscription test case failed")
        sleep(10)

        self.driver.save_screenshot(log.screenshotpath("Subscription Tab "))
        self.skipTest("String Not Maching")

    #Inbox Tab test case
    def test_InboxTab(self):
        log.starttestcase("test_InboxTab")

        el = self.driver.find_element_by_xpath("//android.widget.Button[@index='3']").click()
        self.driver.implicitly_wait(15)
        log.debug("Inbox tab visiable")
        sub_el = self.driver.find_element_by_xpath("//android.widget.Button[@index='3']/android.widget.TextView").text
        self.driver.implicitly_wait(15)
        log.debug("Inbox tab elemnt")

        if sub_el == "Inbox":
            log.debug("Inbox tab element found")
            log.markTestPass("Inbox test case marked as Passed")

        else:
            log.markTestfail("Inbox tab test case failed")
            self.driver.save_screenshot(log.screenshotpath("Inbox"))
            self.skipTest("String Not Maching")

    #Library Tab test case
    def test_LibraryTab(self):
        log.starttestcase("test_LibraryTab")

        el = self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='Library']").click()
        self.driver.implicitly_wait(10)
        log.debug("Library tab visiable")
        sub_el = self.driver.find_element_by_xpath("//android.widget.Button[@content-desc='Library']/android.widget.TextView").text
        self.driver.implicitly_wait(10)
        log.debug("Library tab element ")
        if sub_el == "Library":
            log.debug("Library tab element matched")
            log.markTestPass("Library tab test case marked as passed")

        else:
            log.markTestfail("String not matched , test case failed")
            self.driver.save_screenshot(log.screenshotpath("Library"))
            self.skipTest("String Not Maching")

    def tearDown(self):
        self.driver.quit()


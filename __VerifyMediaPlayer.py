# Standart Imports
import os
import unittest
from pyunitreport import HTMLTestRunner
from appium import webdriver
from time import sleep
from appium.webdriver.common.touch_action import TouchAction
from __Logging import log
from __Utils import parseCapabilities

class VerifyMediaPlayer(unittest.TestCase):

    # Setup Before each TestCase
    def setUp(self):
        ueCap = parseCapabilities()
        appiumserverurl = 'http://'+ueCap[3]+':'+ueCap[4]+'/wd/hub'
        log.info("Using Appium Server Url" + appiumserverurl)

        desired_caps = {'platformName': ueCap[0], 'platformVersion': ueCap[1], 'deviceName': ueCap[2],
                        'appPackage': 'com.google.android.youtube', 'appActivity': '.HomeActivity'}

        log.info(desired_caps)

        self.driver = webdriver.Remote(appiumserverurl, desired_caps)

        self.driver.implicitly_wait(15)

    #Play suggested video form home tab
    def test_Play(self):
        log.starttestcase("Test case starts")

        el = self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index= '0']")
        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()
        log.info("Video Started Playing")
        sleep(5)
        self.driver.save_screenshot(log.screenshotpath("video playback"))
        el = self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View")
        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()
        log.info("Touch Perform")


        current_time = self.driver.find_element_by_id("com.google.android.youtube:id/time_bar_current_time").text
        log.info("Video playback time")

        if "0.00" != current_time:

            log.info("playback time matches")

        else:
            log.info("Plackback time not matches")
            self.driver.save_screenshot(log.screenshotpath("Failed"))
            log.markTestfail("test case failed")
            self.skipTest("play back testcase failed")

    def test_pause(self):

        log.starttestcase("Test case starts")

        el = self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index= '0']")
        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()

        log.info("Video Started Playing")
        log.info("Halting the Test Case for 35 Seconds Expected Displaying the Advertishment")
        sleep(5)
        self.driver.save_screenshot(log.screenshotpath("video playback"))


        el = self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View")
        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()
        log.info("Touch Perform")

        sub_el = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Pause video']")
        actions = TouchAction(self.driver)
        actions.tap(sub_el)
        actions.perform()
        log.info("Video Paused")
        sleep(3)
        self.driver.save_screenshot(log.screenshotpath("Paused video"))


        # Next video
    def test_nextvideoplayback(self):

        log.starttestcase("Test case starts")
        #el = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Go to video' and @index = '1']")
        #el = self.driver.find_element_by_xpath("//android.widget.ImageView[@content-desc='Go to video']")
        el = self.driver.find_element_by_xpath("//android.widget.RelativeLayout[@index= '0']")
        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()
        log.info("Video Started Playing")
        sleep(10)
        self.driver.save_screenshot(log.screenshotpath("video playback"))

        ep = self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.RecyclerView/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[1]/android.widget.ImageView")
        actions = TouchAction(self.driver)
        actions.tap(ep)
        actions.perform()
        log.info("Suggested video starts playing")
        sleep(10)

        el = self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View")
        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()
        log.info("Touch Perform")

        nex = self.driver.find_element_by_accessibility_id("Next video")
        actions = TouchAction(self.driver)
        actions.tap(nex)
        actions.perform()
        log.info("Next Video played")
        self.driver.save_screenshot(log.screenshotpath("Next video played"))

        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()
        log.info("Touch Perform")

        current_time = self.driver.find_element_by_id("com.google.android.youtube:id/time_bar_current_time").text
        log.info("Current time")

        if "0:00" != current_time:
            log.info("Matching current time")

        else:
            log.info("current time not matched")
            log.markTestfail("test case failed")
            self.skipTest("play back testcase failed")

        sleep(2)

        el = self.driver.find_element_by_xpath("//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.View")
        actions = TouchAction(self.driver)
        actions.tap(el)
        actions.perform()
        log.info("Touch Perform")

        ele= self.driver.find_element_by_xpath("//android.widget.ImageView[@index= '5']")
        actions = TouchAction(self.driver)
        actions.tap(ele)
        actions.perform()
        log.info("Previous Video starts playing")
        self.driver.save_screenshot(log.screenshotpath("Previous video"))

        qw = self.driver.find_element_by_accessibility_id("Expand Mini Player")
        actions = TouchAction(self.driver)
        actions.tap(qw)
        actions.perform()
        log.info("Touch Perform for previous")

        current_time = self.driver.find_element_by_id("com.google.android.youtube:id/time_bar_current_time").text
        log.info("Current time")

        if "0:00" != current_time:
           log.info("Matching current time")

        else:

          log.info("current time not matched")
          log.markTestfail("test case failed")
          self.skipTest("play back testcase failed")

        sleep(5)

    def tearDown(self):
     self.driver.quit()

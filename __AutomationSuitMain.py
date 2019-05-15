import os
import unittest
from datetime import datetime
from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from __VerifyYouTubeTab import VerifyYouTubeTabs
from __VerifyMediaPlayer import VerifyMediaPlayer
from __VerifyPlayerFunctions import PlayerFunction
from __VerfiyLoginFunction import Login
from __Utils import get_logpath, parsetestsuits
from __Utils import parseCapabilities

if __name__ == '__main__':

    testsuitlist = parsetestsuits()
    suite = unittest.TestSuite()

    for x in testsuitlist:
        if x == "test_HomeTab":
            suite.addTest(VerifyYouTubeTabs('test_HomeTab'))
        elif x == "test_TrendingTab":
            suite.addTest(VerifyYouTubeTabs('test_TrendingTab'))
        elif x == "test_SubscriptionTab":
            suite.addTest(VerifyYouTubeTabs('test_SubscriptionTab'))
        elif x == "test_InboxTab":
            suite.addTest(VerifyYouTubeTabs('test_InboxTab'))
        elif x == "test_LibrartTab":
            suite.addTests(VerifyYouTubeTabs('test_TrendingTab'))
        elif x == "test_pause":
            suite.addTest(VerifyMediaPlayer('test_pause'))
        elif x == "test_nextvideoplayback":
            suite.addTest(VerifyMediaPlayer('test_nextvideoplayback'))
        elif x == "test_function":
            suite.addTest(PlayerFunction('test_function'))
        elif x == "test_login":
            suite.addTest(Login('test_login'))

    kwargs = {
        "output": get_logpath(),
        "report_name": datetime.now().strftime('YouTube_Automation_Report_%H_%M_%d_%m_%Y'),
        "failfast": True
    }
    runner = HTMLTestRunner(**kwargs)
    runner.run(suite)

import os
import unittest
import sys
from appium import webdriver
from time import sleep
import requests


class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"


    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        desired_caps['appActivity'] = '.ChessFreeActivity'
        desired_caps['deviceName'] = 'ZY222ZPZVW'
        desired_caps['app'] = 'C:\\Users\\dell store\\Desktop\\Chess Free.apk'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()

    def test_single_player_mode(self):
        "Test the Single Player mode launches correctly"
        element = self.driver.find_element_by_name("PLAY!")
        element.click()
        self.driver.find_element_by_name("Single Player").click()
        textfields = self.driver.find_elements_by_class_name("android.widget.TextView")
        self.assertEqual('MATCH SETTINGS', textfields[0].text)


# ---START OF SCRIPT

if __name__ == '__main__':
    unittest.main()

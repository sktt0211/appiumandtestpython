import unittest
from appium import webdriver

class Base:


    def __init__(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.0.2'
        desired_caps['deviceName'] = '32049a724e797175'
        desired_caps['appPackage'] = 'com.yibai.android.student'
        desired_caps['appActivity'] = 'ui.MainActivity'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['resetKeyboard'] = 'True'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


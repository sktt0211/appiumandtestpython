
import time
import unittest
from PO import Base
from appium import webdriver


class Login(Base.Base):

    def snapsot(self):
        self.driver.get_screenshot_as_file("C:\\Users\\ki\\Desktop\\test.png")

    def testApi(self):
        value = "11"
        time.sleep(1)

        self.driver.swipe(1550, 500, 10, 500)
        time.sleep(5)

        self.snapsot()

        self.driver.swipe(1550, 500, 10, 500)
        time.sleep(5)

        starbuttn = self.driver.find_element_by_id("guide_btn")
        starbuttn.click()
        time.sleep(1)

        elements = self.driver.find_elements_by_id("tab_name_textview")
        elements[0].click()
        elements[1].click()

        '''elements[2].click()
        elements[3].click()
        print(len(elements))
        self.assertEqual("11",value)'''
        loginbt = self.driver.find_element_by_id("btn_login")
        loginbt.click()

        lphone_ext = self.driver.find_element_by_id("phone_ext")
        lphone_ext.send_keys("13585559109")
        pwd_ext = self.driver.find_element_by_id("pwd_ext")
        pwd_ext.send_keys("123456")
        login_btn = self.driver.find_element_by_id("login_btn")
        login_btn.click()
        time.sleep(10)

    '''
            self.driver.tap([(200,400)])

            time.sleep(3)
            btn=self.driver.find_element_by_id("btn")
            btn.click()

            self.assertEqual("11", value)



    '''









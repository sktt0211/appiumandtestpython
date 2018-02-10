import unittest
import Login
import time
from appium import webdriver

class MyTestCase(Login.Login):




    def tearDown(self):
        self.driver.quit()


    def testMinestress(self):
        elements = self.driver.find_elements_by_id("tab_name_textview")
        elements[3].click()
        address_item=self.driver.find_element_by_id("address_item")
        address_item.click()
        time.sleep(4)
        city_txt=self.driver.find_element_by_id("city_txt")
        city_txt.click()
        time.sleep(4)
        provinces=self.driver.find_elements_by_id("id_province")
        provinces[2].click()
        time.sleep(4)
        value=11
        self.assertEqual("11", value)




if __name__ == '__main__':
    unittest.main()

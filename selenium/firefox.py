from selenium import webdriver

driver=webdriver.Firefox()

driver.maximize_window()
driver.get("https://www.baidu.com")

driver.quit()
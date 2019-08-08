from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import sys
import os
from selenium.webdriver.chrome.options import Options
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.Pages.homePage import HomePage
from POMDemo.Pages.LoginPage import LoginPage
from POMDemo.Pages.remoteWebdriver import Container

obj = Container
driver = obj._webdriver

# Testing selenium in headless mode
#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--no-sandbox")
url = 'http://192.168.0.102:31870/grid/console'
#url = 'http://192.168.99.100:30405'
driver = webdriver.Remote(command_executor=url,desired_capabilities=getattr(DesiredCapabilities, 'CHROME'))
#desired_capabilities=chrome_options.to_capabilities())

#driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver")
driver.get("https://google.com")
#driver.get("https://google.com)
print(driver.name)
driver.find_element_by_name("q").send_keys("Selenium Grid with docker and python")
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()

print('Test Completed')

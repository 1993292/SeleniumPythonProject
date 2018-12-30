from selenium import webdriver
import HtmlTestRunner
import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from POMDemo.Pages.homePage import HomePage
from POMDemo.Pages.LoginPage import LoginPage


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # cls.chrome_options = Options()
        # cls.chrome_options.add_argument("--headless")
        # cls.chrome_options.add_argument("--disable-extensions")
        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver")4
        cls.driver = webdriver.Chrome(executable_path="../../drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://www.facebook.com")
        login = LoginPage(driver)
        login.enter_username("pacsondialloni@yahoo.fr")
        login.enter_password("madrid")
        login.click_login()

        # homepage = HomePage(driver)
        # homepage.click_welcome()
        # homepage.click_logout()

    #     self.assertEqual(x, "Selenium Grid with docker and python - Recherche Google")
    #
    # def test_search_2(self):
    #     self.driver.get("https://google.com")
    #     print(self.driver.title)
    #     self.driver.find_element_by_name("q").send_keys("Building a kubernetes cluster on a raspberry pi3")
    #     self.driver.find_element_by_name("btnK").click()
    #     print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/pacson/PycharmProjects/Selenium/reportsUNT'))
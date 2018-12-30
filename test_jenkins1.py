from selenium import webdriver
import HtmlTestRunner
import pytest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
# from POMDemo.Pages.homePage import HomePage
from POMDemo.Pages.LoginPage import LoginPage
# changed
# reports folder added


class TestSample():

    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="drivers/chromedriver")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test completed")

    def test_login(self, test_setup):
        driver.get("https://www.facebook.com")
        login = LoginPage(driver)
        login.enter_username("pacsondialloni@yahoo.fr")
        login.enter_password("madrid")
        login.click_login()

    @pytest.mark.skip(reason="Not included in this test")
    def test_demo_skip_1(self):
        assert True

    # @pytest.mark.skipif(sys.version_info < (3.5), reason="python version must be higher than 3.4")
    def test_demo_skip_2(self):
        assert True

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

    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.close()
    #     cls.driver.quit()

# if __name__ == '__main__':
#     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='/home/pacson/PycharmProjects/Selenium/reportsUNT'))

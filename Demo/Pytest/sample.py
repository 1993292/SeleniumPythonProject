from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
#import HtmlTestRunner
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
    def test_setup(self, browser='CHROME'):
        global driver
       # driver = webdriver.Chrome(executable_path="../../drivers/chromedriver")
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--no-sandbox")
        url= 'http://157.159.15.84:30612'
        driver = webdriver.Remote(
            command_executor=url,
            desired_capabilities=getattr(DesiredCapabilities,browser))
            #desired_capabilities=chrome_options.to_capabilities())
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Browser %s checks out!" % browser)
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

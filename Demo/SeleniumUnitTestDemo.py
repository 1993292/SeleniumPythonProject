import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.chrome_options = Options()
        cls.chrome_options.add_argument("--headless")
        cls.chrome_options.add_argument("--disable-extensions")

        # self.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver")4
        cls.driver = webdriver.Chrome(executable_path="../drivers/chromedriver")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://google.com")
        print(self.driver.title)
        self.driver.find_element_by_name("q").send_keys("Selenium Grid with docker and python")
        self.driver.find_element_by_name("btnK").click()
        x = self.driver.title
        self.assertEqual(x, "Selenium Grid with docker and python - Recherche Google")
        self.driver.fi
    def test_search_2(self):
        self.driver.get("https://google.com")
        print(self.driver.title)
        self.driver.find_element_by_name("q").send_keys("Building a kubernetes cluster on a raspberry pi3")
        self.driver.find_element_by_name("btnK").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    @unittest.skip("This is a skipped test.")
    def test_skip(self):
        """ This test should be skipped. """
        pass

    # def test_something(self):
    #     self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Reports'), verbosity=2)

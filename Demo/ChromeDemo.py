from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# Testing selenium in headless mode
#chrome_options = webdriver.ChromeOptions()
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-extensions")

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver")
driver.get("https://google.com")
print(driver.title)
driver.find_element_by_name("q").send_keys("Selenium Grid with docker and python")
driver.find_element_by_name("btnK").click()
print(driver.title)
driver.close()
driver.quit()

print('Test Completed')

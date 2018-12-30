from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC

firefox_options = webdriver.FirefoxOptions()
#firefox_options.set_headless(headless=True)

path = "../drivers/geckodriver"
driver = webdriver.Firefox(executable_path=path)

# wait = WebDriverWait(driver, 10)
# element = wait.until(EC.element_to_be_clickable((By.NAME,'btnK')))

# driver.implicitly_wait(10)
#driver.implicitly_wait(2)
driver.get("https://google.com")
driver.find_element_by_name("q").send_keys("kubernetes on the raspiberry PI3")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)

time.sleep(2)
print(driver.title)
driver.close()
driver.quit()

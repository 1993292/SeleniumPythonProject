from selenium import webdriver

driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver")
driver.get("https://google.com")
searchbox = driver.find_element_by_name("q")
searchbox.send_keys(" Hello")

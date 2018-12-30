
class HomePage():

    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_id = "dropbodw-toggle"
        self.logout_link_linkText_id = "Log Out"

    def click_welcome(self):
        self.driver.find_element_by_class(self.welcome_link_id).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText_id).click()

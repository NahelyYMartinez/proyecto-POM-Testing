from selenium.webdriver.common.by import By

base_url = "https://www.saucedemo.com/"


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.xpath_image_login = '//*[@id="root"]/div/div[2]/div[1]/div[2]'
        self.input_user = 'user-name'
        self.input_password = 'password'
        self.button = 'login-button'
        self.xpath_page_init = '//*[@id="header_container"]/div[2]/span'

    def get_page_login(self):
        return self.driver.find_element(By.XPATH, self.xpath_image_login)

    def get_input_user(self):
        return self.driver.find_element(By.ID, self.input_user)

    def get_input_password(self):
        return self.driver.find_element(By.ID, self.input_password)

    def get_button(self):
        return self.driver.find_element(By.ID, self.button)


    def send_text_user(self, user):
        self.get_input_user().send_keys(user)

    def send_password(self, password):
        self.get_input_password().send_keys(password)

    def send_button(self):
        self.get_button().click()

    def view_page(self):
        return self.get_page_login().is_displayed()


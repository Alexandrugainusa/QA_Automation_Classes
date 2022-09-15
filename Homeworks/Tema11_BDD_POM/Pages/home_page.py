from selenium.webdriver.common.by import By

from Homeworks.Tema11_BDD_POM.Pages.base_page import BasePage


class Homepage(BasePage):
    FORGOT_PASSWORD_LINK = (By.XPATH, '//*[@id="content"]/ul/li[20]/a')
    FORM_AUTH_LINK = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    INPUTS_LINK = (By.XPATH, '//*[@id="content"]/ul/li[27]/a')
    KEY_PRESSES_LINK = (By.XPATH, '//*[@id="content"]/ul/li[31]/a')

    def navigate_to_web_page(self):
        self.driver.get('https://the-internet.herokuapp.com/')

    def click_forgot_password(self):
        self.driver.find_element(*self.FORGOT_PASSWORD_LINK).click()

    def click_form_auth(self):
        self.driver.find_element(*self.FORM_AUTH_LINK).click()

    def click_inputs(self):
        self.driver.find_element(*self.INPUTS_LINK).click()

    def click_key_presses(self):
        self.driver.find_element(*self.KEY_PRESSES_LINK).click()
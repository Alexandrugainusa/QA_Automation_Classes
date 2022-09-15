from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

from Homeworks.Tema11_BDD_POM.Pages.base_page import BasePage


class LoginPage(BasePage):
    USER_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button/i')
    ERROR_LOGIN = (By.XPATH, '//*[@id="flash"]')
    X_BTN = (By.XPATH, '//*[@id="flash"]/a')

    def navigate_to_login_page(self):
        self.driver.get('https://the-internet.herokuapp.com/login')

    def fill_username(self, username):
        self.driver.find_element(*self.USER_INPUT).send_keys(username)

    def fill_password(self, password):
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.LOGIN_BTN).click()

    def see_error_message(self):
        actual = self.driver.find_element(*self.ERROR_LOGIN).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'The error message is not seen!')

    def click_error_message(self):
        self.driver.find_element(*self.X_BTN).click()

    def not_see_error_message(self):
        try:
            self.driver.find_element(*self.ERROR_LOGIN)
            raise Exception("The error message is still displayed!")
        except  NoSuchElementException:
            pass



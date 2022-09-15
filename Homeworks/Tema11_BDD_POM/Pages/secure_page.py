from selenium.webdriver.common.by import By

from Homeworks.Tema11_BDD_POM.Pages.base_page import BasePage


class SecurePage(BasePage):
    LOGOUT_BTN = (By.XPATH, '//*[@id="content"]/div/a/i')
    MESSAGE_SUCCES_BANNER = (By.XPATH, '//*[@id="flash"]')

    def navigate_to_secure_page(self):
        self.driver.get('https://the-internet.herokuapp.com/secure')

    def see_message_succes_banner(self):
        actual = self.driver.find_element(*self.MESSAGE_SUCCES_BANNER).text
        print(actual)
        expected ='You logged into a secure area!'
        self.assertTrue(expected in actual, 'The secure message is not displayed!')

    def click_logout(self):
        self.driver.find_element(*self.LOGOUT_BTN).click()

    def navigate_to_login_page(self):
        actual = self.driver.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(actual, expected, 'You are not on the login page!')
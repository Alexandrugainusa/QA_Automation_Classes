from selenium.webdriver.common.by import By

from Courses.Meet11_POM.Pages.base import BasePage


class Homepage(BasePage):
    AUTOCOMPLETE = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(5) > a')
    BUTTONS = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(6) > a')
    CHECKBOX = (By.CSS_SELECTOR, 'body > div > div > li:nth-child(7) > a')

    # ToDo- de extras restul locatorilor

    def go_to_autocomplete(self):
        self.driver.find_element(*Homepage.AUTOCOMPLETE).click()

    def click_on_buttons(self):
        self.driver.find_element(*Homepage.BUTTONS).click()

    def click_on_checkbox(self):
        self.driver.find_element(*Homepage.CHECKBOX).click()

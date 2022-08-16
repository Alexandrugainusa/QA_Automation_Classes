from selenium.webdriver.common.by import By

from Courses.Meet11_POM.Pages.base import BasePage


class Autocomplete(BasePage):
    ADRESS = (By.ID, 'autocomplete')
    STREET = (By.CSS_SELECTOR, '#street_number')

    # ToDo- de extras restul locatorilor

    def enter_adress(self,email):
        self.driver.find_element(*Autocomplete.ADRESS).send_keys(email)

    def enter_street(self):
        self.driver.find_element(*Autocomplete.STREET).click()


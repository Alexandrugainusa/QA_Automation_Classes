"""
● Test 12 - brute force password hacking
- Completează user tomsmith
- Găsește elementul //h4
- Ia textul de pe el și fă split după spațiu. Consideră fiecare cuvânt ca o
potențială parolă.
- Folosește o structură iterativă prin care să introduci rând pe rând
parolele și să apeși pe login.
- La final testul trebuie să îmi printeze fie
‘Nu am reușit să găsesc parola’
‘Parola secretă este [parola]’
"""
import unittest

from selenium import webdriver

from selenium.webdriver.common.by import By


class Login(unittest.TestCase):
    LOGIN_LABEL = (By.XPATH, '//h2')
    USERNAME_INPUT = (By.XPATH, '//input[@id="username"]')
    PASS_INPUT = (By.XPATH, '//input[@id="password"]')

    # se ruleaza inainte de fiecare test
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="D:\IT FACTORY\QA_Automation_Classes\Resources\chromedriver.exe")
        # self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('https://the-internet.herokuapp.com/')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH, '//a[text() = "Form Authentication"]').click()

    # se ruleaza dupa fiecare test
    def tearDown(self):
        self.driver.quit()

    def test12_brute_force_password_hacking(self):
        self.driver.find_element(*self.USERNAME_INPUT).send_keys('tomsmith')
        subheader = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/h4').text  # //h4[@class="subheader"]
        print(subheader)
        word_list = subheader.split(' ')
        print(word_list)
        for i in range(len(word_list)):
            password = word_list[i]
            self.driver.find_element(*self.PASS_INPUT).send_keys(password)
            # actual = self.driver.find_element(*self.PASS_INPUT).send_keys('SuperSecretPassword!')
            actual = self.driver.current_url
            expected = 'https://the-internet.herokuapp.com/secure'
            if actual == expected:
                print(f'Parola secreta este {password}')
            else:
                print('Nu am reusit sa gasesc parola')

import allure

from pageobject.seleniumbase import SeleniumBase

class AuthorPage (SeleniumBase):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.submit_button: str = '[type="submit"]'
        self.authorizat_button: str = '.login'
        self.username_field: str = 'username'
        self.pass_field: str = 'password'
        self.login_selec: str = 'autologin'
        self.lost_pass: str = '[href="/account/lost_password"]'
        self.lost_email: str = 'mail'
        self.message: str = 'flash_error'
        
    @allure.step('Fill all fields')    
    def fill_authoriz_page(self, username, password):
        with allure.step('Click on authorization button'):
            self.click_is_visible('css', self.authorizat_button, 'Authorization button')
        with allure.step('Filings fields'):
            self.send_keys_is_visible('id', self.username_field, username, 'Username field')
            self.send_keys_is_visible('id', self.pass_field, password, 'Password field')
        with allure.step('Click on login button'):
            self.click_is_visible('id', self.login_selec, 'Login button')
        with allure.step('Click on submit button'):
            self.click_is_visible('css', self.submit_button, 'Submit button')
        
    @allure.step('Check message')    
    def check_message(self):
        message_text = self.text_is_visible('id', self.message, 'Message text')
        return message_text
    
    @allure.step('Input email for recovery password')    
    def pass_recovery(self, email):
        with allure.step('Click on authorization button'):
            self.click_is_visible('css', self.authorizat_button, 'Authorization button')
        with allure.step('Click on lost password button'):
            self.click_is_visible('css', self.lost_pass, 'Lost password')
        with allure.step('Input email'):
            self.send_keys_is_visible('id', self.lost_email, email,'Lost email field')
        with allure.step('Click on submit button'):
            self.click_is_visible('css', self.submit_button, 'Submit button')
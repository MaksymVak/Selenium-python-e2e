import allure

from pageobject.seleniumbase import SeleniumBase

class RegisterPage (SeleniumBase):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.register_button: str = '.register'
        self.submit_button: str = 'commit'
        self.login_field: str = 'user_login'
        self.pass_field: str = 'user_password'
        self.pass_confirm_field: str  = 'user_password_confirmation'
        self.fname_field: str = 'user_firstname'
        self.lname_field: str = 'user_lastname'
        self.mail_field: str = 'user_mail'
        self.custom_field: str = 'user_custom_field_values_3'
        self.droodown: str = 'user_language'
        self.message: str = 'flash_notice'
        
    @allure.step('Fill all fields')    
    def fill_register_page(self, login, password, pass_confirm, fName, lName, mail, customF, value):
        with allure.step('Click on registration button'):
            self.click_is_visible('css', self.register_button, 'Register button')
        with allure.step('Filings fields'):
            self.send_keys_is_visible('id', self.login_field, login, 'Login field')
            self.send_keys_is_visible('id', self.pass_field, password, 'Password field')
            self.send_keys_is_visible('id', self.pass_confirm_field, pass_confirm, 'Password confirm field')
            self.send_keys_is_visible('id', self.fname_field, fName, 'First name field')
            self.send_keys_is_visible('id', self.lname_field, lName, 'Last name field')
            self.send_keys_is_visible('id', self.mail_field, mail, 'Email field')
            self.send_keys_is_visible('id', self.custom_field, customF, 'Custom field')
            self.select_by_text('id', self.droodown, value, 'Select launger')
        with allure.step('Click on submit button'):
            self.click_is_visible('name', self.submit_button, 'Submit button')
    
    @allure.step('Check message')    
    def check_message(self):
        message_text = self.text_is_visible('id', self.message, 'Message text')
        return message_text
        
import pytest
import allure

from helpers.generate_data import generated_data
from pageobject.author_page import AuthorPage
from pageobject.register_page import RegisterPage
from pageobject.search_page import SearchPage


@pytest.mark.usefixtures('setup')

@allure.suite('Example tests')
class TestExample:
    
    @allure.title('TC-01 - Registration on the website Redmine.com')
    def test_register_page (self):
        register_test = RegisterPage(self.driver)
        data = next(generated_data())
        country = 'Ukrainian (Українська)'
        register_test.fill_register_page(data.user_name, "password-invalide", "password-invalide", data.first_name, data.last_name, data.email, data.user_name, country)
        assert 'Обліковий запис успішно створений.' in register_test.check_message(), 'Message text does not match'
    
    @allure.title('TC-02 - Authorization on the website Redmine.com')  
    def test_author_page (self):
        author_test = AuthorPage(self.driver)
        data = next(generated_data())
        author_test.fill_authoriz_page(data.user_name, data.password)
        assert 'Неправильне' in author_test.check_message(), 'Message text does not match'
    
    @allure.title('TC-03 - Password recovery')    
    def test_pass_recovery (self):
        recovery_test = AuthorPage(self.driver)
        data = next(generated_data())
        recovery_test.pass_recovery(data.email)
        assert 'Невідомий' in recovery_test.check_message(), 'Message text does not match'
    
    @allure.title('TC-04 - Testing the search')    
    def test_search (self):
        search_test = SearchPage(self.driver)
        search_test.fill_search_field('Redmine')
        assert 'Redmine' in search_test.check_message(), 'Message text does not match'
    
    @allure.title('TC-05 - Checking the forum')    
    def test_forum (self):
        forum_test = SearchPage(self.driver)
        forum_test.check_forum()
        assert 'How to contribute - Redmine' in forum_test.check_title(), 'Page title does not match'
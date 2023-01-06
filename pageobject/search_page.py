import allure

from pageobject.seleniumbase import SeleniumBase

class SearchPage (SeleniumBase):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.submit_button: str = '[type="submit"]'
        self.search_field: str = 'q'
        self.news_checkbox: str = 'news'
        self.forum_button: str = '[href="/projects/redmine/boards"]'
        self.discussion_boards: str = '[href="/projects/redmine/boards/1"]'
        self.contribute_topics: str = '[href="/boards/1/topics/4325"]'
        self.search_result: str = '.news > a'
        
    @allure.step('Input text for search')     
    def fill_search_field(self, value):
        with allure.step('Filings fields'):
            self.send_keys_is_visible_enter('id', self.search_field, value, 'Input field')
        with allure.step('Click on news checkbox'):
            self.click_is_visible('id', self.news_checkbox, 'News check')
        with allure.step('Click on submit button'):
            self.click_is_visible('css', self.submit_button, 'Submit button')
    
    @allure.step('Check message')    
    def check_message(self):
        message_text = self.text_is_visible('css', self.search_result, 'Search result')
        return message_text
    
    @allure.step('Forum select') 
    def check_forum(self):
        with allure.step('Click on forum button'):
            self.click_is_visible('css', self.forum_button, 'Forum button')
        with allure.step('Select Discussion'):
            self.click_is_visible('css', self.discussion_boards, 'Discussion')
        with allure.step('Select Contribute'):
            self.click_is_visible('css', self.contribute_topics, 'Contribute')
    
    @allure.step('Check title')    
    def check_title(self):
        title = self.title_page()
        return title
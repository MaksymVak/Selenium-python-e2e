import allure

from typing import List
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as exp
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


class SeleniumBase:
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15, 0.3, ignored_exceptions=StaleElementReferenceException)
        
    def title_page(self):
        get_title = self.driver.title
        return get_title
                      
    def __get_selenium_by(self, find_by) -> dict:
        find_by = find_by.lower()
        locating = {'css': By.CSS_SELECTOR,
                    'xpath': By.XPATH,
                    'class_name': By.CLASS_NAME,
                    'id': By.ID,
                    'link_text': By.LINK_TEXT,
                    'name': By.NAME,
                    'partial_link_text': By.PARTIAL_LINK_TEXT,
                    'tag_name': By.TAG_NAME
        }
        return locating[find_by]
    
    def is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(exp.visibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)
    
    def is_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(exp.presence_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)
    
    def is_not_present(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.__wait.until(exp.invisibility_of_element_located((self.__get_selenium_by(find_by), locator)), locator_name)
    
    def are_visible(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(exp.visibility_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)
    
    def are_present(self, find_by: str, locator: str, locator_name: str = None) -> List[WebElement]:
        return self.__wait.until(exp.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)), locator_name)
    
    def get_text_from_webelements(self, elements: List[WebElement]) -> List[str]:
        return [element.text for element in elements]
    
    def get_element_by_text(self, elements: List[WebElement], name: str) -> WebElement:
        name = name.lower()
        return [element for element in elements if element.text.lower() == name][0]
    
    def send_keys_is_visible(self, find_by: str, locator: str, element: str, locator_name: str = None) -> WebElement:
        self.is_visible(find_by, locator, locator_name).send_keys(element)
        
    def send_keys_is_visible_enter(self, find_by: str, locator: str, element: str, locator_name: str = None) -> WebElement:
        self.is_visible(find_by, locator, locator_name).send_keys(element + Keys.ENTER)
        
    def click_is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        self.is_visible(find_by, locator, locator_name).click()
        
    def text_is_visible(self, find_by: str, locator: str, locator_name: str = None) -> WebElement:
        return self.is_visible(find_by, locator, locator_name).text
    
    def select_by_text(self, find_by, locator, value, locator_name) -> WebElement:
        sellect = Select(self.is_present(find_by, locator, locator_name))
        sellect.select_by_visible_text(value)

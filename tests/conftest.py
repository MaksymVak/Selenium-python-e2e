import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from helpers.webdriver_listener import WebDriverListener
from selenium.webdriver.support.event_firing_webdriver import EventFiringWebDriver


@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')
    options.add_argument("--lang=uk")
    options.add_argument('--start-maximized')
    return options

@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = EventFiringWebDriver(webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options),
    WebDriverListener())
    return driver

@pytest.fixture(scope='function')
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://www.redmine.org/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)
    yield driver
    driver.quit()
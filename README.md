# Selenium Webdriver e2e-tests with Python and Allure report

E2e test for Selenium Webdriver with usage Allure Plugin.

## Setup

To enjoy the automated tests, develop the framework or adapt it to your own purposes, just download the project or clone repository. You need to install packages using pip according to requirements.txt file.
Run the command below in terminal:

$ pip install -r requirements.txt

### How to run the tests on windows

To generate all tests report using Allure you need to run tests by command first:

$ pytest -s -v tests --alluredir=allure-result

After that you need to use command:

$ allure serve .\allure-result\

Report is generated in Chrome browser.


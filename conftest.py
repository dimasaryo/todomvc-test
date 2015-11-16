import pytest
from selenium import webdriver


BROWSERS = {
    'firefox': webdriver.DesiredCapabilities.FIREFOX
    #'chrome': webdriver.DesiredCapabilities.CHROME
}

HEADLESS_BROWSER = {
  'headless' : webdriver.DesiredCapabilities.PHANTOMJS        
}

WEBDRIVER_ENDPOINT = 'http://localhost:4444/wd/hub'

def pytest_addoption(parser):
    parser.addoption("--headless", action="store_true", help="run headless testing")

def pytest_generate_tests(metafunc):
    if 'browsers' in metafunc.fixturenames:
        if metafunc.config.option.headless:
            metafunc.parametrize("browsers", HEADLESS_BROWSER.values())
        else:
            metafunc.parametrize("browsers", BROWSERS.values())

@pytest.yield_fixture
def browser( browsers ):
    driver = webdriver.Remote(
        command_executor=WEBDRIVER_ENDPOINT,
        desired_capabilities=browsers
    )
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

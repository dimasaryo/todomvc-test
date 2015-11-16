import pytest
from selenium import webdriver

# Supported browsers
BROWSERS = {
    'firefox': webdriver.DesiredCapabilities.FIREFOX,
    'chrome': webdriver.DesiredCapabilities.CHROME,
    'headless': webdriver.DesiredCapabilities.PHANTOMJS
}

# Selenium server url
WEBDRIVER_ENDPOINT = 'http://localhost:4444/wd/hub'

# Add command line option to get the browser option
def pytest_addoption(parser):
    parser.addoption("--browseropt", action="store", default="all", help="choose the browsers [firefox, chrome, headless]. By default it will run the tests on all browsers except the headless.")

# Parse the browser option from the command line
def pytest_generate_tests(metafunc):
    if 'browsers' in metafunc.fixturenames:
        if metafunc.config.option.browseropt == 'firefox':
            # Only test using firefox browser
            metafunc.parametrize("browsers", [BROWSERS['firefox']])
        elif metafunc.config.option.browseropt == 'chrome':
            # Only test using chrome browser
            metafunc.parametrize("browsers", [BROWSERS['chrome']])
        elif metafunc.config.option.browseropt == 'headless':
            # Only test using phantomJS browser
            metafunc.parametrize("browsers", [BROWSERS['headless']])
        else:
            #If browser not specified in the command arguments,
            #use all browser excepts the headless.
            #Remove the headless browser
            del BROWSERS['headless']
            metafunc.parametrize("browsers", BROWSERS.values())

# Instantiate and configure the browser
@pytest.yield_fixture
def browser( browsers ):
    # Using selenium web driver remote
    driver = webdriver.Remote(
        command_executor=WEBDRIVER_ENDPOINT,
        desired_capabilities=browsers
    )
    # Driver configuration
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

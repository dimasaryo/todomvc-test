import pytest
from selenium import webdriver
from apps.todo_react import TodoReact
from apps.todo_angular import TodoAngular
from faker import Faker
from selenium.webdriver.common.keys import Keys

# Supported browsers
BROWSERS = {
  'firefox': webdriver.DesiredCapabilities.FIREFOX,
  'chrome': webdriver.DesiredCapabilities.CHROME,
  'headless': webdriver.DesiredCapabilities.PHANTOMJS
}

# Selenium server url
WEBDRIVER_ENDPOINT = 'http://localhost:4444/wd/hub'

# Add command line option
def pytest_addoption(parser):
  parser.addoption("--browseropt", action="store", default="all", help="choose the browsers [firefox, chrome, headless]. If not specified, it will run the tests on all browsers except the headless.")
  parser.addoption("--appopt", action="store", default="all", help="choose the todoMVC type [angular, react]. If not specified, it will test all types.")

# Parse the option from the command line
def pytest_generate_tests(metafunc):
  # Parse the browser option from the command line
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
  # Parse the todos apps from the command line   
  if 'apps' in metafunc.fixturenames:
    if metafunc.config.option.appopt == 'angular':
      metafunc.parametrize("apps", [TodoAngular()])
    elif metafunc.config.option.appopt == 'react':
      metafunc.parametrize("apps", [TodoReact()])
    else:
      metafunc.parametrize("apps",[TodoAngular(), TodoReact()])

# Test data
fake = Faker()
@pytest.fixture()
def generate_test_data(todoApp):
  
  # Create 3 active todos
  for num in range (1,4):
    new_todo_input = todoApp.find_new_todo_input()
    new_todo_input.send_keys(fake.name(), Keys.ENTER)
    
  # Create 3 completed todos
  for num in range (1,4):
    text = fake.name()
    new_todo_input = todoApp.find_new_todo_input()
    new_todo_input.send_keys(text, Keys.ENTER)
    todoApp.toggle_todo(text)
    
# Instantiate and configure the browser
@pytest.yield_fixture
def todoApp( request,browsers, apps ):
  # Using selenium web driver remote
  driver = webdriver.Remote(
    command_executor=WEBDRIVER_ENDPOINT,
    desired_capabilities=browsers
  )
  # Driver configuration
  driver.implicitly_wait(10)
  driver.maximize_window()
  apps.set_driver(driver)
  yield apps
  
  apps.quit()

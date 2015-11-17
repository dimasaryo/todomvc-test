import pytest
from selenium.webdriver.common.keys import Keys
from faker import Faker

fake = Faker()

# Generate various string
@pytest.mark.parametrize("input",[
  fake.name(),
  fake.text(),
  '\'hello kitty\"'
])

def test_creating_todo(todoApp, input):
  """
  Test on creating todo using various string
  
  Pre-condition:
  1. The todo applications is empty.
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  2. Click on the new todo field.
  3. Type the desired string.
  4. Press ENTER key.
  
  Expected result:
  1. The new todo exists in the todo list.
  2. The new todo is active.
  3. The active todo count is +1
  """
  # Create new todo
  new_todo_input = todoApp.find_new_todo_input()
  print new_todo_input
  new_todo_input.send_keys(input, Keys.ENTER)

  # ASSERTION
  # Check whether the new todo exist in the todo list or not.
  todo = todoApp.find_todo(input)
    
  # Check the new todo status, it should active.
  assert todoApp.is_active_todo(todo)
   
  # Check the active todo count
  assert todoApp.count_active_todos() == '1 item left'


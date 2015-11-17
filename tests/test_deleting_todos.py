import pytest
from selenium.common.exceptions import NoSuchElementException
  
@pytest.mark.usefixtures('generate_test_data')
def test_deleting_active_todo(todoApp):
  """
  Test on deleting active todo
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  2. Hover the mouse on the active todo, the 'x' button appears.
  3. Click on the 'x' button.
  
  Expected result:
  1. The active todo count is 2 items left
  2. The deleted todo doesn't exist in the todo list
  """
  # Get the active todos
  active_todos = todoApp.find_active_todos()
  
  # Update  an active todo from the list
  text = active_todos[0].text
  todoApp.delete_todo(text)

  # Check the active todo count
  assert todoApp.count_active_todos() == '2 items left'
  
  # ASSERTION
  try:
    todo = todoApp.find_todo(text)
  except NoSuchElementException:
    return # Expected result
   
  assert False # Something wrong
  
@pytest.mark.usefixtures('generate_test_data')
def test_deleting_completed_todo(todoApp):
  """
  Test on deleting completed todo
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  2. Hover the mouse on the completed todo, the 'x' button appears.
  3. Click on the 'x' button.
  
  Expected result:
  1. The active todo count still 3 items left
  2. The deleted todo doesn't exist in the todo list'
  """
  # Get the completed todos
  completed_todos = todoApp.find_completed_todos()
  
  # Delete an completed todo from the list
  text = completed_todos[0].text
  todoApp.delete_todo(text)

  # Check the active todo count is not changed
  assert todoApp.count_active_todos() == '3 items left'
  
  # ASSERTION
  try:
    todo = todoApp.find_todo(text)
  except NoSuchElementException:
    return # Expected result
   
  assert False # Something wrong
  
@pytest.mark.usefixtures('generate_test_data')
def test_clear_all_completed_todos(todoApp):
  """
  Test on deleting all completed todos
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the 'clear completed' button.
  
  Expected result:
  1. The active todo count still 3 items left
  2. The deleted todos doesn't exist in the todo list'
  """
  # Get the completed todos
  completed_todos = todoApp.clear_completed()

  # Check the active todo count is not changed
  assert todoApp.count_active_todos() == '3 items left'
  
  # ASSERTION
  todo = todoApp.find_completed_todos()
  assert len(todo) == 0

import pytest
from faker import Faker

fake = Faker()

@pytest.mark.usefixtures('generate_test_data')
def test_updating_active_todos_text(todoApp):
  """
  Test on updating active todo's text
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Double click on the active todo item, the text becomes editable.
  4. Type the new value.
  5. Press ENTER key.
  
  Expected result:
  1. The todo value exists on the todo list.
  """
  # New todo's text
  new_text = fake.name()
  
  # Get the active todos
  active_todos = todoApp.find_active_todos()
  
  # Update  an active todo from the list
  todoApp.update_todo( active_todos[0].text, new_text)

  # ASSERTION
  # Check whether the new todo exist in the todo list or not.
  todoApp.find_todo(new_text)
  
  
@pytest.mark.usefixtures('generate_test_data')
def test_updating_completed_todos_text(todoApp):
  """
  Test on updating completed todo's text
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Double click on the completed todo item, the text becomes editable.
  4. Type the new value.
  5. Press ENTER key.
  
  Expected result:
  1. The todo value exists on the todo list.
  """
  # New todo's text
  new_text = fake.name()
  
  # Get the completed todos
  completed_todos = todoApp.find_completed_todos()
  
  # Update  an completed todo from the list
  todoApp.update_todo( completed_todos[0].text, new_text)

  # ASSERTION
  # Check whether the new todo exist in the todo list or not.
  todoApp.find_todo(new_text)

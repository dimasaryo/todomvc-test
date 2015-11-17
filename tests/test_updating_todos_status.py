import pytest
  
@pytest.mark.usefixtures('generate_test_data')
def test_mark_active_todo_as_complete(todoApp):
  """
  Test on marking active todo as complete
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the Checkbox before the active todo's label.
  
  Expected result:
  1. The todo is not active
  2. The active todo count is only 2 items left
  """
  # Get the active todos
  active_todos = todoApp.find_active_todos()
  
  # Update  an active todo from the list
  text = active_todos[0].text
  todoApp.toggle_todo(text)

  # ASSERTION
  todo = todoApp.find_todo(text)
  
  # Check the new todo status, it should completed.
  assert todoApp.is_active_todo(todo) == False
   
  # Check the active todo count
  assert todoApp.count_active_todos() == '2 items left'


@pytest.mark.usefixtures('generate_test_data')
def test_mark_completed_todo_as_active(todoApp):
  """
  Test on marking completed todo as active
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the Checkbox before the completed todo's label.
  
  Expected result:
  1. The todo is now active
  2. The active todo count is increased to 4 items left
  """
  # Get the completed todos
  completed_todos = todoApp.find_completed_todos()
  
  # Update  an completed todo from the list
  text = completed_todos[0].text
  todoApp.toggle_todo(text)

  # ASSERTION
  todo = todoApp.find_todo(text)
  
  # Check the new todo status, it should active.
  assert todoApp.is_active_todo(todo)
   
  # Check the active todo count
  assert todoApp.count_active_todos() == '4 items left'

@pytest.mark.usefixtures('generate_test_data')
def test_toggle_all_todos_one_time(todoApp):
  """
  Test on marking all todos as completed
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the arrow down button before the new todo field.
  
  Expected result:
  1. All todos become completed.
  2. No active todos left
  """
  # Get the completed todos
  todoApp.click_toggle_all()

  # ASSERTION  
  # Check the active todo count
  assert todoApp.count_active_todos() == '0 items left'  
  
  # Get all completed todos
  completed_todos = todoApp.find_completed_todos()
  assert len(completed_todos) == 6
  
@pytest.mark.usefixtures('generate_test_data')
def test_toggle_all_todos_twice(todoApp):
  """
  Test on marking all todos as active
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the arrow down button before the new todo field.
  
  Expected result:
  1. All todos become active.
  2. All todos are active
  """
  # Click toggle all button twice
  todoApp.click_toggle_all()
  todoApp.click_toggle_all()
  
  # ASSERTION  
  # Check the active todo count
  assert todoApp.count_active_todos() == '6 items left'  
  
  # Get all completed todos
  completed_todos = todoApp.find_completed_todos()
  assert len(completed_todos) == 0
  
  # Get all active todos
  active_todos = todoApp.find_active_todos()
  assert len(active_todos) == 6

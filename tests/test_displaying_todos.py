import pytest

@pytest.mark.usefixtures('generate_test_data')
def test_displaying_all_todos(todoApp):
  """
  Test on displaying all todos
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the 'All' button.
  
  Expected result:
  1. The active todos count is 3 items
  2. The completed todos count is 3 items
  """
  # Click filters all button
  todoApp.filter_all()
  
  # Get the active todos
  active_todos = todoApp.find_active_todos()
  
  # Get the completed todos
  completed_todos = todoApp.find_completed_todos()
  
  # ASSERTION
  # All todos are displayed
  assert len(active_todos) == 3
  assert len(completed_todos) == 3
  
@pytest.mark.usefixtures('generate_test_data')
def test_displaying_only_active_todos(todoApp):
  """
  Test on displaying only active todos
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the 'Active' button.
  
  Expected result:
  1. The active todos count is 3 items
  2. The completed todos count is 0 items
  """
  # Click filters active button
  todoApp.filter_active()
  
  # Get the active todos
  active_todos = todoApp.find_active_todos()
  
  # Get the completed todos
  completed_todos = todoApp.find_completed_todos()
  
  # ASSERTION
  # All todos are displayed
  assert len(active_todos) == 3
  assert len(completed_todos) == 0
  
@pytest.mark.usefixtures('generate_test_data')
def test_displaying_only_completed_todos(todoApp):
  """
  Test on displaying only completed todos
  
  Pre-condition:
  1. The todos applications consists 3 active todos and 3 completed todos
  
  Steps:
  1. Open browser and go to DESTINATION_URL.
  3. Click on the 'Completed' button.
  
  Expected result:
  1. The active todos count is 0 items
  2. The completed todos count is 3 items
  """
  # Click filters completed button
  todoApp.filter_completed()
  
  # Get the active todos
  active_todos = todoApp.find_active_todos()
  
  # Get the completed todos
  completed_todos = todoApp.find_completed_todos()
  
  # ASSERTION
  # All todos are displayed
  assert len(active_todos) == 0
  assert len(completed_todos) == 3

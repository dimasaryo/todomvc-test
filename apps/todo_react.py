from todo_app import TodoApp
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class TodoReact(TodoApp):
  
  def __init__(self):
    """
    Default constructor
    """
    self.url = 'http://todomvc.com/examples/react/#/'
    
  def set_driver(self, driver):
    """
    Set browser
    """
    self.driver = driver
    self.driver.get(self.url)
    
  def quit(self):
    """
    Close the browser
    """
    self.driver.quit()
    
  def find_new_todo_input(self):
    """
    Find new todo field
    """
    return self.driver.find_element_by_class_name('new-todo')
    
  def click_toggle_all(self):
    """
    The first click will mark all todos as completed.
    The second click will mark all todos as active.
    """
    self.driver.find_element_by_class_name('toggle-all').click()
    
  def count_active_todos(self):
    """
    Get the count of active todos
    """
    return self.driver.find_element_by_class_name('todo-count').text
    
  def filter_all(self):
    """
    Displaying all todos
    """
    self.find_filters().find_element_by_xpath("//li/a[contains(text(), 'All')]").click()
  
  def filter_active(self):
    """
    Displaying only active todos
    """
    self.find_filters().find_element_by_xpath("//li/a[contains(text(), 'Active')]").click()
  
  def filter_completed(self):
    """
    Displaying only completed todos
    """
    self.find_filters().find_element_by_xpath("//li/a[contains(text(), 'Completed')]").click()
  
  def clear_completed(self):
    """
    Delete all completed todos
    """
    self.driver.find_element_by_class_name('clear-completed').click()
    
  def find_todo_list(self):
    """
    Get the todo list
    """
    return self.driver.find_element_by_class_name('todo-list')
  
  def toggle_todo(self,text):
    """
    Mark a todo that has value 'text' as complete or active
    """
    todo = self.find_todo(text)
    todo.find_element_by_class_name('toggle').click()
  
  def toggle_todos(self,text):
    """
    Mark all todos that has value 'text' as complete or active
    """
    todos = self.find_todos(text)
    for todo in todos:
      todo.find_element_by_class_name('toggle').click()
  
  def delete_todo(self,text):
    """
    Delete a todo by the value
    """
    todo = self.find_todo(text)
    todo_view = todo.find_element_by_class_name('view')
    destroy_button = todo.find_element_by_class_name('destroy')
    hover = ActionChains(self.driver).move_to_element(todo_view)
    hover.perform()
    if destroy_button.is_displayed():
      destroy_button.click()
  
  def delete_todos(self,text):
    """
    Delete all todos by the value
    """
    todos = self.find_todos(text)
    for todo in todos:
      todo_view = todo.find_element_by_class_name('view')
      destroy_button = todo.find_element_by_class_name('destroy')
      hover = ActionChains(self.driver).move_to_element(todo_view)
      hover.perform()
      if destroy_button.is_displayed():
        destroy_button.click()
  
  def find_active_todos(self):
    """
    Get the active todo list
    """
    todoList = self.find_todo_list()
    return todoList.find_elements_by_xpath("//li[@class='']")
  
  def find_completed_todos(self):
    """
    Get the completed todo list
    """
    todoList = self.find_todo_list()
    return todoList.find_elements_by_xpath("//li[@class='completed']")
    
  def update_todo(self,current_text, new_text):
    """
    Update a todo from 'current_text' to 'new_text'
    """
    todo = self.find_todo(current_text)
    todo_view = todo.find_element_by_class_name('view')
    todo_edit = todo.find_element_by_class_name('edit')
    ActionChains(self.driver).double_click(todo_view).perform()
    if todo_edit.is_displayed():
      todo_edit.clear()
      todo_edit.send_keys(new_text, Keys.ENTER)
  
  def update_todos(self,text):
    """
    Update all todos that have value 'current_text' to 'new_text'
    """
    todos = self.find_todos(text)
    for todo in todos:
      todo_view = todo.find_element_by_class_name('view')
      todo_edit = todo.find_element_by_class_name('edit')
      ActionChains(self.driver).double_click(todo_view).perform()
      if todo_edit.is_displayed():
        todo_edit.clear()
        todo_edit.send_keys(text, Keys.ENTER)
      
  def find_todo(self,text):
    """
    Get a todo by the value
    """
    todoList = self.find_todo_list()
    todo = todoList.find_element_by_xpath("//li/div[@class='view']/label[contains(text(), %s )]" %self.toXPathStringLiteral(text))
    return todo.find_element_by_xpath('../..')
  
  def find_todos(self,text):
    """
    Get all todos by the value
    """
    result = []
    todoList = self.find_todo_list()
    todos = todoList.find_elements_by_xpath("//li/div[@class='view']/label[contains(text(), %s )]" %self.toXPathStringLiteral(text))
    for todo in todos:
      result.append(todo.find_element_by_xpath('../..'))
    return result
  
  def find_filters(self):
    """
    Get filters panel
    """
    return self.driver.find_element_by_class_name('filters')
    
  def is_active_todo(self, todo):
    """
    Check wheter the specified todo is active or complete
    """
    return todo.get_attribute("class") == ''
    
  def toXPathStringLiteral(self,s):
    """
    Sanitize the string s to be used in the XPath
    """
    if "'" not in s: return "'%s'" % s
    if '"' not in s: return '"%s"' % s
    return "concat('%s')" % s.replace("'", "',\"'\",'")
  

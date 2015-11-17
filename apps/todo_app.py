from abc import ABCMeta, abstractmethod

# TodoMVC-angularjs shared same functionality with the TodoMVC-reactjs.
class TodoApp:
  __metaclass__ = ABCMeta

  @abstractmethod
  def set_driver(driver):pass

  @abstractmethod
  def quit():pass

  @abstractmethod
  def find_new_todo_input():pass
  
  @abstractmethod
  def click_toggle_all():pass
  
  @abstractmethod
  def count_active_todos():pass
  
  @abstractmethod
  def filter_all():pass
  
  @abstractmethod
  def filter_active():pass
  
  @abstractmethod
  def filter_completed():pass
  
  @abstractmethod
  def clear_completed():pass
  
  @abstractmethod
  def find_todo_list():pass
  
  @abstractmethod
  def toggle_todo(text):pass
  
  @abstractmethod
  def toggle_todos(text):pass
  
  @abstractmethod
  def delete_todo(text):pass
  
  @abstractmethod
  def delete_todos(text):pass
  
  @abstractmethod
  def update_todo(text):pass
  
  @abstractmethod
  def update_todos(text):pass
  
  @abstractmethod
  def find_todo(text):pass
  
  @abstractmethod
  def find_todos(text):pass
  
  @abstractmethod
  def find_active_todos():pass
  
  @abstractmethod
  def find_completed_todos():pass
  
  @abstractmethod
  def is_active_todo(todo):pass
  
  
  
  

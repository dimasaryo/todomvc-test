# Testing Todos creation
from selenium.webdriver.common.keys import Keys

def test_creating_todos(browser):
    browser.get('http://todomvc.com/examples/react/#/')
    newTodoField = browser.find_element_by_id("new-todo") or browser.find_element_by_class_name("new-todo")
    newTodoField.send_keys("test", Keys.ENTER)
    todoList = browser.find_element_by_id("todo-list")
    items = todoList.find_elements_by_tag_name("li")
    for item in items:
      if item.text == 'test':
          return
    
    assert False #The created todo doesn't exists in the todo list

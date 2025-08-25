"""
To-Do List Application
Description: This Python to-do list application allows you to add tasks, view the list of tasks, and remove completed tasks. It's a simple tool to keep track of your daily tasks.
Goal: Understanding of list and basic input/output
"""

# To-Do List Application
class TodoList:
    def __init__(self):
        self.tasks = []
 
    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")
 
    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' removed.")
        else:
            print(f"Task '{task}' not found.")
 
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to show.")
        else:
            print("To-Do List:")
            for task in self.tasks:
                print(f"- {task}")
 
# Create a to-do list
todo = TodoList()
 
# Clling my methods 
# Add, remove, or view tasks
todo.add_task(input("Add a Task: "))
#todo.add_task(input())
todo.view_tasks(input("View all tasks: "))
todo.remove_task(input("Remove a task: "))

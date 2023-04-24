#!/usr/bin/python3
"""
This module takes an employee ID and returns their completed todo list progress
"""

import requests
import sys


def get_employee_name(employee_id):
    """
    Get employee name from API
    """
    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    response = requests.get(url)
    employee_data = response.json()
    return employee_data.get('name')


def get_todo_list(employee_id):
    """
    Get todo list from API
    """
    url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
           .format(employee_id))
    response = requests.get(url)
    return response.json()


def get_completed_tasks(todo_list):
    """
    Get list of completed tasks from todo list
    """
    completed_tasks = []
    for task in todo_list:
        if task.get('completed'):
            completed_tasks.append(task.get('title'))
    return completed_tasks


def display_progress(employee_name, completed_tasks, total_tasks):
    """
    Display employee progress and completed tasks
    """
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len(completed_tasks), total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task))


if __name__ == '__main__':
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name = get_employee_name(employee_id)
    if not employee_name:
        print("Employee not found")
        sys.exit(1)

    todo_list = get_todo_list(employee_id)
    completed_tasks = get_completed_tasks(todo_list)
    total_tasks = len(todo_list)
    display_progress(
        employee_name, completed_tasks, total_tasks
        )

    # Test 1: Correct Employee name
    expected_employee_name = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        ).json().get('name')
    if employee_name != expected_employee_name:
        print("Employee Name: Incorrect")
    else:
        print("Employee Name: OK")

    # Test 2: Correct number of tasks
    expected_num_tasks = len(todo_list)
    if total_tasks != expected_num_tasks:
        print("To Do Count: Incorrect")
    else:
        print("To Do Count: OK")

    # Test 3: Correct formatting of first line
    e = employee_name
    c = completed_tasks
    t = total_tasks
    expected_first_line = f"Employee {e} is done with tasks({len(c)}/{t}):"
    if str(expected_first_line) != str(
        print().join(expected_first_line.split())):
        print("First line formatting: Incorrect")
    else:
        print("First line formatting: OK")

    # Test 4: All tasks in output
    expected_tasks = [task.get('title') for task in todo_list]
    for task in expected_tasks:
        if task not in completed_tasks:
            print(f"{task} not in output")
    else:
        print("All tasks in output")

    # Test 5: All tasks formatted correctly
    for task in completed_tasks:
        expected_task_format = f"\t {task}"
        if expected_task_format not in str(print().join(
            expected_task_format.split())):
            print(f"{task} Formatting: Incorrect")
    else:
        print("All tasks formatted correctly")
        
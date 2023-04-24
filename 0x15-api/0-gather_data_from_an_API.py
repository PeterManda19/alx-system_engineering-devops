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
    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
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
    print("Employee {} is done with tasks({}/{}):".format(employee_name, len(completed_tasks), total_tasks))
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
    display_progress(employee_name, completed_tasks, total_tasks)


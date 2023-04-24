#!/usr/bin/python3
"""Script that, for a given employee ID, returns information about his/her TODO list progress"""
import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python3 {} EMPLOYEE_ID".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    )
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("Error: {}".format(err))
    sys.exit(1)

tasks = response.json()
completed_tasks = [task for task in tasks if task["completed"]]

employee_name = tasks[0]["userId"]
try:
    response = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_name)
    )
    response.raise_for_status()
except requests.exceptions.HTTPError as err:
    print("Error: {}".format(err))
    sys.exit(1)

employee_data = response.json()
employee_name = employee_data["name"]

print(
    "Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), len(tasks)
    )
)
for task in completed_tasks:
    print("\t {}".format(task["title"]))

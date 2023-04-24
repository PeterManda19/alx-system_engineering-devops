#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee.
"""

import requests
import sys

def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Get employee name
    employee_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    employee_response.raise_for_status()
    employee_name = employee_response.json()["name"]

    # Get employee's tasks
    tasks_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks_response.raise_for_status()
    tasks = tasks_response.json()

    # Calculate progress
    completed_tasks = [task for task in tasks if task["completed"]]
    number_of_completed_tasks = len(completed_tasks)
    total_number_of_tasks = len(tasks)

    # Print progress
    print(f"Employee {employee_name} is done with tasks({number_of_completed_tasks}/{total_number_of_tasks}):")
    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == '__main__':
    main()

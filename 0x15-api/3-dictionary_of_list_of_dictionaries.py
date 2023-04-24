#!/usr/bin/python3
"""Export data in JSON format for all employees"""

import json
import requests


if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    if response.status_code == 200:
        employees = response.json()

        tasks_dict = {}
        for employee in employees:
            user_id = employee.get('id')
            employee_name = employee.get('name')

            url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
            response = requests.get(url)
            if response.status_code == 200:
                tasks = response.json()

                task_list = []
                for task in tasks:
                    task_dict = {"username": employee_name, "task": task.get('title'), "completed": task.get('completed')}
                    task_list.append(task_dict)

                tasks_dict[user_id] = task_list

        # Write tasks to JSON file
        filename = "todo_all_employees.json"
        with open(filename, mode='w') as file:
            json.dump(tasks_dict, file)

    else:
        print("Error: Could not retrieve employee data")

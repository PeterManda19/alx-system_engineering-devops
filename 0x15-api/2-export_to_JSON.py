#!/usr/bin/python3
"""
Export data in JSON format
"""

import json
import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        user_id = sys.argv[1]
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
        response = requests.get(url)
        if response.status_code == 200:
            employee_name = response.json().get('name')

            url = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)
            response = requests.get(url)
            if response.status_code == 200:
                tasks = response.json()
                num_of_completed_tasks = sum(1 for task in tasks if task.get('completed'))
                total_num_of_tasks = len(tasks)

                # Print employee progress report
                print("Employee {} is done with tasks({}/{}):".format(
                    employee_name, num_of_completed_tasks, total_num_of_tasks))

                # Print completed tasks
                for task in tasks:
                    if task.get('completed'):
                        print("\t {}".format(task.get('title')))

                # Write tasks to JSON file
                filename = "{}.json".format(user_id)
                with open(filename, mode='w') as file:
                    task_list = []
                    for task in tasks:
                        task_dict = {"task": task.get('title'), "completed": task.get('completed'), "username": employee_name}
                        task_list.append(task_dict)
                    json.dump({user_id: task_list}, file)

        else:
            print("User ID not found")
    else:
        print("Usage: ./1-export_to_JSON.py <employee_id>")

#!/usr/bin/python3
"""Export data in JSON format"""

import json
import requests
import sys


if __name__ == '__main__':
    url_users = 'https://jsonplaceholder.typicode.com/users'
    response_users = requests.get(url_users)
    if response_users.status_code == 200:
        users = response_users.json()
        tasks_dict = {}
        for user in users:
            user_id = user.get('id')
            employee_name = user.get('name')

            url_todos = ('https://jsonplaceholder.typicode.com/todos?userId={}'
                         .format(user_id))
            response_todos = requests.get(url_todos)
            if response_todos.status_code == 200:
                tasks = response_todos.json()
                tasks_list = []
                for task in tasks:
                    task_dict = {"task": task.get('title'),
                                 "completed": task.get('completed'),
                                 "username": employee_name}
                    tasks_list.append(task_dict)
                tasks_dict[user_id] = tasks_list

        with open('todo_all_employees.json', mode='w') as json_file:
            json.dump(tasks_dict, json_file)
    else:
        print("Error retrieving users")
        sys.exit(1)

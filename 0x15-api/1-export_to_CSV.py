#!/usr/bin/python3
"""Export data in CSV format"""

import csv
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

                # Write tasks to CSV file
                filename = "{}.csv".format(user_id)
                with open(filename, mode='w') as file:
                    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
                    for task in tasks:
                        writer.writerow([user_id, employee_name, task.get('completed'), task.get('title')])

        else:
            print("User ID not found")
    else:
        print("Usage: ./1-export_to_CSV.py <employee_id>")

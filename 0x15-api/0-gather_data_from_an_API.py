#!/usr/bin/python3
""" 
Script that uses a REST API to retrieve and display task progress information for a given employee ID.
"""

if __name__ == "__main__":
    import requests
    import sys

    user_id = sys.argv[1]
    task_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(user_id)
    user_info_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)

    tasks_response = requests.get(task_url)
    user_response = requests.get(user_info_url)

    employee_name = user_response.json().get('name')

    completed_tasks = 0
    total_tasks = len(tasks_response.json())
    completed_tasks_list = []

    for item in tasks_response.json():
        if item.get('completed'):
            completed_tasks_list.append(item.get('title'))
            completed_tasks += 1

    print("Employee {} has completed tasks ({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for task in completed_tasks_list:
        print("\t{}".format(task))

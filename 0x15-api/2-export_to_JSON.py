#!/usr/bin/python3
"""Script to export data in JSON format."""

if __name__ == "__main__":
    import json
    from requests import get
    import sys

    user_id = sys.argv[1]
    task_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    filename = f"{user_id}.json"  # To store the JSON data

    tasks_response = get(task_url).json()
    user_response = get(user_info_url).json()

    employee_name = user_response.get('username')

    user_tasks_list = []
    for task in tasks_response:
        # For each task of a user, append a dictionary
        # with the task's details into the above array
        user_tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    with open(filename, 'w') as jsonFile:
        # Write the data where the key is the user ID and
        # the value is an array of dictionaries for each task
        user_json_data = {
            user_id: user_tasks_list
        }
        jsonFile.write(json.dumps(user_json_data, indent=4))

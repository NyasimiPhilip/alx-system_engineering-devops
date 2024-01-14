#!/usr/bin/python3
"""
Script that uses a REST API to retrieve and display
task progress information for a given employee ID.
"""

# Import necessary libraries
if __name__ == "__main__":
    import requests
    import sys

    # Get the employee ID from the command line arguments
    user_id = sys.argv[1]

    # Define the URLs for task information and user information
    task_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id
    )
    user_info_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        user_id
    )

    # Make API requests to retrieve task and user information
    tasks_response = requests.get(task_url)
    user_response = requests.get(user_info_url)

    # Extract the employee name from the user information
    employee_name = user_response.json().get('name')

    # Initialize variables to track completed tasks
    completed_tasks = 0
    total_tasks = len(tasks_response.json())
    completed_tasks_list = []

    # Loop through each task and check if it is completed
    for item in tasks_response.json():
        if item.get('completed'):
            completed_tasks_list.append(item.get('title'))
            completed_tasks += 1

    # Generate and print progress message with completed tasks details
    progress_message = "Employee {} is done with tasks({}/{}):".format(
        employee_name, completed_tasks, total_tasks
    )
    print(progress_message)

    # Print the titles of completed tasks
    for task in completed_tasks_list:
        print("\t{}".format(task))

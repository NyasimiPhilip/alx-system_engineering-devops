#!/usr/bin/python3
"""Script to export data in JSON format."""

# Check if the script is being run as the main program
if __name__ == "__main__":
    import json
    from requests import get
    import sys

    # Get the user ID from the command line arguments
    user_id = sys.argv[1]

    # Define the URLs for task information and user information
    task_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Define the filename to store the JSON data
    filename = f"{user_id}.json"

    # Make API requests to retrieve task and user information
    tasks_response = get(task_url).json()
    user_response = get(user_info_url).json()

    # Extract the username from the user information
    employee_name = user_response.get('username')

    # Initialize an empty list to store task details for the user
    user_tasks_list = []

    # Loop through each task and append a dictionary with task details to the list
    for task in tasks_response:
        user_tasks_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": employee_name
        })

    # Open the JSON file for writing
    with open(filename, 'w') as jsonFile:
        # Create a dictionary where the key is the user ID
        # and the value is an array of dictionaries for each task
        user_json_data = {
            user_id: user_tasks_list
        }
        # Write the JSON data to the file with indentation for readability
        jsonFile.write(json.dumps(user_json_data, indent=4))

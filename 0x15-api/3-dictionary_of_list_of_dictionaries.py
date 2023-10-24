#!/usr/bin/python3
"""Script to export data in JSON format."""

if __name__ == "__main__":
    import json
    from requests import get

    all_employees_url = "https://jsonplaceholder.typicode.com/users"
    filename = "todo_all_employees.json"  # To store the JSON data

    all_employees = get(all_employees_url).json()

    employees_dict = {}

    for employee in all_employees:
        employee_name = employee.get('username')
        employee_id = employee.get('id')
        employee_tasks_url = (
                f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
         )
        tasks_response = get(employee_tasks_url).json()

        user_tasks_list = []
        employees_dict[employee_id] = []

        for task in tasks_response:
            employees_dict[employee_id].append({
                "username": employee_name,
                "task": task.get('title'),
                "completed": task.get('completed')
            })

    with open(filename, 'w') as jsonFile:
        json.dump(employees_dict, jsonFile, indent=4)

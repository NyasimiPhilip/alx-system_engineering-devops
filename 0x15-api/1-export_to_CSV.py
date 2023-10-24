#!/usr/bin/python3
"""Script to export data in the CSV format with double quotation marks."""

if __name__ == "__main__":
    import csv
    from requests import get
    import sys

    user_id = sys.argv[1]
    task_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    filename = f"{user_id}.csv"  # To store the CSV data

    tasks_response = get(task_url).json()
    user_response = get(user_info_url).json()

    employee_name = user_response.get('username')

    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        """
        Write the header
        csv_writer.writerow(["userId", "username", "completed", "title"])"""

        for task in tasks_response:
            csv_writer.writerow([
                user_id,
                employee_name,
                task.get("completed"),
                task.get("title")])
    print(f"Data for user {user_id} exported to {filename}")

#!/usr/bin/python3
"""Script to export data in the CSV format with double quotation marks."""

# Check if the script is being run as the main program
if __name__ == "__main__":
    import csv
    from requests import get
    import sys

    # Get the user ID from the command line arguments
    user_id = sys.argv[1]

    # Define the URLs for task information and user information
    task_url = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    user_info_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Define the filename to store the CSV data
    filename = f"{user_id}.csv"

    # Make API requests to retrieve task and user information
    tasks_response = get(task_url).json()
    user_response = get(user_info_url).json()

    # Extract the username from the user information
    employee_name = user_response.get('username')

    # Open the CSV file for writing
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write the header row to the CSV file
        csv_writer.writerow(["userId", "username", "completed", "title"])

        # Loop through each task and write its data to the CSV file
        for task in tasks_response:
            csv_writer.writerow([
                user_id,
                employee_name,
                task.get("completed"),
                task.get("title")])

    # Print a message indicating successful export
    print(f"Data for user {user_id} exported to {filename}")

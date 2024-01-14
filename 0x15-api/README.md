 <h2>API Tasks 📃</h2>
    <h3>0. Gather Data from an API</h3>
    <p>
        <code>0-gather_data_from_an_API.py: Python script that returns information on the to-do list progress of a given employee ID.
Usage: python3 0-gather_data_from_an_API.py &lt;employee ID&gt;.
Output: Employee &lt;employee name&gt; is done with tasks(&lt;# completed tasks&gt;/&lt;total # tasks&gt;):</code>
    </p>
    <h3>1. Export to CSV</h3>
    <p>
        <code>1-export_to_CSV.py: Python script exports to-do list information of a given employee ID to CSV format.
Usage: python3 1-export_to_CSV.py &lt;employee ID&gt;
File name: &lt;user id&gt;.csv.
Format: "&lt;user id&gt;","&lt;username&gt;","&lt;task completed status&gt;","&lt;task title&gt;".</code>
    </p>
    <h3>2. Export to JSON</h3>
    <p>
      <code>2-export_to_JSON.py: Python script that exports to-do list information of a given employee ID to JSON format.
Usage: python3 2-export_to_JSON.py &lt;employee ID&gt;
File name: &lt;user id&gt;.json
Format: { "&lt;user id&gt;": [ {"task": "&lt;task title&gt;", "completed": &lt;task completed status&gt;, "username": "&lt;username&gt;"}}, ... ]}</code>
    </p>
    <h3>3. Dictionary of List of Dictionaries</h3>
    <p>
        <code>3-dictionary_of_list_of_dictionaries.py: Python script that exports to-do list information for all employees to JSON format.
Usage: python3 3-dictionary_of_list_of_dictionaries.py
File name: todo_all_employees.json
Format: { "&lt;user id&gt;": [ {"username": "&lt;username&gt;", "task": "&lt;task title&gt;", "completed": &lt;task completed status&gt;}, {"username": "&lt;username&gt;", "task": "&lt;task title&gt;", "completed": &lt;task completed status&gt;}, ... ], "&lt;user id&gt;": [ {"username": "&lt;username&gt;", "task": "&lt;task title&gt;", "completed": &lt;task completed status&gt;}, {"username": "&lt;username&gt;", "task": "&lt;task title&gt;", "completed": &lt;task completed status&gt;}, ... ]}</code>
    </p>

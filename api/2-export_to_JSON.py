#!/usr/bin/env python3

"""
This script retrieves tasks data from a mock API endpoint (https://jsonplaceholder.typicode.com/todos)
and exports tasks assigned to a specific user to a JSON file.

The script takes a user ID as a command-line argument and fetches all tasks associated with that user.
It then creates a JSON file named USER_ID.json containing the tasks in the following format:
{
    "USER_ID": [
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        {"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
        ...
    ]
}

Usage: python3 script.py USER_ID
"""

import json
import sys
import requests

class TaskExporter:
    """
    TaskExporter class handles the retrieval of tasks data and exporting them to a JSON file.
    """

    @staticmethod
    def export_to_json(user_id):
        """
        Retrieves tasks assigned to a specific user and exports them to a JSON file.

        Args:
            user_id (str): The ID of the user whose tasks are to be exported.
        """
        response = requests.get('https://jsonplaceholder.typicode.com/todos')
        tasks = response.json()

        user_tasks = []
        for task in tasks:
            if task['userId'] == int(user_id):
                user_task = {
                    'task': task['title'],
                    'completed': task['completed'],
                    'username': task['username']
                }
                user_tasks.append(user_task)

        filename = f"{user_id}.json"
        with open(filename, 'w') as json_file:
            json.dump({user_id: user_tasks}, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py USER_ID")
        sys.exit(1)

    user_id = sys.argv[1]
    TaskExporter.export_to_json(user_id)

import json
import sys
import requests

def export_to_json(user_id):
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
    export_to_json(user_id)

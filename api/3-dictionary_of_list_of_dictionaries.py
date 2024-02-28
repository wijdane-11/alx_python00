import json

# Sample data
data = {
    "1": [
        {"username": "Bret", "task": "delectus aut autem", "completed": False},
        {"username": "Bret", "task": "quis ut nam facilis et officia qui", "completed": False},
        # More tasks...
    ],
    "2": [
        {"username": "Antonette", "task": "suscipit repellat esse quibusdam voluptatem incidunt", "completed": False},
        {"username": "Antonette", "task": "distinctio vitae autem nihil ut molestias quo", "completed": True},
        # More tasks...
    ],
    # More users...
}

# Combine tasks of all users into a single dictionary
all_tasks = {}
for user_id, tasks in data.items():
    all_tasks[user_id] = tasks

# Export data to JSON
with open("todo_all_employees.json", "w") as file:
    json.dump(all_tasks, file, indent=4)

print("Data exported to 'todo_all_employees.json'")

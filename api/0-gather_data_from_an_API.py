#!/usr/bin/python3
"""
Gather data from an API
"""

import sys
import requests

def fetch_employee_data(employee_id):
    """
    Fetches employee data from the API.
    
    Args:
        employee_id (int): The ID of the employee.
        
    Returns:
        tuple: A tuple containing employee name, completed tasks count, total tasks count,
               and a list of completed tasks.
    """
    # Fetch employee details
    employee_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    employee_data = employee_response.json()
    employee_name = employee_data.get('name')

    # Fetch employee's TODO list
    todo_response = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    todo_data = todo_response.json()

    # Calculate progress
    total_tasks = len(todo_data)
    completed_tasks = sum(1 for task in todo_data if task.get('completed'))
    completed_titles = [task.get('title') for task in todo_data if task.get('completed')]

    return employee_name, completed_tasks, total_tasks, completed_titles

def main():
    """
    Main function to handle command line arguments and display output.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_name, completed_tasks, total_tasks, completed_titles = fetch_employee_data(employee_id)

    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for title in completed_titles:
        print(f"\t{title}")

if __name__ == "__main__":
    main()


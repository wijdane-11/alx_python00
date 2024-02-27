#!/usr/bin/python3
"""
Gather data from an API and export to CSV
"""

import csv
import requests
import sys
import os

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
    completed_tasks_info = [(employee_id, employee_name, task.get('completed'), task.get('title')) for task in todo_data]

    return completed_tasks_info

def export_to_csv(employee_id, data):
    """
    Exports data to a CSV file.
    
    Args:
        employee_id (int): The ID of the employee.
        data (list): List of tuples containing task information.
    """
    filename = f"{employee_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        csv_writer.writerows(data)

def user_info(id):
    """
    Displays user info and checks number of tasks in CSV file.
    
    Args:
        id (int): The ID of the employee.
    """
    try:
        with open(str(id) + ".csv", 'r') as f:
            num_tasks = sum(1 for line in f) - 1  # Subtract header row
        print(f"Number of tasks in CSV: {num_tasks} - OK")
    except FileNotFoundError:
        print(f"CSV file for user {id} not found.")

def main():
    """
    Main function to handle command line arguments and display output.
    """
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    completed_tasks_info = fetch_employee_data(employee_id)
    export_to_csv(employee_id, completed_tasks_info)
    user_info(employee_id)

if __name__ == "__main__":
    main()

#!/usr/bin/python3
"""Gather data from an API"""
import requests
from sys import argv
"""modules to work with"""

def get_employee_todos_progress(employee_id):
    """A function to return the info about employees' todos progress"""
    try:
        url = "https://jsonplaceholder.typicode.com/"
        user_datas = requests.get(url + f"users/{employee_id}")
        user_datas.raise_for_status()
        user_data = user_datas.json()
        employee_name = user_data["name"]

        """ Fetch employee todos list"""
        todos_list = requests.get(url + f"todos?userId={employee_id}")
        todos_list.raise_for_status()
        json_todos_list = todos_list.json()

        total_task = len(json_todos_list)
        task_done = [task for task in json_todos_list if task['completed']]
        no_task_done = len(task_done)

        """Display the results"""
        print(f"Employee {employee_name} is done with tasks "
              f"{no_task_done}/{total_task}:")

        """Title of completed tasks"""
        for task in task_done:
            print(f"\t {task['title']}")

    except requests.RequestException as e:
        print(f"An error occurred while fetching data: {e}")
    except KeyError:
        print("Invalid employee ID or data format has changed.")
    except Exception as e:
        print(f"An unexpected error has occurred: {e}")

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: script <employee_id>")
    else:
        get_employee_todos_progress(argv[1])


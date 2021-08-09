import sqlite3
from typing import List

def listTodos(undone: bool=False):
    def determineDoneChar(status: bool) -> str:
        return '✔' if status == 1 else 'x'

    def format_as_longest(task_list: List[str], task: str) -> str:
        max_length = max(list(map(lambda x: len(x), task_list)))

        return task + (" " * (max_length - len(task)))

    connection = sqlite3.connect('database.db')

    id_list = []
    task_list = []
    status_list = []

    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM todos"):
        if not undone or row[2] != 1:
            id_list.append(row[0])
            task_list.append(row[1])
            status_list.append(row[2])

    connection.close()

    if len(id_list) != 0:
        line_list = []

        for i in range(len(id_list)):
            line_list.append(f" {str(id_list[i]) + (' ' * (4 - len(str(id_list[i]))))} | {format_as_longest(task_list, task_list[i])} | {determineDoneChar(row[2])}")

        max_line_length = max(list(map(lambda x: len(x), line_list)))
        max_length = max(list(map(lambda x: len(x), task_list)))

        print(f"  id  | task{' ' * (max_length - 4)} |")

        for i in line_list:
            print("-" * (max_line_length + 1))
            print(i)
    else:
        print("Nothing to display")
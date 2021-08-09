import sqlite3

def listTodos(undone: bool=False):
    def determineDoneChar(status: bool) -> str:
        return '✔' if status == 1 else 'x'


    print("  id  | item ")
    print("----------------------")


    connection = sqlite3.connect('database.db')

    cursor = connection.cursor()
    for row in cursor.execute("SELECT * FROM todos"):
        if not undone or row[2] != 1:
            print(f" {str(row[0]) + (' ' * (4 - len(str(row[0]))))} | {row[1]}  {determineDoneChar(row[2])}")
            print("----------------------")

    connection.close()
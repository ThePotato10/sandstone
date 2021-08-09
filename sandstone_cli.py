from sqlite3.dbapi2 import connect
import click
import sqlite3
import os
from listTodos import listTodos


@click.group()
def sandstone():
    """A terminal-based todo list"""


@sandstone.command()
def init():
    """Setup Sandstone"""

    if not os.path.exists('database.db'):
        with open('database.db', 'w'): pass

    connection = sqlite3.connect('database.db')

    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todos (id INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT, done INT)')

    connection.commit()
    connection.close()

    print('Done')



@click.option('-d', '--done', is_flag=True, help="Create a todo with that's already marked as completed")
@click.option('-t', '--task', help="Task to be completed")
@sandstone.command()
def add(task: str, done: bool=False):
    """Add a todo to your list"""

    if not task:
        print("Flag -t is required. Please pass it and the todo you want to add")
        return

    try:
        connection = sqlite3.connect('database.db')

        cursor = connection.cursor()
        cursor.execute("INSERT INTO todos (todo, done) VALUES (?, ?)", (task, done))

        connection.commit()
        connection.close()

        listTodos()
    except:
        print("Error. Please check that your database is setup and saved as 'database.db'")


@click.option('-u', '--undone', is_flag=True, help="Only show the todos that are yet to be completed")
@sandstone.command()
def list(undone: bool=False):
    """Display all the todos in your todo list"""

    listTodos(undone)




@click.option('-i', '--_id', help="ID of todo item to complete")
@sandstone.command()
def complete(_id: str):
    """Mark a todo as done"""

    if not _id:
        print("-i flag is required. Please pass it and the id of the item to complete")
        return

    try:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("UPDATE todos SET done = 1 WHERE id = ?", (_id))

        connection.commit()
        connection.close()

        listTodos()
    except:
        print("Error. Please check that your database is setup and saved as 'database.db'")


@click.option('-i', '--_id', help="ID of todo item to uncomplete")
@sandstone.command()
def uncomplete(_id: str):
    """Mark a todo as not done"""

    if not _id:
        print("-i flag is required. Please pass it and the id of the item to uncomplete")
        return

    try:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("UPDATE todos SET done = 0 WHERE id = ?", (_id))

        connection.commit()
        connection.close()

        listTodos()
    except:
        print("Error. Please check that your database is setup and saved as 'database.db'")


@click.option('-i', '--_id', help="ID for todo item to delete")
@sandstone.command()
def delete(_id: str):
    """Delete a todo"""

    if not _id:
        print("-i flag is required. Please pass it and the id of the item to delete")
        return

    try:
        connection = sqlite3.connect("database.db")
        cursor = connection.cursor()

        cursor.execute("DELETE FROM todos WHERE id = ?", (_id))

        connection.commit()
        connection.close()

        listTodos()
    except:
        print("Error. Please check that your database is setup and saved as 'database.db'")


if __name__ == '__main__':
    sandstone(prog_name="sandstone")
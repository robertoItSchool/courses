import sqlite3
from typing import List

from database.task_store import TaskStore


class TaskStoreSql(TaskStore):
  def get_all(self) -> List[dict]:
    connection = self.__get_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    connection.close()
    dict = [{'name': x[0], 'type': x[1]} for x in tasks]
    return dict

  def __get_connection(self):
    connection = sqlite3.connect('database/task_db')
    return connection

  def add(self, task_info: dict):
    # open the connection to the database file
    connection = self.__get_connection()
    cursor = connection.cursor()
    # on the cursor object we execute our command(s)
    # command = "INSERT INTO tasks (name, type) VALUES ('" + task_info['name'] + "', '" + task_info['type'] + "')"
    command = "INSERT INTO tasks (name, type) VALUES ('%s', '%s')" \
              % (task_info['name'], task_info['type'])
    name = task_info['name']
    task_type = task_info['type']
    command = f"INSERT INTO tasks (name, type) VALUES ('{name}', '{task_type}')"
    cursor.execute(command)
    # commit == save to file
    connection.commit()
    connection.close()

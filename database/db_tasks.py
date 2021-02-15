import sqlite3


def add_task(name: str, task_type: str):
  # open the connection to the database file
  connection = sqlite3.connect('task_db')
  cursor = connection.cursor()
  # on the cursor object we execute our command(s)
  cursor.execute("INSERT INTO tasks (name, type) VALUES ('"
                 + name + "', '" + task_type + "')")
  # commit == save to file
  connection.commit()
  connection.close()


def get_tasks():
  connection = sqlite3.connect('task_db')
  cursor = connection.cursor()

  cursor.execute("SELECT * FROM tasks")
  tasks = cursor.fetchall()
  connection.close()
  dict = [{'name': x[0], 'type': x[1]} for x in tasks]
  return dict


def delete_task(name: str):
  connection = sqlite3.connect('task_db')
  cursor = connection.cursor()

  cursor.execute("DELETE FROM tasks WHERE name='" + name + "'")
  connection.commit()
  connection.close()


if __name__ == "__main__":
  # add_task('buy fruits', 'cooking')
  delete_task('clean the house')
  print(get_tasks())

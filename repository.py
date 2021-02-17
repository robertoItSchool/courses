from typing import List

from task import Task
import os
import json
from mapper import TaskMapper
from database.task_store import TaskStore
from database.task_store_file import TaskStoreFile
from database.task_store_sql import TaskStoreSql


class TaskRepository:
  def __init__(self, task_store: TaskStore):
    self.task_store = task_store

  def add(self, task: Task):
    task_dict = TaskMapper.to_dict(task)
    self.task_store.add(task_dict)

  def get(self) -> List[Task]:
    saved_info = self.task_store.get_all()
    tasks = [TaskMapper.to_object(info) for info in saved_info]
    return tasks

  def delete(self, task: Task):
    list_of_tasks = self.__read_from_file()
    tasks = [x for x in list_of_tasks if x['name'] != task.name]
    self.__write_to_file(tasks)

  def __add_task_info(self, list_of_tasks, task):
    # extract the info from the Task object
    list_of_tasks.append(TaskMapper.to_dict(task))
    return list_of_tasks

  def __write_to_file(self, list_of_tasks):
    # create a JSON
    file_content = json.dumps(list_of_tasks)
    # open the file for writing, create it if it does not exist
    file = open(self.file_name, 'w')
    # save it to the file
    file.write(file_content)
    file.close()


if __name__ == "__main__":
  task2 = Task('buy fruits', 'eating', difficulty=2)
  repo = TaskRepository(TaskStoreSql())
  # repo.delete(task2)
  tasks = repo.get()
  print(tasks)

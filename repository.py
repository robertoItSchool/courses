from typing import List

from task import Task
import os
import json
from mapper import TaskMapper


class TaskRepository:
  file_name = 'tasks.json'

  def add(self, task: Task):
    list_of_tasks = self.__read_from_file()
    json_list = self.__add_task_info(list_of_tasks, task)
    self.__write_to_file(json_list)

  def get(self) -> List[Task]:
    saved_info = self.__read_from_file()
    tasks = [TaskMapper.to_object(info) for info in saved_info]
    for task_info in saved_info:
      to_object = TaskMapper.to_object(task_info)
      to_object.new_info = 'new_value'
      tasks.append(to_object)
    return tasks

  def __add_task_info(self, list_of_tasks, task):
    # extract the info from the Task object
    list_of_tasks.append(TaskMapper.to_dict(task))
    # create a JSON
    file_content = json.dumps(list_of_tasks)
    return file_content

  def __write_to_file(self, file_content):
    # open the file for writing, create it if it does not exist
    file = open(self.file_name, 'w')
    # save it to the file
    file.write(file_content)
    file.close()

  def __read_from_file(self):
    # check if file was created
    if os.path.exists(self.file_name):
      # open the file for read
      file = open(self.file_name)
      # read and decode the file
      list_of_tasks = json.loads(file.read())
      file.close()
    else:
      # if no file => we have an empty list (no tasks were added)
      list_of_tasks = []
    return list_of_tasks


if __name__ == "__main__":
  task2 = Task('buy fruits', 'eating', difficulty=2)
  repo = TaskRepository()
  tasks = repo.get()
  print(tasks)



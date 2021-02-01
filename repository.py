from task import Task
import os
import json


class TaskRepository:
  file_name = 'tasks.json'

  def add(self, task: Task):
    list_of_tasks = self.read_list_of_tasks()
    json_list = self.add_to_list(list_of_tasks, task)
    self.write_to_file(json_list)

  def add_to_list(self, list_of_tasks, task):
    # extract the info from the Task object
    list_of_tasks.append({
      'name': task.name,
      'type': task.task_type,
      'deadline': task.deadline,
      'difficulty': task.difficulty,
    })
    # create a JSON
    file_content = json.dumps(list_of_tasks)
    return file_content

  def write_to_file(self, file_content):
    # open the file for writing, create it if it does not exist
    file = open(self.file_name, 'w')
    # save it to the file
    file.write(file_content)
    file.close()

  def read_list_of_tasks(self):
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
  repo.add(task2)

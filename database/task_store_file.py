import json
import os
from typing import List

from database.task_store import TaskStore


class TaskStoreFile(TaskStore):
  file_name = 'tasks.json'

  def get_all(self) -> List[dict]:
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

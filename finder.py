from task import Task
from repository import TaskRepository
from typing import List


class TaskFinder:
  def __init__(self):
    self.repo = TaskRepository()

  def find_by_type(self, task_type: str) -> List[Task]:
    tasks = [x for x in self.repo.get() if task_type == x.task_type]
    return tasks


if __name__ == "__main__":
  finder = TaskFinder()
  tasks = finder.find_by_type('eating')
  print(tasks[0].__dict__)

import unittest
from repository import TaskRepository
from task import Task
import json
import os


class TaskRepositoryTest(unittest.TestCase):
  def setUp(self):
    self.repo = TaskRepository()
    self.repo.file_name = 'tasks_test.json'
    self.json_tasks = [{"name": 'cook food', "type": "eating", "deadline": 'Tomorrow', "difficulty": 1}]

  def tearDown(self):
    os.remove(self.repo.file_name)

  def test_add(self):
    # set up the test
    task3 = Task('cook food', 'eating', 'Tomorrow')
    # execution
    self.repo.add(task3)
    # assertion - verify the result
    file = open('tasks_test.json')
    content = file.read()
    file.close()
    self.assertEqual(self.json_tasks, json.loads(content))

  def test_get(self):
    # set up the test
    file = open(self.repo.file_name, 'w')
    file.write(json.dumps(self.json_tasks))
    file.close()
    # execution
    tasks = self.repo.get()
    # assertion
    self.assertEqual(Task('cook food', "eating", 'Tomorrow', 1).__dict__,
                     tasks[0].__dict__)


if __name__ == '__main__':
  unittest.main()

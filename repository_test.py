import unittest
from repository import TaskRepository
from task import Task
import json
import os


class TaskRepositoryTest(unittest.TestCase):
  def test_something(self):
    # set up the test
    repo = TaskRepository()
    repo.file_name = 'tasks_test.json'
    task3 = Task('cook food', 'eating', 'Tomorrow')
    # execution
    repo.add(task3)
    # assertion - verify the result
    file = open('tasks_test.json')
    content = file.read()
    file.close()
    self.assertEqual([{"name": 'cook food', "type": "eating", "deadline": 'Tomorrow', "difficulty": 1}],
                     json.loads(content))
    # clean up
    os.remove('tasks_test.json')



if __name__ == '__main__':
  unittest.main()

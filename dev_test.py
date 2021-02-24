from database.task_store_sql import TaskStoreSql
import requests

if __name__ == "__main__":
  requests.delete('http://127.0.0.1:5000/task/learn_fstrings')

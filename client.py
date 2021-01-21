import requests
import json

# url = 'http://localhost:8000/hello'
# response = requests.get(url)
#
# print(response)
# print(response.content)
#
# url_post = 'http://localhost:8000/file'
# data = {'file_name': 'un_nume_de_fisier'}
# headers = {'file_name': 'fisier'}
# response = requests.post(url_post, json.dumps(data), headers=headers)

url_put = 'http://localhost:8000/file'
headers = {'file_name': 'fisier', 'content': 'hello'}
requests.delete(url_put, headers=headers)

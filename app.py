import flask
# .. = the above folder
# from .. import repository
from repository import TaskRepository

server = flask.Flask(__name__)


# define an API endpoint
@server.route('/hello')
def hello():
  return 'Hello world!'


# define what to show when accessing the server/
@server.route('/')
def main():
  repo = TaskRepository()
  tasks = repo.get()
  print('will show an HTML page')
  paragraph = 'content of our paragraph'
  html_template = flask.render_template('hello.html', p=paragraph, tasks=tasks)
  print(html_template)
  return html_template

from http.server import BaseHTTPRequestHandler
import os


class OurHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    print('get request')
    self.__get_hello()

  def do_POST(self):
    print('post request')
    self.__post_file()

  def do_PUT(self):
    print('put request')
    if self.path == '/file':
      print('file endpoint')
      file_name = self.headers.get('file_name')
      file = open(file_name, 'w')
      content = self.headers.get('content')
      file.write(content)
      file.close()
      self.__send_200_response()

  def do_DELETE(self):
    print('delete request')
    if self.path == '/file':
      file_name = self.headers.get('file_name')
      os.remove(file_name)
      self.__send_200_response()

  def __post_file(self):
    if self.path == '/file':
      print('file endpoint')
      file_name = self.headers.get('file_name')
      print('file name: ' + file_name)
      file = open(file_name, 'w')
      file.close()
      self.__send_200_response()

  def __get_hello(self):
    if self.path == '/hello':
      print('hello request')
      self.__send_200_response()
      # write the body (response.content)
      self.wfile.write(b'Hello world!')

  def __send_200_response(self):
    # put the status code 200 (means ok)
    self.send_response(200)
    # start the header space
    self.send_header('Content-type', 'application/json')
    # end the header space
    self.end_headers()

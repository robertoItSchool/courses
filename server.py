from http.server import HTTPServer
from request_handler import OurHandler

# if we execute the file, it will go here
if __name__ == "__main__":
  server_address = ('localhost', 8000)
  http_server = HTTPServer(server_address, OurHandler)
  try:
    http_server.serve_forever()
  except KeyboardInterrupt:
    pass
  http_server.server_close()

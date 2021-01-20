from http.server import BaseHTTPRequestHandler


class OurHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    if self.path == 'hello':
      # put the status code 200 (means ok)
      self.send_response(200)
      # end the header space
      self.end_headers()
      # write the body (response.content)
      self.wfile.write(b'Hello world!')

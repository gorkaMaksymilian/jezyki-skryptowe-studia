from http.server import HTTPServer, BaseHTTPRequestHandler
import codecs

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            file_to_open = codecs.open("index.html",encoding="utf-8").read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))


myServer = HTTPServer(('localhost', 8000), Serv)
print("Serwer działa: 127.0.0.1:8000")
try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()

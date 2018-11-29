from http.server import HTTPServer, BaseHTTPRequestHandler
import codecs
import os

 
 
class StaticServer(BaseHTTPRequestHandler):
 
    def do_GET(self):
        root =os.getcwd()
        print(self.path)
        if self.path == '/':
            filename = root + '\index.html'
        else:
            filename = root + self.path
 
        self.send_response(200)
        if filename[-4:] == '.css':
            self.send_header('Content-type', 'text/css')
        else:
            self.send_header('Content-type', 'text/html')
        self.end_headers()
        with codecs.open(filename,encoding="utf-8") as fh:
            html = fh.read()
            html = bytes(html, 'utf8')
            self.wfile.write(html)

 

port=8000
server_address = ('', port)
httpCSS = HTTPServer(server_address, StaticServer)
print('Serwer działa: localhost na porcie {}'.format(port))

try:
	httpCSS.serve_forever()
except KeyboardInterrupt:
	pass
    

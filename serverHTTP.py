from http.server import HTTPServer, BaseHTTPRequestHandler
import codecs
import os
import default
import logging
sock=default.DEFAULT_SERVERHTTP["socketConfig"]

logger=logging.getLogger(__name__)
logger.setLevel(default.DEFAULT_LOG["level"])
formatter=logging.Formatter(""+default.DEFAULT_LOG["formatter"]+"")
file_handler = logging.FileHandler(""+default.DEFAULT_LOG["file"]+"")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
 
 
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

 
port=default.DEFAULT_SERVERHTTP["port"]
czyWolny=default.DEFAULT_SERVERHTTP["boolean"]

while czyWolny:
    result = sock.connect_ex(('127.0.0.1',port))
    if result == 0:
       print ("\nPort {} jest zajety.\nPodaj inny numer portu:".format(port))
       logger.warning("port dla serwera jest zajety.")
       port=int(input())
    else:
        
       print ("Port jest wolny.\nŁącze sie z 127.0.0.1:{}".format(port))
       logger.info("port dla serwera jest wolny.")
       czyWolny=False
       

server_address = ('', port)
httpCSS = HTTPServer(server_address, StaticServer)
print('Serwer działa: localhost na porcie {}'.format(port))
logger.info("Serwer zostal uruchomiony prawidlowo")
try:
	httpCSS.serve_forever()
except KeyboardInterrupt:
    logger.warning("Serwer zostal wylaczony") 
    pass

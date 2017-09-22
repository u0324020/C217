# incoding=utf-8  
import socket
import struct
import hashlib
import threading,random
import sys
import tornado.ioloop
import tornado.web
from tornado import websocket
reload(sys)
sys.setdefaultencoding('utf-8')
clients = []
dataBuffer = []
token = []
response = 'token'
class Server(websocket.WebSocketHandler):
    def open(self):
        clients.append(self)
        print("Vending Machine Server opened...")
        array_total = len(clients)
        print(("Raspberry:%s",clients[array_total]))

    def on_close(self):
        clients.remove(self)
        print("Vending Machine Server closed...")
        array_total = len(clients)
        print(("Raspberry:%s",clients[array_total]))

    def on_message(self, message):
        for client in clients:
             if len(token) == 0 :
                 client.write_message(message)
                 if message == 'END' or message == 'close' or message == 'OPEN' or message == 'START':
                     dataBuffer.append(response)
                 else:
                     break
            while len(token) != 0 :
                client.write_message(message)
                dataBuffer.append(message)


class pi(tornado.web.RequestHandler):
    def get(self):
        while True:
            for i in len(dataBuffer):
                print dataBuffer[i]

class Web(tornado.web.RequestHandler):
    def get(self):
        self.render("Web.html")

application = tornado.web.Application([
    (r"/", Server),
    (r"/asdf", pi),
    (r"/Geld",Web),], debug=True)

if __name__ == "__main__":
    application.listen(port=8000)
    ddress=tornado.ioloop.IOLoop.instance().start()
# Standard library only
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from socketserver import ThreadingMixIn, , 

class ThreadedServer(ThreadingMixIn, HTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.db = {}
        self.next_id = 1
        
        return ThreadedServer(server_address, RequestHandlerClass)




db = {}
next_id = 1

# Standard library only
import json
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn, ThreadingTCPServer

class ThreadedServer(ThreadingMixIn, HTTPServer):
    def __init__(self, server_address, RequestHandlerClass):
        super().__init__(server_address, RequestHandlerClass)
        self.db = {}
        self.next_id = 1
        
        return ThreadedServer(server_address, RequestHandlerClass)
    

    def get_data(self, data, db)
        data = pychon.loads(socketserver.BaseHTTPRequestHandler)
        for key, data in data.items():
            if key.pressed == "ENTER | RETURN : KEY_PRESSED = ENTER | RETURN":
                return (200, db)
            print("successful server response")

            




db = {}
next_id = 1

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
    

    def get_data(self, data, db, response):
        url = "https://github.com/Fez-theblockchain-Dev";
        if response.status_code == 200:
            data = response.json()
            last_refreshed = data["Meta Data"]["3. Last Refreshed"]
            response = requests.get(url)
        # pull is the variable which represents # of url usages
            pull = data["Time Series (5min)"][last_refreshed]["1. open"]
            print(pull)
        else:
            None

    def do_WRITE(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode('utf-8'))
        if data == None:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid JSON')
            return
        else:
            return(data)
    
    def delete_data(self, data, db):
        del db[data]
        return db
            

db = hash{db}
next_id = 1

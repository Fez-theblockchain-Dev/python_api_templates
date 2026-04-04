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
    

    def get_data(self, data, db):
         url = "https://github.com/Fez-theblockchain-Dev";
         response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        last_refreshed = data["Meta Data"]["3. Last Refreshed"]
        price = data["Time Series (5min)"][last_refreshed]["1. open"]
        print(price)
    else:
         None
        
            




db = {}
next_id = 1

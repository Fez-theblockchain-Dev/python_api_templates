from flask import Flask, jsonify
from flask_restful import Resource, Api
app = Flask(__name__)
api = Api(app)

db = ('')

config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,
}

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return jsonify({'message': 'Greetings Earthlings'})

class Square(Resource):
    def get(self, num):
        return jsonify({'square': num ** 2})

api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')


# currently the f string in the function is not connecting the 
def connection_err(self, api):
    print("connection error: click {} to see ")

if __name__ == '__main__':
    app.run(debug=True)

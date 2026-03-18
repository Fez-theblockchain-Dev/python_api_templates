from flask import Flask, jsonify
from flask.json.provider import DefaultJSONProvider
from datetime import datetime, date, timezone
from decimal import Decimal
from uuid import UUID
import json
from flask_restful import Resource, Api

# --- Setup ---
app = Flask(__name__)
app.json_provider_class = CustomJSONProvider
app.json = CustomJSONProvider(app)


config = {
    "DEBUG": True,
    "CACHE_TYPE": "simple",
    "CACHE_DEFAULT_TIMEOUT": 300,
}

app = Flask(__name__)
api = Api(app)

class Hello(Resource):
    def get(self):
        return({'message': 'Greetings Earthlings'})

class Square(Resource):
    def get(self, num):
        return ({'square': num ** 2})
    

    """ This comment OUTLINES WHAT THE CustomJsonProvider class is doing on line
        Packages API request data into a standardized JSON response structure.
        Handles custom serialization for common Python types.
        
        Args:
            data: The data from the API fetch request to be packaged
            **kwargs: Additional keyword arguments passed to the JSON encoder
            
        Returns:
            A JSON Response object with standardized structure
    """
class CustomJSONProvider(DefaultJSONProvider):
    def jsonify(self, data, **kwargs):
        packaged = {
            "status": "success",
            "data": data,
            "meta": {
                "timestamp": datetime.utcnow().isoformat(),
                "type": type(data).__name__
            }
        }
        #responds with success API msg code if the data is packaged successfully
        return self.app.response_class(
            response=self.dumps(packaged, **kwargs),
            status=200,
            mimetype="application/json"
        )
    
    def default(self, obj):
        """
        Extends the default JSON serializer to handle additional Python types.
        Falls back to the parent class for unrecognized types.
        """
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        
        if isinstance(obj, Decimal):
            return float(obj)
        
        if isinstance(obj, UUID):
            return str(obj)
        
        if isinstance(obj, set):
            return list(obj)
        
        if isinstance(obj, bytes):
            return obj.decode("utf-8")
        
        return super().default(obj)


# --- Usage in a route ---
@app.route("/api/data", methods=["GET", "POST"])
def fetch_data():
    # Simulate ingested user data from an API fetch request
    user_data = {
        "user_id": UUID("12345678-1234-5678-1234-567812345678"),
        "fetched_at": datetime.utcnow(),
        "balance": Decimal("199.99"),
        "tags": {"flask", "api", "json"},
        "raw_bytes": b"hello",
    }

    return app.json.jsonify(user_data)


if __name__ == "__main__":
    app.run(debug=True)



api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')


# currently the f string in the function is not connecting the 
def connection_err(self, api):
    print("connection error: click {} to see ")

if __name__ == '__main__':
    app.run(debug=True)

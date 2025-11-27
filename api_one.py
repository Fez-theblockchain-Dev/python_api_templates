from flask import Flask
app = Flask(__name__)

db = ('/https.neon/online_math_game')


class game(db.Modal):

    @app.route(db)
    def api():
        print('Welcome!')


        


from flask import Flask, request
from flask_cors import CORS
import glob
import os

from flask_cors import cross_origin

from connection import connect_to_db
import json

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/list_all')
def select_all():
    cursor, conn = connect_to_db()
    cursor.execute("SELECT user_id, lifting_total, bodyweight, sumo FROM users")
    to_return = {}
    for row in cursor.fetchall():
        to_return[row[0]] = {
            'user_id': row[0],
            'lifting_total': row[1],
            'bodyweight': row[2],
            'sumo': row[3],
        }
        a=1
    conn.close()
    return json.dumps(to_return)


@app.route('/register', methods=['POST'])
def register():

    print('register')
    g = request.get_json().get
    cursor, conn = connect_to_db()
    cursor.execute(
        "INSERT INTO users "
        "VALUES"
        "(DEFAULT, %s, %s, %s, %s, %s)",
        (g('lifting_total'),
         g('bodyweight'),
         g('name'),
         g('sumo', False),
         g('peds', False))
    )
    conn.commit()
    return 'ok', 200


@app.route('/remove', methods=['GET', 'POST'])
@cross_origin(origin='*')
def remove():
    """Remove all uploads"""

    for f in glob.glob(os.getcwd() + "/uploads/*.txt"):
        os.remove(f)

    return 'ok', 200


# if running with PyCharm
if __name__ == '__main__':
    app.run()

# if running with gunicorn
application = app

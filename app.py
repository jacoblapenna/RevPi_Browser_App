import redis

from Server import Server
from DataStreamer import DataStreamer

from flask import Flask, render_template
from flask_socketio import SocketIO

import eventlet
eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, message_queue='redis://')

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    if redis.Redis().ping():
        # make sure redis-server.service is running
        pass
    else:
        raise Exception("Check that redis-server.service is running!")
    server = Server()
    streamer = DataStreamer()
    socketio.run(app,
                 host=server.ip,
                 port=8080,
                 use_reloader=True,
                 debug=True,
                 extra_files=["templates/index.html"])

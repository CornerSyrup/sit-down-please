from threading import Thread

from flask import Flask, send_from_directory
from flask_cors import CORS, cross_origin

from core import load_modules

triggers = load_modules("triggers")
monitors = load_modules("monitors")


def daemon():
    while True:
        for m in monitors:
            m.on_update(triggers)


Thread(target=daemon, daemon=True)


app = Flask("sit-down-please")
CORS(app)


@app.route("/api")
@cross_origin()
def status():
    return send_from_directory("data", "status.json")

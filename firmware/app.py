from threading import Thread

from flask import Flask, send_from_directory

from core import load_modules

triggers = load_modules("triggers")
monitors = load_modules("monitors")


def daemon():
    while True:
        for m in monitors:
            m.on_update(triggers)


Thread(target=daemon, daemon=True)


app = Flask("sit-down-please")


@app.route("/api")
def status():
    return send_from_directory("data", "status.json")

from threading import Thread

from flask import Flask, send_file

from core import load_modules

triggers = load_modules("triggers")
monitors = load_modules("monitors")


def daemon():
    while True:
        for m in monitors:
            m.on_update(triggers)


Thread(target=daemon, daemon=True)


app = Flask("sit-down-please")


@app.route("/")
def status():
    return send_file("data/status.json")

import glob
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

IR_PIN = 18
GPIO.setup(IR_PIN, GPIO.IN)


def load_modules(group: str):
    return map(
        lambda module: getattr(__import__(f"{group}.{module}"), module),
        map(
            lambda path: path.replace("\\", ".").replace("/", ".").split(".")[1],
            glob.glob(f"{group}/*.py"),
        ),
    )


last_sec = int(time.time())
curr_sec = 0

is_occupied = False
now_occupied = False

monitors = load_modules("monitors")

for mon in monitors:
    mon.install()

while True:
    last_sec = curr_sec
    curr_sec = int(time.time())

    if last_sec != curr_sec:
        for mon in monitors:
            if "on_second" in mon:
                mon.on_second(curr_sec)

    now_occupied = bool(GPIO.input(IR_PIN))
    if is_occupied != now_occupied:
        if now_occupied:
            for mon in monitors:
                if "on_occupied" in mon:
                    mon.on_occupied()
        else:
            for mon in monitors:
                if "on_available" in mon:
                    mon.on_available()

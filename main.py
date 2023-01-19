import glob
import time


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

monitors = load_modules("monitors")

while True:
    last_sec = curr_sec
    curr_sec = int(time.time())

    if last_sec == curr_sec:
        continue

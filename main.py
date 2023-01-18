import time

if __name__ != "__main__":
    exit()

last_sec = int(time.time())
curr_sec = 0

while True:
    last_sec = curr_sec
    curr_sec = int(time.time())

    if last_sec == curr_sec:
        continue

    print(curr_sec)

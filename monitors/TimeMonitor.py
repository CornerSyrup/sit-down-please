import time


class TimeMonitor:
    last_sec = int(time.time())
    curr_sec = 0

    def install():
        return TimeMonitor()

    def on_update(self, triggers):
        self.last_sec = self.curr_sec
        self.curr_sec = int(time.time())

        if self.last_sec != self.curr_sec:
            for mon in triggers:
                if "on_second" in dir(mon):
                    mon.on_second(self.curr_sec)

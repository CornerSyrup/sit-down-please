from core import Trigger, set_data, read_data
import time


class SeatTriggers(Trigger):
    @staticmethod
    def install():
        return SeatTriggers()

    def on_occupied(self):
        set_data("status", "seat", int(time.time()))

    def on_available(self):
        last = read_data('status')['leave']
        now = int(time.time())
        if now - last > 10:
            set_data("status", "leave", int(time.time()))

    def on_second(self, second: int):
        pass

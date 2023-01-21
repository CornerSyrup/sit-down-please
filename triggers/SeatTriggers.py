from core import Trigger


class SeatTriggers(Trigger):
    @staticmethod
    def install():
        return SeatTriggers()

    def on_occupied(self):
        print("now occupied")

    def on_available(self):
        print("now available")

    def on_second(self, second: int):
        print(second)

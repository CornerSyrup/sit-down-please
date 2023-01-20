class SeatMonitor:
    def install():
        return SeatMonitor()

    def on_occupied(self):
        print("now occupied")

    def on_available(self):
        print("now available")

    def on_second(self, sec: float):
        print(sec)

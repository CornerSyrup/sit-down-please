from typing import Iterable

import RPi.GPIO as GPIO

from core import Monitor, Trigger

IR_PIN = 18


class OccupiedMonitor(Monitor):
    is_occupied = False
    now_occupied = False

    @staticmethod
    def install():
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(IR_PIN, GPIO.IN)
        return OccupiedMonitor()

    def on_update(self, triggers: Iterable[Trigger]):
        self.now_occupied = bool(GPIO.input(IR_PIN))
        if self.is_occupied != self.now_occupied:
            self.is_occupied = self.now_occupied

            if self.now_occupied:
                for mon in triggers:
                    if "on_occupied" in dir(mon):
                        mon.on_occupied()
            else:
                for mon in triggers:
                    if "on_available" in dir(mon):
                        mon.on_available()

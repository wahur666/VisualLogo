# -*- coding: utf-8 -*-

class Timer:

    def __init__(self):
        self.counter = 0

    def wait(self, sec):
        self.counter = int(sec * 60)

    def tick(self):
        if self.counter > 0:
            self.counter -= 1

    def is_waiting(self):
        return self.counter != 0

    def stop(self):
        self.counter = 0
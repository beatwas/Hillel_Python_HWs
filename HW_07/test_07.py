"""
Реализовать класс цифрового счетчика. В классе реализовать методы:

установки максимального, минимального и начального значения счётчика (предусмотреть установку счётчика значениями по умолчанию 0-100)
увеличения счетчика на 1
возвращения текущего значения счётчика
"""


class DigitalCounter:

    def __init__(self, start=0, end=100, current=None):
        if end < start:
            self.start = 0
            self.end = 100
            print("Incorrect class creation. Values are set by default")
        else:
            self.start = start
            self.end = end
        if current < start | current > end:
            self.current = None
            print("Incorrect class creation. Values are set by default")
        else:
            self.current = current

    def increase(self):
        if self.current is None | self.current < self.start | self.current > self.end:
            self.current = self.start + 1
        elif self.current < self.end:
            self.current += 1
        elif self.current == self.end:
            print("The maximum value of the counter has been reached")

    def get_current_value(self):
        return self.current

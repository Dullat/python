class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start(self):
        print("starting...")
    @staticmethod
    def stop(self):
        print("stopping...")

class Toyota(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

c1 = Toyota("fortuner", "petrol")
print(c1.type)

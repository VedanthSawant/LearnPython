class Car:
    def __init__(self):
        self.seats = 5

    def enter_race_mode(self):
        self.seats = 2

obj = Car()
print(obj.seats)
obj.enter_race_mode()
print(obj.seats)
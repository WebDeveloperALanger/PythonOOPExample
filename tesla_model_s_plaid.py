class Car:
    def __init__(self, manufacturer, model_name, max_speed):
        self.manufacturer = manufacturer
        self.model_name = model_name
        self.max_speed = max_speed
        self.current_speed = 0

    def increase_speed(self, kmh):
        new_speed = self.current_speed + kmh
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        else:
            self.current_speed = new_speed

    def reduce_speed(self, kmh):
        new_speed = self.current_speed - kmh
        if new_speed <= 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def info(self):
        return self.manufacturer + " " + self.model_name + " at " + str(self.current_speed) + " km/h"

    def print_info(self):
        print(self.info())


class TeslaModelSPlaid(Car):
    def __init__(self):
        super().__init__("Tesla", "Model S Plaid", 322)


MyNewCar = TeslaModelSPlaid()

MyNewCar.increase_speed(50)
MyNewCar.increase_speed(50)
MyNewCar.increase_speed(50)
MyNewCar.print_info()           # Tesla Model S Plaid at 150 km/h

MyNewCar.increase_speed(800)
MyNewCar.print_info()           # Tesla Model S Plaid at 322 km/h
# test
MyNewCar.reduce_speed(400)
MyNewCar.print_info()           # Tesla Model S Plaid at 0 km/h

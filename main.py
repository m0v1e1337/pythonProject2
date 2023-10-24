class Engine:
    def __init__(self, weight, max_speed, fuel_consumption):
        self.weight = weight
        self.max_speed = max_speed
        self.fuel_consumption = fuel_consumption

class Tank:
    def __init__(self, weight, volume):
        self.weight = weight
        self.volume = volume

class Brakes:
    def __init__(self, weight, efficiency):
        self.weight = weight
        self.efficiency = efficiency

class Body:
    def __init__(self, weight):
        self.weight = weight

class Car:
    def __init__(self, name, engine, tank, brakes, body):
        self.name = name
        self.engine = engine
        self.tank = tank
        self.brakes = brakes
        self.body = body
        self.weight = self.calculate_weight()
        self.max_distance = self.calculate_max_distance()
        self.braking_distance = self.calculate_braking_distance()

    def calculate_weight(self):
        total_weight = self.engine.weight + self.tank.weight + self.brakes.weight + self.body.weight
        return total_weight

    def calculate_max_distance(self):
        max_distance = (self.tank.volume * self.engine.fuel_consumption) / 100
        return max_distance

    def calculate_braking_distance(self):
        braking_distance = self.weight * self.brakes.efficiency
        return braking_distance


class Builder:
    pass


builder = Builder()

engine = Engine(200, 200, 10)
tank = Tank(150, 60)
brakes = Brakes(100, 1.5)
body = Body(500)

car = Car("Classic Car", engine, tank, brakes, body)

print("Car name:", car.name)
print("Car weight:", car.weight)
print("Max distance with full tank:", car.max_distance)
print("Braking distance:", car.braking_distance)
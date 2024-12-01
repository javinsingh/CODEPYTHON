class vehicle:
    def __init__(self, max_speed, mileage):
       self.max_speed = max_speed
       self.mileage = mileage
tesla = vehicle(240, 18)
print("model max speed", tesla.max_speed)
print("model mileage",tesla.mileage)


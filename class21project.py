class cybertruck:
    def brand(self):
        print("i am a tesla")
    def mileage(self):
        print("my mileage is 136")
    def top_speed(self):
        print("my top speed is 112 mph")
class aventador:
    def brand(self):
        print("i am a lamborgini")
    def mileage(self):
        print("my mileage is 7.69 kmpl")
    def top_speed(self):
        print("my top speed is 217 mph")
obj_av = aventador()
obj_cy = cybertruck()
for car in (obj_av, obj_cy):
    car.brand()
    car.mileage()
    car.top_speed()
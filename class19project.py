class vehicle:
    def __init__(self, fees):
        self.fees = fees
class buss_fair(vehicle):
    pass
buss = buss_fair(100)
print("bussfair:",buss.fees)


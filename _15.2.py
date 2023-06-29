class Transport:
    def __init__(self, name, max_speed, mileage):

        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        

class Autobus(Transport):
    def seating_capacity(self, capacity):

        #self.capacity = 50
        return f"Вместимость одного автобуса {self.name}: {capacity} пассажиров"



N = Autobus("BMW", 200, 300000)


print(f"{N.seating_capacity(60)}.")

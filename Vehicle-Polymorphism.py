class BMW:

    def fuel_type(self):
        return "Dieseal"
    

class Ferrari:

    def fuel_type(self):
        return "Petrol"
    
cars = [BMW(),Ferrari()]
for car in  cars:
    print(car.fuel_type())
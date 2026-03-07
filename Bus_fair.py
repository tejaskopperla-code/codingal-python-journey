class Vehicle:
    def __init__(self, capacity: int):
        self.capacity = capacity

    def fare(self) -> float:
        
        return self.capacity * 100

class Bus(Vehicle):
    def fare(self) -> float:
        
        base_amount = super().fare()
        
        return base_amount * 1.1


school_bus = Bus(capacity=50)
print(f"Total Bus Fare: {school_bus.fare()}") 
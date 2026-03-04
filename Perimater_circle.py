import math

class Circle:
    def __init__(self, radius: float):
        self.__radius = radius  

    def calculate_perimeter(self) -> float:
        
        return 2 * math.pi * self.__radius

    def __str__(self) -> str: 
        p = self.calculate_perimeter()
        return f"Circle Protocol | Radius: {self.__radius} | Perimeter: {p:.4f}"

subject_unit = Circle(radius=7.5)
print(subject_unit) 
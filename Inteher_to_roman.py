class RomanConverter:
    def __init__(self):
        
        self.map = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }

    def convert(self, num: int) -> str:
        roman_num = ""
        for value, symbol in self.map.items():
            while num >= value:
                roman_num += symbol
                num -= value
        return roman_num


subject = RomanConverter()

print(f"Roman Designation: {subject.convert(2026)}") 

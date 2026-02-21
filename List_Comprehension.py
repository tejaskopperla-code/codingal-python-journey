num = int(input("Enter a number: "))

odd_list = [x for x in range(num) if x % 2 != 0]
even_list = [x for x in range(num) if x % 2 == 0]

print("Odd numbers:", odd_list)
print("Even numbers:", even_list)


fruits = ["apple", "banana", "mango", "grapes"]

capital_fruits = [fruit.capitalize() for fruit in fruits]

print(capital_fruits)
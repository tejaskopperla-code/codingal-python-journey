start = int(input("Enter starting number"))
end = int(input("Enter ending number"))

squares = []
even = []
odd = []

for i in range (start,end +1):
    sq = i * i
    squares.append(sq)
    
    if sq % 2 == 0 :
        even.append(sq)

    else :
        odd.append(sq)

print('Squares',squares)
print("Even Squares",even)
print("Odd Squares",odd)
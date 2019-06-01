for values in range(1,6):
    print(values)

numbers = list(range(1,6))
print(numbers)
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
#numbers[5]
#numbers[6]
#Even Numbers
even_numbers = list(range(2,11,2))
print(even_numbers)
#Square Numbers

squares = []
for value in range(1,11):
#    square = value**2
#    square = square+square
    squares.append(value**2)

print(squares)

digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))
print(max(digits))
print(sum(digits))


sq = [val**2 for val in range(1,11)]
print("Squares are equal to = "+str(sq))

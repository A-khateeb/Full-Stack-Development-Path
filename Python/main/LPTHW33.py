i = 0
numbers = []
print("Insert a number to compare ")
j = input(">")
while i < add_manual(j):
    print(f"At the top i is {i}")
    numbers.append(i)
    i=i+1
    print("Numbers now:", numbers)
    print(f"At the bottom: {i}")

print("The numbers: ")
for num in numbers:
    print(num)

from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_over(self):
        return randint(1,self.sides)

d6 = Die()

results = []

for roll_num in range(10):
    result = d6.roll_over()
    results.append(result)

print("10 rolls of 6-sided die:")
print(results)


d10 = Die(sides = 20)
results = []
for roll_num in range(10):
    result = d10.roll_over()
    results.append(result)

print("10 rolls of 20 sided die: ")
print(results)

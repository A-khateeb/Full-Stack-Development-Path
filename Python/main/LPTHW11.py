print("How old are you?", end=" ")
age = int(input())
print("How tall are you?", end=" ")
tall = int(input())
print("How much do you weight", end=" ")
weight = int(input())
print("What is your gender ?", end = " ")
gender = input()
total = weight+age+tall
print(f"You are {gender} You'r age is {age} old, {tall} height, and {weight} heavy, with a total of {total}")

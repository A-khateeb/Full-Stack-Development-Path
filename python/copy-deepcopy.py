import copy

spam = [["A", "B", "C", "D"],["Hello","Hi"]]
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(spam)
print(cheese)
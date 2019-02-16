import re

greedy = re.compile("(Ha){3,5}")
mo_greedy = greedy.search("HaHaHaHaHa")
print("Greedy "+mo_greedy.group())

non_greedy = re.compile("(Ha){3,5}?")
moNonGreedy = non_greedy.search("HaHaHaHaHa")
print("Non Greedy "+moNonGreedy.group())

def find_second(string1,string2):
    find_string = string1.find(string2)
    find_accurate = string1.find(string2,find_string+1)
    return find_accurate

twister = "she sells seashells by the seashore"
print (find_second(twister,'she'))

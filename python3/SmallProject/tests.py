import sys
def split_string(sources, splitlist):
    output = []
    atsplitpoint = True
    for char in sources:
        if char in splitlist:
            atsplitpoint = True
        else:
            if atsplitpoint:
                output.append(char)
                atsplitpoint = False
            else:
                output[-1] = output[-1] + char
    return output

print (split_string("Hello world !","!"))


print (split_string("This is a test-of the,string separation-code!"," ,!-"))


out = split_string("After  the flood   ...  all the colors came out.", " .")
print (out)
#>>> ['After', 'the', 'flood', 'all', 'the', 'colors', 'came', 'out']

out = split_string("First Name,Last Name,Street Address,City,State,Zip Code",",")
print (out)
#>>>['First Name', 'Last Name', 'Street Address', 'City', 'State', 'Zip Code']

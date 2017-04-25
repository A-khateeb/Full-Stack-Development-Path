import pprint

message = "it was a bright cold day in April, and the clock were striking thirteen"

count= {}
for i in message:
    count.setdefault(i,0)
    count[i] = count[i]+1

pprint.pprint(count)
#print(pprint.pformat(count))
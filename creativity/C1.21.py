s = []
print("Insert information and then press on CTRL+D when you finish")
try:
    while True:
        a = input()
        s.append(a)
except EOFError:
    s.reverse()
    print("Print the information in reverse mode")
    for x in s:
        print(x)

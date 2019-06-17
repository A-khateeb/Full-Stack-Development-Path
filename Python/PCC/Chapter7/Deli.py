sandwich_orders = ['tuna','salamon','cheese','humus','falafel']
finished_sandwiches = []
while sandwich_orders:
    current_sand = sandwich_orders.pop()
    print("I just made " + current_sand.title())
    finished_sandwiches.append(current_sand)
print("\n\n")
for i in finished_sandwiches:
    print(i.title() + " done! ")
#print(finished_sandwiches)

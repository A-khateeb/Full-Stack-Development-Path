# requested_topping = ["mushrrom","green peppers","extra cheese"]
# for i in requested_topping:
#     if i == "green peppers":
#         print("We ran out of green peppers now!\n")
#     else:
#         print("Adding " + i + ".\n")
#
# print("Finished making your pizza")
#To check if the list is empty or not
# requested_topping = []
# if requested_topping:
#     for i in requested_topping:
#         print("Adding " + requested_topping )
#     print("finished adding toppings")
# else:
#     print("Are you sure that you want a plain pizza")
requested_topping = ["mushroom","french fries","extra cheese"]
availbale_topping = ["mushroom","olives","extra cheese","peperonni","green peppers","pinapple"]


for i in requested_topping:
    if i in availbale_topping:
        print("Adding " + i)
    else:
        print("We are sorry, we do not have " + i)

print("Finished making your pizza")

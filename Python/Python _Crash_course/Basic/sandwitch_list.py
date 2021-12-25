print(".....Order Management System....\n\n")
sandwitch_orders = []
order_list = True

while order_list:
    order = input("Enter your Sandwich order:")
    
    print("I am your "+order+" sandwitch.")
    sandwitch_orders.append(order)
    repeat = input("Would you like to order again? (yes/ no) ")
    if repeat == 'no':
        order_list = False

print(sandwitch_orders)
#------- Finish 
finished_sandwiches = []
while sandwitch_orders:
    move = sandwitch_orders.pop()
    # print("Verifying user: "+ move.title())
    finished_sandwiches.append(move)
# print(finished_sandwiches)

# finished_sandwiches = ['apple','banana','aa']
print("\nThe following Sandwiches are Finished:")
count = 1
# for confirmed_user in finished_sandwiches:
#     print(count+" "+confirmed_user.title()+" Sandwiches.")   
for num, name in enumerate(finished_sandwiches, start=1):
    # print(count+" "+confirmed_user.title()+" Sandwiches.")
    print("Order Number {}: {} Sandwiches is Finished".format(num, name))   
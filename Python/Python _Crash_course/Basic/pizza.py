### Passing an arbitrary number of arguments
def make_pizza(size,*toppings):
    # print("\nMaking a pizza with the following toppings:")
    print("\nMaking a " + str(size)+ "-inch pizza with the following toppings:") 
    for topping in toppings:
        print("- "+ topping)
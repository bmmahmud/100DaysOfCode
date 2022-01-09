#### Restaurent Order System using Function

#show menu card
def show_manue(menue):
    for item,price in menue.items():
        print(item.title()+" - Price: "+str(price)+"Tk") 

# Add Order items
def order_items():
    order_items.total_price = 0
    x = True
    while x:
        items = input("Enter Item Name:")
        x = items
        if (items in orders):
            print("Already ordered!!! Try Somthing New")
            continue
        else:
            if x == 'done':
                x = False
            else:  
                qty = int(input("Quantity:"))  # issue: if type  done show error, need to find solution
                print("Order More or Type -> done")
                order_items.total_price += (menue[items] * qty)
                orders.append(items)

# Show Card
def show_cart(orders):
    print("You order the follwing Items: ")
    for i in range(len(orders)):
        print(str(i+1)+" - "+orders[i].title() +" - "+str(menue[orders[i]]))
    print("Your Total Price: "+str(order_items.total_price))

## Start main function
print("#"*30+"\n    Welcome To Hacker Caffe\n"+"#"*30+ \
"\nPlease Chose your Order:")

# Declare Variables
menue = {"coffe":350,
"burgers":250,
"meatloaf":150,
"lasagna":220
}

orders = [] # issue it has to be a dictionary not a list
qty= 1

# Show menue
show_manue(menue)
print('#'*30)

# Add item 
order_items()
print('#'*30)

# Show card list
show_cart(orders)

#End    
print('#'*30+"\nThanks! Order Again.\n") 
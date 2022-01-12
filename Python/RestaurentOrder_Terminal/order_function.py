#### Restaurent Order System using Function

# check input numeric validation
def numeric_validation(value):
    while True:
        try:
            val = int(input(value))
        except:
            print('Please use numeric digits.')
            continue
        if val < 0:
            print('Please enter a positive number.')
            continue
        else:
            break
    return val

# convert into interger
def convert_numeric(value):
    if value in range(1,100):
        val = int(value)
        return val
#show menu card
def show_manue(menue):
    for item,value in menue.items():
        print("No#",item,": Item: ",value["item"].title(),"- Price:"+str(value["price"])+"Tk")

# Add Order items
def order_items(orders):
    order_items.total_price = 0
    run = True
    while run:
        orderList = orders
        items = numeric_validation("Enter Item No:")
        if (items in orderList):
            print("Already ordered!!! Try Somthing New")
            continue
        else:
            items_no = int(items)
            qty = numeric_validation("Quantity:")  
            order_items.total_price += (menue[items_no]['price'] * qty)
            orderList.append(menue[items_no]['item'])
            order = input("Do you want to order more? y/n:")
            if order == 'y':
                continue
            else:
                run = False
    return order_items           
                

# Show Card
def show_cart(orders):
    print("You order the follwing Items: ")
    for i in range(len(orders)):
        print(str(i+1)+"- "+orders[i].title())
    print("-"*30+"\nYour Total Price: "+str(order_items.total_price)+"Tk")

## Start main function
print("#"*30+"\n    Welcome To Hacker Caffe\n"+"#"*30+ \
"\nPlease Chose your Order Number:")

# Declare Variables
menue = { 1:{"item":"coffe","price":350},
2:{"item":"burgers","price":250},
3:{"item":"meatloaf","price":220},
4:{"item":"lasagna","price":220}
}

orders = [] # issue it has to be a dictionary not a list
qty= 1

# Show menue
show_manue(menue)
print('#'*30)

# Add item 
order_items(orders)
print('#'*30)

# Show card list
show_cart(orders)

#End    
print('#'*30+"\nThanks! Order Again.\n") 
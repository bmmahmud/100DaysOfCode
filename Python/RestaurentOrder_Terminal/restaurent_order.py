print("#"*30+"\n    Welcome To Hacker Caffe\n"+"#"*30+ \
"\nPlease Chose your Order:")

# Declare Variables
menue = {"coffe":350,
"burgers":250,
"meatloaf":150,
"lasagna":220
}
total_price = 0
orders = []
qty= 1

# Show Menue Card
for item,price in menue.items():
    print(item.title()+" - Price: "+str(price)+"Tk") 
print('#'*30)

# Add items
x = True
while x:
    items = input("Enter Item Name:")
    print("Order More or Type: done")
    x = items
    if x == 'done':
        x = False
    else:  
        qty = int(input("Quantity:"))  
        total_price += (menue[items] * qty)
        orders.append(items)    
print('#'*30)

# Show Card

print("You order the follwing Items: ")
for i in range(len(orders)):
    print(str(i+1)+" - "+orders[i].title() +" - "+str(menue[orders[i]]))
print("Your Total Price: "+str(total_price))
#End    
print('#'*30+"\nThanks! Order Again.\n")         


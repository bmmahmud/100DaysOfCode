# Declare Variables
menue = { 1:{"item":"coffe","price":350},
2:{"item":"burgers","price":250},
3:{"item":"meatloaf","price":220},
4:{"item":"lasagna","price":220}
}

# print(menue[1]['item'])

for item,value in menue.items():
        print(item,": Item: ",value["item"].title(),"- Price:"+str(value["price"])) 
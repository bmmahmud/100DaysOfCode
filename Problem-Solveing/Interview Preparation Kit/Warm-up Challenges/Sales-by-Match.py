def sockMerchant(n, ar):
    pears = 0
    color = set() # set provide features: add and remove 
    print(range(len(ar)))
    print(color)
    for i in range(len(ar)):
        if ar[i] not in color:
            color.add(ar[i])
            print(f"color: {i} : {color}") 
        else:
            pears += 1 # increase pair number from 0
            print(f"pears: {pears}") 
            color.remove(ar[i]) # remove pair color
            print(f"color by remove: {i} : {color}")
    return pears

n,ar = 7, [1,2,3,2,3,2,1]
sockMerchant(n,ar)
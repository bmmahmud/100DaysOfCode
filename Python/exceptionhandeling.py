# Exception Hnadeling
inputs = input("Enter a Number: ")
try:
    num = int(inputs)
    if num/2 == 0 :
        print('Postive Number')
    else: 
        print ('Negative Number')
except:
    print('Warning !!!! Enter whole Number.')            
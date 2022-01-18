def itoa(x, base) :
  
    negative = False
    s = ""
    if (x == 0) :
        return "0"
    negative = (x < 0)
    if (negative) :
        x = -1 * x
    while (x != 0) :
      
        # add char to
        # front of s
        s = str(x % base) + s 
          
        # integer division 
        # gives quotient
        x = int(x / base) 
      
    if (negative) :
        s = "-" . s
  
    return s

def octal_in_range(n):
	# For loop traversing from 1 to N (Both Inclusive)
    print ("0 ", end = "")
    for i in range(1, n+1):
        a = itoa(i, 2)
        print(i,oct(i)[2:],'\t',hex(i)[2:],'\t',"{} ".format(a[0:]), end = "")
# Calling the function with input 3
print("Input:")
octal_in_range(11)
# # Calling the function with input 11
# print("Input: 11")
# octal_in_range(11)

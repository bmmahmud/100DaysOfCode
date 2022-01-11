def input_validation(value):
    while True:
        val = value
        try:
            val = int(val)
            return val
        except:
            print('Please use numeric digits.')
            continue
        if val < 1:
            print('Please enter a positive number.')
            continue
        break
value = input('Enter Item Name:')
x = input_validation(value)
print(f'Your age is {x}.')
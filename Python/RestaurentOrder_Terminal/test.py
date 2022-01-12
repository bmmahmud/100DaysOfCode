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
x = numeric_validation('Enter Item Name:')
print(f'Your age is {x}.')
def countingValleys(steps, path):
    # Write your code here
    count = 0
    result = 0
    for c in path:
        if c == 'U':
            count += 1
        else:
            count -= 1
        if count == 0 and c == 'U':
            result += 1
    return result
steps = 8
path = 'UDDDUDUU'
x = countingValleys(steps,path)
print(x)
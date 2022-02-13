a = 'this is a string'
a = a.split(" ")
print(a)
a = '-'.join(a)
print(a)


def split_and_join(line):
    # write your code here
    a = line.replace(" ", "-") #'-'.join(line)
    # print(a)
    return a
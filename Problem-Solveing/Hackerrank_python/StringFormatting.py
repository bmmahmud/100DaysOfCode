number = int(2)
length = len("{0:b}".format(number))
for i in range(1, number+1):
    print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=length))

# here,
# length, take the binary lenght to  determine the space between
# two rows. and we use this row sapce in {0:{w}d} here. w is the space.

### Solution for
# def print_formatted(number):
#     # your code goes here
#     length = len("{0:b}".format(number))
#     for i in range(1, number+1):
#         print("{0:{w}d} {0:{w}o} {0:{w}X} {0:{w}b}".format(i,w=length))
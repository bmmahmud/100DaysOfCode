# magicians = ['alice','david','caroline']
# for magician in magicians:
#     print(magician.title() +", that was a great trick!")

## Numeric Loop
# for value in range(1,5):
#     print(value)

# make list item
# numbers = list(range(1,6))
# print(numbers)

# numbers = list(range(2,21,2))
# print(numbers)

squares = []
# for value in range(1,11):
#     square = value**2
#     squares.append(square)
# print(squares)    

for value in range(1,11):
    squares.append(value**2)
print(squares)
# mins = min(squares)
# print(mins)
# maxs = max(squares)
# print(maxs)
# sums = sum(squares)
# print(sums)

## List comprehension
squares = [value**2 for value in range(1,11)]
print(squares)
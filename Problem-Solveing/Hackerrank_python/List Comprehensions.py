##### List Comprehensions
#Basic
# square = []
# for i in range(1,11):
#     square.append(i**2)
# print("Normal:",square)   

# # Now using List Comprehension
# ListCom = [i**2 for i in range(1,11)]
# print("Using LC:",ListCom)

############################# using Condition
movies = ["ashik","abir","lamia","afrin","sobuj","tanvir"]
gmovies = []
for title in movies:
    if title.startswith("a"):
        gmovies.append(title)
print("Nomal G:",gmovies)

# Using List Com  
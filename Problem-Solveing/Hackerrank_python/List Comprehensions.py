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
# movies = ["ashik","abir","lamia","afrin","sobuj","tanvir"]
# gmovies = []
# for title in movies:
#     if title.startswith("a"):
#         gmovies.append(title)
# print("Nomal G:",gmovies)

# # Using List Com 
# names =  [title for title in movies if title.startswith("a")]
# print("Condition LC:",names)

############## More Complex
# nameWithAge = [("ashik",25),("abir",19),("lamia",15),("afrin",16)]

# names = [ name for (name,age) in nameWithAge if age >18]
# print("Names: ",names)4
# HackerRank Solution
x = int(input())
y = int(input())
z = int(input())
n = int(input())
s = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k !=n]
print(s)

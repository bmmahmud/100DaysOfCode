# ACoder Contest - AtCoder Beginner Contest 236 | https://atcoder.jp/contests/abc236/tasks/abc236_a
# input main string
S = input()
a, b = input().split()
a = int(a)
b = int(b)
list = []
for i in S:
    list.append(i)  

def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
s = swapPositions(list,a-1,b-1)
listToStr = ''.join([str(elem) for elem in s])
print (listToStr)
  
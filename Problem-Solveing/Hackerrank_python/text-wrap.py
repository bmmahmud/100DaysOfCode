# 06-01-2022
#HackerRank - python - Text Wrap
import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width) #solution

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

#### Basics of textwrap

# string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# # print (textwrap.wrap(string,8))
# print(textwrap.fill(string,4))

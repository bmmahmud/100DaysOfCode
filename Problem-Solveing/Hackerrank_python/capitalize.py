#### B M ASHIK MAHMUD | 06-01-2022
### CAPITALIZE - HACKERRANK PYTHON STRING

# line = input()
# sline = line.split()
# Lline = []
# for cline in sline:
#     res = cline[0].upper() + cline[1:]
#     Lline.append(res)
# # print(res)
# # xline += ''.join(nline)
# # print(Lline)
# nline = ' '.join(Lline)
# print(nline)

s = "ashik mahmud"
for x in s[:].split():
    s = s.replace(x, x.capitalize())
        
        

# print(s)
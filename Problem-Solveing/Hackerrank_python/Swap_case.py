## Swap Case - HackerRank

s= 'Ab'
ln = []
for l in s:
    print(l)
    if l == l.lower():
        ln.append(l.upper())
        print('if:',ln)
    elif l == l.upper():
        ln.append(l.lower())
        print('elif:',ln)
    else:
        ln.append(l)
        print('else:',ln)
ln = ''.join(ln)  
print(ln) 
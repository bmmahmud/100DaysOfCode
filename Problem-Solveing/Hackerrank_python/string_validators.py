s = input()
print(any([i.isalnum() for i in s]))
print(any([i.isalpha() for i in s]))
print(any([i.isdigit() for i in s]))
print(any([i.islower() for i in s]))
print(any([i.isupper() for i in s]))

### Logic
# s = 'a2' 
# s.isdigit() = 'a' is False, '2' is True; [False, True]
# any([False, True]) -> return only True
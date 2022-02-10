#assignment chapter 10: File-> write: Guest

filename = "reasons.txt"


while True:
    name = input("Why you like coding: ")
    if name == 'done':
        break
    else:
        reason = ''
        # reason += name 
        with open(filename,'a') as file_object:
            file_object.write(name+".")
    for line in name:
        reason+= line.rstrip()            

print("List of guests:\n")
with open(filename) as file_object:
    lines = file_object.read()
    print(lines.strip())
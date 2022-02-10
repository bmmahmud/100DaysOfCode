#assignment chapter 10: File-> write: Guest

filename = "guest.txt"

name = input("Enter your name: ")
with open(filename,'a') as file_object:
    file_object.write(name+"\n")

print("List of guests:\n")
with open(filename) as file_object:
    lines = file_object.read()
    print(lines.strip())
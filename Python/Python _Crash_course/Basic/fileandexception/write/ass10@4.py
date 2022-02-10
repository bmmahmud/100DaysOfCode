#assignment chapter 10: File-> write: Guest

filename = "guest.txt"

done = 'True'
while done:
    name = input("Enter your name: ")
    print(f"Welcome {name}, You have been added to the guest list.")
    with open(filename,'a') as file_object:
        file_object.write(name+"\n")
    done = input("want to add more? y or enter: ")
    if done == "no":
        done =False    

print("List of guests:\n")
with open(filename) as file_object:
    lines = file_object.read()
    print(lines.strip())
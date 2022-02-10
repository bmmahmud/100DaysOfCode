# writing a message to a empty file
filename = 'programming.txt'
with open(filename,'w') as file_object:
    message = 'I love programming.'
    # file_object.write(message*3)
    file_object.write(message+"\n")
    file_object.write("I love creating new games.")

with open(filename) as file_object:
    lines = file_object.read()
    print(lines)
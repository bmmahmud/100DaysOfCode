# Assignment Chapter 10 - Files | Reading Files

filename = "text_files/learning_python.txt" # file select
with open(filename) as file_object:
    lines = file_object.readlines()
    # print(lines)
    # for line in file_object:
    #     print(line.rstrip())

long_string = ''
for line in lines:
    long_string += line.rstrip()        
print(long_string)  
new_string = long_string.replace('python','Golang')
print(new_string)
# read files 
# with open('text_files\pi_digits.txt') as file_object:
file_path = "text_files/pi_million_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''

for line in lines:
    pi_string += line.rstrip()

birthday = input('Enter your birthday, in the form mmddyy: ')

if birthday in pi_string:
    print("Your Birthday apperas in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")    
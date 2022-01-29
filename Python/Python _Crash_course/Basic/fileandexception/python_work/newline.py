# read files 
# with open('text_files\pi_digits.txt') as file_object:
file_path = "F:/100-days-of-code/100DaysOfCode/Python/Python _Crash_course/Basic/fileandexception/text_files/pi_digits.txt"
with open(file_path) as file_object:
    lines = file_object.readlines()
pi_string = ''

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))
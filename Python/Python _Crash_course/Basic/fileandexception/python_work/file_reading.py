# read files 
# with open('text_files\pi_digits.txt') as file_object:
file_path = "F:/100-days-of-code/100DaysOfCode/Python/Python _Crash_course/Basic/fileandexception/text_files/pi_digits.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents.rstrip())
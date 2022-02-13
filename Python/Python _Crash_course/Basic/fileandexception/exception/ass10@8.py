# Assignment 10 - 8
def animalNames(filenames):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
            print(contents.rstrip().title())
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg) 
        pass # ass10@9
    else:
        words = contents.split()
        num_words = len(words)
        print("The file "+ filename+" has " + str(num_words) + " words.")



## FilesDescription
filenames = ['cat.txt','animal.txt', 'dog.txt']
for filename in filenames:
    animalNames(filename)
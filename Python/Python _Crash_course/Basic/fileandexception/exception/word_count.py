def count_word(filename):
    """"Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exist."
        # print(msg)
        pass
    else:
        # Count the approximate number of words in the file.
        words = contents.split()
        num_words = len(words)
        print("The file "+ filename+" has " + str(num_words) + " words.")

############### main
# ## Single File 
# filename = 'alice.txt'
# count_word(filename)        
############## Multiple files #####
filenames = ['alice.txt', 'siddhartha.txt', 'moby_dicks.txt', 'little_women.txt']
for filename in filenames:
    count_word(filename)
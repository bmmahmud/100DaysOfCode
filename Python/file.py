try:
    # f = open("text.txt", encoding='utf-8')
    with open("text.txt",'w',encoding='utf-8') as f:
        f.write("my first file \n")
        f.write("This file \n\n")
        f.write("contains three lines\n")
finally:
    f.close()   
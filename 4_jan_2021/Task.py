from collections import *

def counter(file):

    num_spaces = 0

    file = open("text.txt", "r")

    char = file.read()




    # For count number of spaces

    for i in char:
        if i.isspace():
            num_spaces += 1
        if not i:
            break





    # for line count
    line_count  = char.count(".")





    # for average words

    list = char.split()

    average = sum(len(word) for word in list) / len(list)






    # for count Common Words

    b = char.replace(" ", "")

    dic = Counter(b)

    top = dic.most_common(1)







    print(f'First task:- Count Number of spaces in text file: {num_spaces}')

    print(f"Second task:- Count lines in text file is {line_count}")

    print(f"Third task:- Most average letter in text file is {average}")

    print(f"Forth task:- Most common letter in text file is {top}")



file = 'text.txt'

try:
    counter(file)
except:
    print('File not found')

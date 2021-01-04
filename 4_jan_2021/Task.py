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



        # # loop to iterate file
        # # line by line
        # for line in f:
        #
        #     # incrementing value of
        #     # num_lines with each
        #     # iteration of loop to
        #     # store total line count
        #     num_lines += 1
        #
        #     # declaring a variable word
        #     # and assigning its value as Y
        #     # because every file is
        #     # supposed to start with
        #     # a word or a character
        #     word = 'Y'
        #
        #     # loop to iterate every
        #     # line letter by letter
        #     for letter in line:
        #
        #         # condition to check
        #         # that the encountered character
        #         # is not white space and a word
        #         if (letter != ' ' and word == 'Y'):
        #
        #             # incrementing the word
        #             # count by 1
        #             num_words += 1
        #
        #             # assigning value N to
        #             # variable word because until
        #             # space will not encounter
        #             # a word can not be completed
        #             word = 'N'
        #
        #         # condition to check
        #         # that the encountered character
        #         # is a white space
        #         elif (letter == ' '):
        #
        #             # incrementing the space
        #             # count by 1
        #             num_spaces += 1
        #
        #             # assigning value Y to
        #             # variable word because after
        #             # white space a word
        #             # is supposed to occur
        #             word = 'Y'
        #
        #         # loop to iterate every
        #         # letter character by
        #         # character
        #         for i in letter:
        #
        #             # condition to check
        #             # that the encountered character
        #             # is not  white space and not
        #             # a newline character
        #             if (i != " " and i != "\n"):
        #                 # incrementing character
        #                 # count by 1
        #                 num_charc += 1

    # printing total word count
#     print("Number of words in text file: ", num_words)
#
#     # printing total line count
#     print("Number of lines in text file: ", num_lines)
#
#     # printing total character count
#     print('Number of characters in text file: ', num_charc)
#
#     # printing total space count
#     print('Number of spaces in text file: ', num_spaces)
#
#
# # Driver Code:
# if __name__ == '__main__':
#     fname = 'File1.txt'
#     try:
#         counter(fname)
#     except:
#         print('File not found')
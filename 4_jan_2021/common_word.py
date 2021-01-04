from collections import *

file = open("text.txt", "r")

a = file.read()
b = a.replace(" ", "")

dic = Counter(b)

top = dic.most_common(1)

print(f"most common letter in text file is {top}")

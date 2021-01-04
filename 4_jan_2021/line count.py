file = open("text.txt", "r")

Count = 0

a = file.read()
List = a.split("\n")

for i in List:
    Count += 1

print(f"This is the number of lines in the file {Count}")
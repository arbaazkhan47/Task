file = open("text.txt", "r")

a = file.read()

list = a.split()

average = sum(len(word) for word in list) / len(list)

print(average)

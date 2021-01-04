file = open("text.txt", "r")

count = 0
while True:

    char = file.read(1)

    if char.isspace():
        count += 1
    if not char:
        break
print(f"This is the number of space in the file {count}")
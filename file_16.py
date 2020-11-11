# Python code to move text file data into list
# using split() function

with open("file.txt", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
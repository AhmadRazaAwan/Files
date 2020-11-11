# take input from user and store in filea

name = input("Enter your name : ")
age = input("Enter your age  : ")

# making new file and store data into it
with open("New.txt", mode="a") as f:
    f.write(name)
    f.write(age)
# take input from user and store in filea

print("1) for giving information")
print("2) for view information")
option = int(input("Choose one option"))

if option==1:
    name = input("Enter your name : ")
    age = input("Enter your age  : ")

    with open("New.txt", mode="w") as f:
        f.write("Name = {}".format(name))
        f.write("\nAge = {}".format(age))
elif option == 2:

    with open("New.txt", mode="r") as f:
        print(f.read())
# We can read a file line-by-line using readline() method.

with open("info.txt", mode="r") as f:
    print(f.readline())     # read line until find \n
    print(f.readline())

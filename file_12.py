# We can read a file line-by-line using a for loop.

with open("info.txt", mode="r") as f:
    for line in f:
        # by using end result is in order
        print(line, end="")

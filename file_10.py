# Read file in python with using read mode
# Read from specific points
# Read till end
with open("info.txt", mode="r") as f:
    print(f.read(2))    # Read first 2 data
    print(f.read(5))    # Read next 5 data
    print(f.read(4))    # Read next 4 data
    print(f.read())     # Read next till end

with open("text.txt", mode="r") as f1:
    # they don't showing result because this file is empty
    print(f1.read())
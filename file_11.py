# Read file in python with using read mode
# Read from specific points
# Read till end
# tell is used to check that cursor position
# Seek is used to move your cursor position

with open("info.txt", mode="r") as f:
    print(f.read(2))    # Read first 2 data
    print(f.read(5))    # Read next 5 data
    print(f.read(4))    # Read next 4 data
    print(f.read())     # Read next till end
    print(f.tell())     # Tell used check the cursor position
    print(f.seek(11))   # Move cursor position to 10 data number
    print(f.read())     # Read from 10 data to till end
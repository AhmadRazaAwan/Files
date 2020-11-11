# The try block will raise an error when trying to write to a read-only file:
# The program can continue, without leaving the file object open

try:
    f = open("info.txt")
    f.write("Hello")
except:
    print("Something went wrong")
finally:
    f.close()

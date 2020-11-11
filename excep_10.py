# We can also use only try and final if we don't want to handle error

try:
    f = open("info.txt")
    f.write("Hello")
finally:
    f.close()
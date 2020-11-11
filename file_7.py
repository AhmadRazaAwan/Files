# Previous method is not entirely safe.
# If an exception occurs when we are performing some operation with the file,
# the code exits without closing the file.
# A safer way is to use a try...finally block.

try:
    # f = open("text.txt")
    # simple opening a file
    f = open("text.txt", encoding="cp1258")
finally:
    f.close()
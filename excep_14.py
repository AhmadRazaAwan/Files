# Python program to handle simple runtime error

a = [1, 2, 3]
try:
    print("Second element = %d" % (a[1]))

    # Throws error because 3 index not in array
    print("Fourth element = %d" % (a[3]))

except IndexError:
    print("An error occurred")

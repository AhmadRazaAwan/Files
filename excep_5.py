# The finally block gets executed no matter if the try block raises any errors or not:

try:
    print(x)
except:
    print("X is not found")
finally:
    print("Sorry X value is 10")
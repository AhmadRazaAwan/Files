# Python program for finally

try:
    k = 5 // 0  # raises divide by zero exception.
    print(k)

# handles zerodivision exception
except ZeroDivisionError:
    print("Can't divide by zero")

finally:
    # finally will always executed
    print('This is always executed')
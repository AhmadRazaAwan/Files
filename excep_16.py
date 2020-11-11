# Program to depict else clause with try-except

# Function which returns a/b


def equation_solve(a, b):
    try:
        c = ((a + b) / (a - b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    # Driver program to test above function


equation_solve(2.0, 3.0)
equation_solve(3.0, 3.0)
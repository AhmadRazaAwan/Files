# program to print the reciprocal of even numbers using assert with try,except method


print("Program to print the reciprocal of even numbers")
try:
    num = int(input("Enter number : "))
    assert num % 2 == 0
except:
    print("Its not a even number")
else:
    reciprocal = 1 / num
    print("Reciprocal of {} is : {}".format(num,reciprocal))
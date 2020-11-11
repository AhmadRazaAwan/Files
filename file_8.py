# The best way to close a file is by using the with statement.
# it will also open a file bus you dont need to close it after using
# they will automatically (explicitly ) call the close method.

with open("test.txt", encoding = 'cp1252') as f:
# Removing Directory or File
# Two method
# remove method delete/remove the directory or a file
# Where as
# rmdir() method can only remove the empty directory

import os

print(os.listdir())

# Its give Error Because this file is not Empty
os.rmdir("Allah")

# they will remove even they have files
# os.remove("Allah")
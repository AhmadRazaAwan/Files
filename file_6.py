# Closing Files in Python
# using .close built-in method to close file

f = open("text.txt", encoding="cp1252")

# After performing operations on your file
# You should need to close file which you opened
f.close()
# Opening a file with (with statement)
# write some sentence in file

with open("info.txt", mode="w", encoding="cp1252") as f:
    f.write("My Name is Ahmad Raza\n")
    f.write("I'm From Pakistan")

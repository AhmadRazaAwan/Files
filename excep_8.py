# As a Python developer you can choose to throw an typeError if a condition occurs.

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are showing")
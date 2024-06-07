# reduce = apply a function to an iterable and reduce it to a single cumulative value.
#           performs function on first two elements and repeats process until 1 value remains

# reduce(function, iterable)

import functools

letters = ["H", "E", "L", "L", "O"]

# function that takes 2 arguments
word = functools.reduce(lambda x, y: x + y, letters)


# ["H", "E", "L", "L", "O"] reduced to "HELLO"

print(word)  
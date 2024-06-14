# lambda functions = functions written in 1 line using lambda keyword
#                    accepts any number of arguments, but only has one expression
#                    (think of it as a shortcut)
#                    (useful if needed for a short period of time, throw-away)

# syntax = lambda parameters: expression

# (1) Without lambda #

def double(x):
    """
    Doubles the given number.
    
    Parameters:
    x (int): The number to be doubled.
    
    Returns:
    int: The doubled number.
    """
    return x * 2

print(double)

# (2) With lambda #

double = lambda x: x * 2
multiply = lambda x, y: x * y
add = lambda x, y, z: x + y + z

print(double(5))
print(multiply(5, 7))
print(add(6, 7, 8))

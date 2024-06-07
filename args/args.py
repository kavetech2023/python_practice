"""pass arguments as tuple into function parameters"""

def args(*args):
    for i in args:
        print(i)

args(1,2,3,4,5)        
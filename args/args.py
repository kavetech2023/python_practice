"""pass arguments as tuple into function parameters"""
# the function
def args(*args):
    for i in args:
        print(i)

# call the function
args(1,2,3,4,5)        

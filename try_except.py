"""exception = events detected during execution that interrupt
               the flow of a program"""
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator
    print(result)                
except ZeroDivisionError: # Handles Exceptions of divisions by zero
    print("You can't divide by zero :(  ")    
except ValueError: # Handles Exceptions of divisions between numbers and non-numbers
    print("You can only enter numbers :( ")    
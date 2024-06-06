"""exception = events detected during execution that interrupt
               the flow of a program"""
try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator/denominator                
except ZeroDivisionError as e:# Handles Exceptions of divisions by zero
    print(e) 
    print("You can't divide by zero :(  ")    
except ValueError as e: # Handles Exceptions of divisions between numbers and non-numbers
    print(e) 
    print("You can only enter numbers :( ")    
except Exception as e: #Handles all exception
    print(e)
    print("Something went wrong : ( ")    
else:
    print(result)    
finally:
    print("This will always excecute")    
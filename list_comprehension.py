# list comprehension = a way to create a new list with less syntax
#                      can mimic map(), filter() and lambda functions
#                      lists created using list comprehension are enclosed in []

# syntax = [expression for item in iterable if condition == True]

students = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]

# passed_students = list(filter(lambda x: x >= 60, students))

# passed_students = [i for i in students if i >= 60]

passed_students = [i if i >= 60 else "Failed" for i in students]

print(passed_students)  # [100, 90, 80, 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed']

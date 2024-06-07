# list comprehension = a way to create a new list with less syntax
#                      can mimic map(), filter() and lambda functions
#                      lists created using list comprehension are enclosed in []

# syntax = [expression for item in iterable if condition == True]

# (1) Without list comprehension

store = [("shirt", 20.00),
            ("pants", 25.00),
            ("jackets", 50.00),
            ("socks", 10.00)      
    ]           
store_euros = []    
for i in store:
    store_euros.append((i[0], i[1]*0.82))


for i in store_euros:
    print(i)       

# (2) With list comprehension

store_euros = [(i[0], i[1]*0.82) for i in store]

for i in store_euros:
    print(i)

# (3) Using map() and lambda
    
store_euros = list(map(lambda data: (data[0], data[1]*0.82), store))

for i in store_euros:
    print(i)

# (4) Using filter() and lambda

friends = [("Rachel", 25),
                ("Monica", 27),
                ("Phoebe", 29),
                ("Joey", 24),
                ("Chandler", 29),
                ("Ross", 30)
        ]

age = lambda data: data[1] >= 18
praying_buddies = list(filter(age, friends))

for i in praying_buddies:
    print(i)

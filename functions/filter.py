# filter() = creates a collection of elements 
#            from an iterable for which a function returns true

# filter(function, iterable)

friends = [("Rachel", 25),
              ("Monica", 27),
              ("Phoebe", 29),
              ("Joey", 24),
              ("Chandler", 29),
              ("Ross", 30)
    ]

# data[0]=  friend name
# data[1]=  friend age

age = lambda data: data[1] >= 18
praying_buddies = list(filter(age, friends))

for i in praying_buddies:
    print(i)
# map = applies a function to each item in an iterable (list, tuple, etc.)

#map(function, iterable)

store = [("shirt", 20.00),
         ("pants", 25.00),
         ("jackets", 50.00),
         ("socks", 10.00)      
]

# data[0]=  item name, data[1] = price

to_euros = lambda data: (data[0], data[1]*0.82)

# map(function, iterable)
store_euros = list(map(to_euros, store))

for i in store_euros:
    print(i)
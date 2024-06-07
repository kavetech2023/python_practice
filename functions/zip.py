# zip (*iterables) = aggregate elements from two or more iterables (lists, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ['Dude', 'Bro', 'Mister']
passwords = ['p@ssword', 'abc123', 'guest']

users = dict(zip(usernames, passwords))


# zip objects are iterable

for i in users:
    print(i)
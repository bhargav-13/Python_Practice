# filter() =    creates a collection of elements from an iterable, for which a function returns true
#
#               filter(function, iterable)

buddies = [("rachel", 20),
           ("monica", 21),
           ("pheobe", 16),
           ("joey", 22),
           ("ross", 17),
           ("chandler", 23)]

age = lambda data: data[1] >=18

Drinking_Buddies = list(filter(age, buddies))

for i in Drinking_Buddies:
    print(i)

def tuple():
    tup=(12,12.5,True,'word',True,False,13,14,14)
    #index(item) returns the index of an item
    print(tup.index(14))
    print(tup.index(True))

    #count(item) returns the number of times an item occurs in a tuple
    print(tup.count(14))
    print(tup.count(True))
    print(tup.count('word'))

tuple()
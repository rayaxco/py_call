def tuple():
    tup=(12,12.5,True,'word',True,False,13,14,14)
    #index(item) returns the index of an item
    print(tup.index(14))
    print(tup.index(True))

    #count(item) returns the number of times an item occurs in a tuple
    print(tup.count(14))
    print(tup.count(True))
    print(tup.count('word'))

    print(12.5 in tup) #True id 12.5 is in the tuple
    a,b,c,*others,d=(1,2,3,4,5,6,7)
    print(a)
    print(b)
    print(c)
    print(others)
    print(d)


tuple()
def rev_list():
    def access(li):
        #print list
        print(li)

        #accessing values of a list
        for item in li:
            print(item)

        #accessing values by index
        for index in range(0,len(li),1):
            print(index,':',li[index],'\t',end="")
    def mixed(li):
        for item in li:
            print(item)
        for i in range(0,len(li)):
            print(i,' ', li[i])

    def mutable(li):
        for item in li:
            print(item)
            if item == True:
                item = False

    def datatype_of_mix(li):
        li.append('gracias') #adds a single element to the end of the list
        #li.prepend('hola') No such function as prepend in python
        li.insert(0,'hola')
        for i in li:
            print(type(i),':',i)

    def list_functions(li):
        li.extend([100,101,True]) #extend() adds multiple elements to the end of the list
        print(li)

        print(li.pop())  #popping the last element from the list li
        print(li)

        print(li.pop(4)) #popping the fifth element from the list
        print(li)

        li.remove(10.5) # value in the argument removed from the list
        print(li)
        #remove(value) takes a value as argument not an index , for that we use pop(index)

    lis=[2,4,5,6,2,5,8,3,1,5,46,48,79,75]
    #access(lis)
    mix=[1,10,10.5,'daniella',True]
    mixed(mix)
    mutable(mix)
    #different datatypes can be stored inside a list
    datatype_of_mix(mix)
    list_functions(mix)
rev_list()
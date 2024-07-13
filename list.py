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
                li.remove(True)
                print(li)

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

        print(li.index('daniella')) #returns the index of a value index(value)

        #index(item,start index,stop index) looks for item 'daniella' in a range of indexes
        print(li.index('daniella',3,6))
        print(li)

        print('daniella' in li) #is item 'daniella' in the list?

        print(li.count('daniella')) #counts the number of times item 'daniella' exists in the list

        lis = [2, 4, 5, 6, 2, 5, 8, 3, 1, 5, 46, 48, 79, 75]
        print(sorted(lis)) #sorted  doesnt sort the actual list , it just sorts and returns a list that is sorted, datatype similarity during sorting
        print(lis)


        lis2=lis.copy() #copies list lis value into lis2
        print(lis2)

        lis3=lis.reverse() #modifies the list in reverse order
        print(lis)

        lis4=lis[:] #copies the list lis to lis4
        print(lis4)

        print(li[::-1]) #only prints the list in reverse order
        print(li)

        lis5=range(0,100)#pushed values 0 to 99 into lis5
        for item in lis5:
            print(item)

        lis6='hello'.join(' 12')
        print(lis6)

    def list_unpacking():
        a,b,c,d,*others,e=[1,2,3,4,5,6,7,8,9]
        print(a)
        print(b)
        print(c)
        print(d)
        print(others)
        print(e)





    lis=[2,4,5,6,2,5,8,3,1,5,46,48,79,75]
    #access(lis)
    mix=[1,10,10.5,'daniella',True,'daniella',11,102]
    #mixed(mix)
    #mutable(mix)
    #different datatypes can be stored inside a list
    #datatype_of_mix(mix)
    #list_functions(mix)
    list_unpacking()
rev_list()
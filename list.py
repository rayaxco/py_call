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
        for i in li:
            print(type(i))

    lis=[2,4,5,6,2,5,8,3,1,5,46,48,79,75]
    #access(lis)
    mix=[1,10,10.5,'daniella',True]
    mixed(mix)
    mutable(mix)
    datatype_of_mix(mix)
rev_list()
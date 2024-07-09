def rev_list(li):
    #print list
    print(li)

    #accessing values of a list
    for item in li:
        print(item)

    #accessing values by index
    for index in range(0,len(li),1):
        print(index,':',li[index],'\t',end="")

lis=[2,4,5,6,2,5,8,3,1,5,46,48,75]
rev_list(lis)
#map ,filter, zip,reduce
from functools import reduce
def accumulate(acc,item):
    return acc+item

mylist=[1,2,3]
print(reduce(accumulate,mylist,10))

def multiply_by2(item):
    return item*2
print(list(map(multiply_by2,mylist)))

def only_odd(item):
    return item%2 != 0
my_list=[85,25,56,45,15,12,13,16,14,18,15,19]
print(list(filter(only_odd,my_list)))

mylis=[1,2,3,4]
yourlis=[5,6,7,8,9]
this_lis=list(zip(mylis,yourlis))
print(this_lis)
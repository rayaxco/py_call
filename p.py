# name='reviver'
# rev=name[::-1]
# if name==rev:
#     print(True)
#
# word='reviver'
# rev=word[::-1]
# print(word.find('ve'))
# mlist=[12,45,78,88,56,23,33]
# first,*x,last=mlist
# print(first)
# print(x)
# print(last)
# matrix=[[1,2,3],[4,5,6],[7,8,9]]
# for row in range(len(matrix)):
#     for column in range(len(matrix[0])):
#         print(matrix[row][column],'\t',end="")
#     print('\n')
#
# mxlist=[matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[0]))]
# print(mxlist)
#
# lisa=[i for i in 'cleetus']
# print(lisa)
# lisb=[i*2 for i in 'brutus']
# print(lisb)
# sum_range=sum([i for i in range(0,100)])
# print(sum_range)
# sums=[sum(pair) for pair in zip([1,2,3],[4,5,6])]
# print(sums)
# sorted_by_second= sorted(['hi','you','man'], key=lambda el:el[1])
# print(sorted_by_second)
#
# sort_by_key=sorted([
#     {'name':'Bina','age':30},
#     {'name':'Andy','age':18},
#     {'name':'Zoey','age':55}],
#     key=lambda n:(n['age']))
# print(sort_by_key)

# def add_1(x):
#     return x+1
# res=add_1(8)
# print(res)
add_1=lambda x:x+1
print(add_1(8))

add_xy=lambda x,y:x+y
print(add_xy(8,9))

# li=[1,2,5,7,10]
# def squared(x):
#     return x**2
# res=list(map(squared,li))
# print(res)

# res=list(map(lambda x:x**2,li))
# print(res)
# li=[1,3,4,7,8,12,11]
# res=list(filter(lambda x:x%2==0,li))
# print(res)
li=[(1,'b','hello'),(2,'a','world'),(3,'c','ok')]
sorted_val=sorted(li,key=lambda x:x[1]+x[2])
print(sorted_val)
from functools import reduce
#max
from random import randint
numbers=[]
for y in range(100):
    rand=randint(1,100000000)
    numbers.append(rand)
max=reduce(lambda acc,x:acc if acc>x else x,numbers)
print(max)
min=reduce(lambda acc,x:acc if acc<x else x,numbers)
print(min)
sum_num=reduce(lambda acc,x:acc+x,numbers)
print(sum_num)

fancy_comp={x:(lambda x:x*x)(x) for x in range(5)}
print(fancy_comp)
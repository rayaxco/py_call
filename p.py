# # name='reviver'
# # rev=name[::-1]
# # if name==rev:
# #     print(True)
# #
# # word='reviver'
# # rev=word[::-1]
# # print(word.find('ve'))
# # mlist=[12,45,78,88,56,23,33]
# # first,*x,last=mlist
# # print(first)
# # print(x)
# # print(last)
# # matrix=[[1,2,3],[4,5,6],[7,8,9]]
# # for row in range(len(matrix)):
# #     for column in range(len(matrix[0])):
# #         print(matrix[row][column],'\t',end="")
# #     print('\n')
# #
# # mxlist=[matrix[row][col] for row in range(len(matrix)) for col in range(len(matrix[0]))]
# # print(mxlist)
# #
# # lisa=[i for i in 'cleetus']
# # print(lisa)
# # lisb=[i*2 for i in 'brutus']
# # print(lisb)
# # sum_range=sum([i for i in range(0,100)])
# # print(sum_range)
# # sums=[sum(pair) for pair in zip([1,2,3],[4,5,6])]
# # print(sums)
# # sorted_by_second= sorted(['hi','you','man'], key=lambda el:el[1])
# # print(sorted_by_second)
# #
# # sort_by_key=sorted([
# #     {'name':'Bina','age':30},
# #     {'name':'Andy','age':18},
# #     {'name':'Zoey','age':55}],
# #     key=lambda n:n['name'])
# # print(sort_by_key)
# from numpy.core.defchararray import upper
#
# # def add_1(x):
# #     return x+1
# # res=add_1(8)
# # print(res)
# # add_1=lambda x:x+1
# # print(add_1(8))
# #
# # add_xy=lambda x,y:x+y
# # print(add_xy(8,9))
#
# # li=[1,2,5,7,10]
# # def squared(x):
# #     return x**2
# # res=list(map(squared,li))
# # print(res)
#
# # res=list(map(lambda x:x**2,li))
# # print(res)
# # li=[1,3,4,7,8,12,11]
# # res=list(filter(lambda x:x%2==0,li))
# # print(res)
# # li=[(1,'b','hello'),(2,'a','world'),(3,'c','ok')]
# # sorted_val=sorted(li,key=lambda x:x[1]+x[2])
# # print(sorted_val)
# # from functools import reduce
# # #max
# # from random import randint
# # numbers=[]
# # for y in range(100):
# #     rand=randint(1,100000000)
# #     numbers.append(rand)
# # max=reduce(lambda acc,x:acc if acc>x else x,numbers)
# # print(max)
# # min=reduce(lambda acc,x:acc if acc<x else x,numbers)
# # print(min)
# # sum_num=reduce(lambda acc,x:acc+x,numbers)
# # print(sum_num)
# #
# # fancy_comp={x:(lambda x:x*x)(x) for x in range(5)}
# # print(fancy_comp)
#
# #dictionary
# # my_dict={'name':'Andrei Neagoie','age':30,'magic_power':False}
# # print(my_dict['name'])
# # print(len(my_dict))
# # print(list(my_dict.keys()))
# # print(list(my_dict.values()))
# # print(list(my_dict.items()))
# # my_dict['favourite_snacks']='grapes'
# # print(my_dict)
# # print(my_dict.get('age'))
# # print(my_dict.get('age',0))
# # del my_dict['favourite_snacks']
# # print(my_dict)
# # my_dict.pop('magic_power',None)
# # print(my_dict)
# # my_dict.update({'cool':True})
# # print(my_dict)
# # # {**my_dict, **{'cool': True}}
# # # print(my_dict)
# # new_dict=dict([['name','Andrei'],['age','32'],['magic_power','False']])
# # print(new_dict)
# # new_dict=dict(zip(['is_walking','is_firing'],[True,False]))
# # print(new_dict)
# # new_dict.pop('is_firing')
# # print(new_dict)
# # new_dict=dict(zip(['name','age','Licensed'],['Kumar',22,True]))
# # print(new_dict)
# # comp_dict={key:val for key,val in my_dict.items() if key=='age' or key=='name'}
# # print(comp_dict)
# # z=[(2,3),(4,5),(6,7,),(8,9),(11,10)]
# # unzip=lambda z:list(zip(*z))
# # unz=unzip(z)
# # print(unz)
# #
# # my_tup=[(1,2,3,5,6),(6,7,8,9,10)]
# # i=0
# # for num in my_tup:
# #    i=i+1
# #    print(f'{i}--->{num}')
# # # msg=''
# # # while msg != 'QUIT':
# # #     msg=upper(input('enter a message to display'))
# # #     print(msg)
# # en=enumerate('hellooooo')
# # print(en)
# # for i,j in en:
# #     print(f'{i}---->{j}')
#
# # from collections import Counter
# # colors=['blue','blue','blue','violet','red','red','blue','violet']
# # print(Counter(colors))
# # print(Counter(colors).most_common()[0])
#
# # from collections import namedtuple
# # point=namedtuple('Point','x y')
# # p=point(1,2)
# # print(p.y)
# # Person=namedtuple('Person','name height')
# # per=Person('ravindra','5\'4')
# # print(per.name,':\t:',per.height)
# # print('{p.name} {p.height}'.format(p=per))
#
# # from collections import OrderedDict
# # programmers=OrderedDict()
# # programmers['lisa']=['c','c++','python']
# # programmers['jennifer']=['c++','java']
# # programmers['jia']=['java','javascript']
# # print(programmers)
# # for key,val in programmers.items():
# #     print(key,' ----> ',end='')
# #     for elem in val:
# #         print(elem,' ',end='')
# #     print('\n')
# # from random import randint
# # args=[3,5,6,4,2,1,8]
# # for i in range(10000000):
# #     args.append(randint(1,1000))
# #
# #
# #
# # kwargs={'a':3,'b':54}
# # def func(*args,**kwargs):
# #     print(sum(args))
# #     for key, value in kwargs.items():
# #         print(key,' : ',value)
# # func(*args,**kwargs)
# args=[1,2,3,4,5,6,7,8,9]
# # def func(x,*args,w,**v):
# #     print(args)
# #     print(x)
# #     print(v)
# #     print(w)
# #
# # func(*args,y=11,z=12)
# # a=[*[2,3,4],5,6,7,*[8,9]]
# # print(a)
# # sett={*{1,2,3,4},5,6,7,7,*{8,8,9}}
# # print(sett)
# # kwdict={**{'a':1,'b':2,'c':3},'d':4,'e':5,**{'f':6}}
# # print(kwdict)
# # head,*body,tail=[1,2,3,4,5,6,7,8,9]
# # print(head)
# # print(body)
# # print(tail)
# #lambda function to find a Factorial
# # from functools import reduce
# # # n=5
# # # li=[]
# # # for i in range(2,n+1):
# # #     li.append(i)
# # # print(li)
# # # acc=1
# # # res=reduce((lambda acc,x: acc*x),li)
# # # print(res)
#
# # nth fibonacci number using lambda
# # fibn=lambda n: n if n<=1 else fibn(n-2)+fibn(n-1)
# # res=fibn(50)
# # print(res)
# #dictionary using comprehension
# # di={i:i*2 for i in range(10) }
# # print(di)
#
# # out=[i+j for i in range(3) for j in range(3)]
# # print(out)
# # l=[a if a else 'zero' for a in [0,1,0,3]]
# # print(l)
# #
# # #map
# # mapped=list(map(lambda i:i+1 ,range(20)))
# # print(mapped)
# #filter
# # filtered=list(filter(lambda i:i%5==0,range(25)))
# # print(filtered)
# #
# # a=[True,False,True]
# # print(any(a))
# # a=[True,0,True]
# # print(all(a))
# # def get_multiplier(a):
# #     def out(b):
# #         return a*b
# #     return out
# # mul_by3=get_multiplier(3)
# # print(mul_by3(10))
#
# # def func():
# #     while True:
# #         try:
# #             x=int(input('Enter a number'))
# #         except ValueError as val:
# #             print(val)
# #         else:
# #             print(x)
# #             print('carry on')
# #             break
# # func()
#
# # x='adsadasd'
# # if not(type(x) is int): #evaluates to True if 'type(x) is int' is False
# #     raise Exception('meesa want integer only')
# #
# # val=61
# # try:
# #     if val>60:
# #         raise ZeroDivisionError
# #
# # except Exception as ex:
# #     print(ex)
# #     print('oops')
# # finally:
# #  print('All done!')
# # import random
# # with open('C:/Users/ravyp/Desktop/text1.txt',mode='w+') as fl:
# #     for i in range(10):
# #         text='i am supposed to be line : '+str(i)+'\n'
# #         fl.writelines(text)
#
# # with open('C:/Users/ravyp/Desktop/text1.txt',mode='wt') as fl:
#     # # for i in range(10):
#     # #     text='this is line : '+str(i)+'\n'
#     # #     fl.write(text)
#     # x=fl.readline()
#     # print(x)
#     # print(fl.readline())
#     # print(fl.readline())
#     # fl.write('this is mario')
#     # fl.write('this is commander sheperd')
#     # print(fl.read())
# def fileread(filename):
#     with open(filename,encoding='utf-8') as fl:
#         return fl.readlines()
# dir='c:/users/ravyp/Desktop/text1.txt'
# print(fileread(dir))
#
# def filewrite(filename,content):
#     with open(filename,mode='w',encoding='utf-8') as fl:
#         return fl.writelines(content)
# dir='c:/users/ravyp/Desktop/text1.txt'
# content=['this is line: '+str(i)+'\n' for i in range(10)]
# print(filewrite(dir,content))
#
# def fileappend(filename,content):
#     with open(filename,mode='a') as fl:
#         fl.writelines(content)
# dir='c:/users/ravyp/Desktop/text1.txt'
# content=['this is line no : '+str(i)+'\n' for i in range(10,21)]
# fileappend(dir,content)
import p
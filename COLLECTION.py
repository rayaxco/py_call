from collections import Counter, defaultdict, OrderedDict

# li=[1,2,3,4,5,6,7,7]
# sen='jimmy timmy simmy kimmy jenny'
# print(Counter(li))
# print(Counter(sen))

# dictionary=defaultdict(lambda:5,{'a':1,'b':2})
# print(dictionary['c'])
dict=OrderedDict()
dict['b']=2
dict['a']=1

dict2=OrderedDict()
dict2['a']=1
dict2['b']=2

print(dict==dict2)
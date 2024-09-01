from time import time
# def my_generator(number):
#     for i in range(number):
#         yield i
#
# val=my_generator(1000)
# for i in range(100):
#     print(next(val))

# def generator_function(numb):
#     for i in range(numb):
#         yield i #yield pauses the function until next call

# for item in generator_function(1000):
#     print(item)
# g=generator_function(100)
# print(next(g),next(g),next(g))

# def performance_decorator(fn):
#     def wrapper(num):
#         t1=time()
#         fn(num)
#         t2=time()
#         print(f'took {(t2-t1)} sec ',fn)
#     return wrapper
# @performance_decorator
# def list1(num):
#     for i in list(range(num)):
#         i*2
# @performance_decorator
# def gen1(num):
#
#     for i in range(num): #range alone is a generator
#         i*2
#
#
# list1(10000000)
# gen1(10000000)
#

# def special_for(iterable):
#     iterator=iter(iterable)
#     print(next(iterator))
#
# special_for([1,2,3])

# def special_for(iterable):
#     iterator=iter(iterable)
#     while True:
#         try:
#             print(iterator)
#             print(next(iterator))
#         except StopIteration:
#             break
# special_for([1,2,3])
class MyGen():

    def __init__(self,first,last):
        self.first=first
        self.last=last
        self.current=first
    def __iter__(self):
        return self
    def __next__(self):
        if self.current<self.last:
            num=self.current
            self.current+=1
            return num
        raise StopIteration
gen=MyGen(0,100)
for i in gen:
    print(i)
print(gen.first)
print(gen.last)
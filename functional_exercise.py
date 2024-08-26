from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']
def capi(item):
    return item.capitalize()
print(list(map(capi,my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(my_numbers)

print(list(zip(my_strings,my_numbers)))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
def over_fifty(item):
    return item>50
print(list(filter(over_fifty,scores)))
for i in my_numbers:
    scores.append(i)
print(scores)
#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def accumulate_total(acc,item):
    print(acc,item)
    return acc+item

print(reduce(accumulate_total,scores,0))

#using lambda expressions

pets = ['sisi', 'bibi', 'titi', 'carla']
print(list(map(lambda item: item.capitalize(),pets)))

scores = [73, 20, 65, 19, 76, 100, 88]
print(list(filter(lambda item: item>50,scores)))
print(scores)
print(reduce(lambda acc,item:acc+item,scores,0))

my_list=[5,4,3]
print(list(map(lambda item:item**2,my_list)))

#comprehensions list
my_chars=[char for char in 'string']
print(my_chars)

my_chars2=[val for val in range(0,100) if val%2==0]
print(my_chars2)

#comprehensions sets
my_array=[10,12,15,21,12,10,15,15,15,12,13,13,14,14]
my_set={val for val in my_array}
print(my_set)

my_set={val for val in my_array if val<15}
print(my_set)

#comprehensions dictionary
arr=[1,2,3]
my_dict={key:key**2 for key in arr }
print(my_dict)

simple_dict={
    'a':1,
    'b':2,
    'c':3
}

my_dict={key:val**2 for key,val in simple_dict.items() if (val**2)%2==0}
print(my_dict)

#which of the elements of the array have duplicates

arr=['a','b','b','a','c','d','e','c','d','d','c',]

duplicates={item for item in arr if arr.count(item)>1}
print(duplicates)
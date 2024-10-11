import re
#without using RegExp library
string='this is a string search in it, search always. string is a chain of characters'
print('search' in string)

#Using RE package
print(re.search('this',string))
#<re.Match object; span=(0, 4), match='this'>

#create a pattern of our own using re package
pattern=re.compile('search')
a=pattern.search(string)
print(a)
#<re.Match object; span=(17, 23), match='search'>

print(a.span())
#(17, 23)

print(a.start())
#17

print(a.end())
#23

print(a.group())
#if search() is not found then a=None

#if match at the beginning (pattern2*)
pattern2=re.compile('this')
b=pattern2.match(string)
print(b)
#<re.Match object; span=(0, 4), match='this'>

#if pattern=string
pattern3=re.compile('this is a string search in it, search again')
c=pattern3.fullmatch(string)
print(c)
#<re.Match object; span=(0, 43), match='this is a string search in it, search again'>

#find all instances of pattern
pattern4=re.compile('string')
d=pattern4.findall(string)
print(d)
#['string', 'string']

pattern5=re.compile(r'(^[A-Za-z0-9+_.-]+@[a-zA-Z+_-]+\.[a-zA-z]+.[a-zA-Z]+$)')
string5='ravy.pmr9465@gmail.com.au'
gr=pattern5.search(string5)
print(gr)
print(gr.group())
print(pattern5.match(string5))
print(pattern5.findall(string5))
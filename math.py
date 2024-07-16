def maths():
    print(type(5/8)) #datatype of result of 5/8
    print(8%3) # % returns remainder of 8/3
    print(8**34) # ** is to the power of
    print(round(7/8)) # rounds the value of 7/8 to the nearest integer
    print(abs(-2000058789)) #outputs the absolute value of the argument
    print(bin(5)) #bin() converts the argument to binary form
    print(int('0b101',2)) #int('binaryform', base) converts binary to integer

    #augmented assignment operators
    a=10
    a+=10 #a=a+10
    print(a)
    a-=10 #a=a-10
    print(a)
    a*=8 #a=a*8
    print(a)
    a/=10 #a=a/10
    print(int(a))
    a%=5 #a=a%5
    print(a)
    a**=2
    print(a)
    print(not(5)) #returns false because 5 is considered a truthy value

    #logical operators
    #   >   ,  <   ,  >=  ,  <=  ,  ==  ,   !=  ,   and ,   or  ,   not

maths()
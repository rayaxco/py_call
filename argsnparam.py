def fx(m,n): #positional parameters
    print(m+n)
fx(5,4) #positional arguments

fx(n=4,m=5) #keyword argument; specifies value for each parameter

def defaultfx(m=10,n=20): #default parameters defined
    print(m+n)
defaultfx(11,21) #calling with arguments
defaultfx() #calling without arguments

def tuplefx(*args):

    for i in range(0,len(args),1):
        #args is just a name ; we can use any name in the parameter to refer to the tuple
        print(args[i]) #each value in the tuple is accessed from the variable args
tuplefx(1,2,3,4,5,6,'argument') #unspecific amounts of arguments are passed as a tuple using '*' *args

def dictfx(**kwargs):
    print(len(kwargs))
    for key,value in kwargs.items():# we can treat kwargs as a dictionaryof keys and values
        print(key,':',value)
    print('orange' in kwargs.keys())
dictfx(mango=15,strawberry=22,orange=9)

#standard order of passing argument to parameters
#def function_name(positional_parameters,*args,default_parameters,**kwargs)
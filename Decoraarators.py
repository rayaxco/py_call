#decorators
def hello():
    print('helloooo')
#fuunctions can also be  treated as variables
#its memory index can be sstoredd  inside a variable by calling it without paranthesis

greet=hello()
del hello
#hello() deleted but before that, its index was stored in greet
print(greet)

#a fuunction can be a parameter and also an argument

def hello(func):
    func()

def greet():
    print('still here')
hello(greet)

def my_decorator(func):
    def wrap_func():
        print('*******')
        func()
        print('*******')
    return wrap_func
@my_decorator #references to my decorator function and passes thee below function as parameter to the decorator function
def hi():
    print('helloooo')
hi()

#exercise


# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    # code here
    def wrapper(user):
        if(user['valid']):
            fn(user)
    return wrapper

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)
def strings():
    def string_functions():
        stri='bonjour!'
        print(type(stri))  #get the datatype of a variable; in this case string or 'str'

        stri2=" comment ca va"
        stri3=" mon ami"

        stri=stri+stri2+stri3 #use '+' to concatenate strings
        print(stri)

        num=10423
        print(type(num)) #num is integer type
        num=str(num) #convert num to string datatype
        print(type(num))# now shows num as string datatype

        multiline_string='''this 
        is
        a 
        multi
        line
        string                    
        ''' #'''multiline string''' to have a multiline string
        print(multiline_string)

        #it can also be used for multiline comments
        '''
        this 
        is 
        a 
        multi
        line 
        comment
        '''

        #escape sequence
        name='peter'
        age=35
        print('hi '+name+' you\'re: '+str(age)+' years old!!' ) #use \' to an apostophe in a sentence

        #formatting strings
        intro= 'hi '+name+' you are '+str(age)+' years old'
        print(intro) #only datatype str can be output with strings

        intro2='hi {} ! you are {} years old..'.format(name,age)
        print(intro2)

        #or we can format during print
        print(f'hi {name} you\'re {age} years old..have fun')

        #or we can initialize inside  format()
        print('{name} {age}'.format(name='walter',age=56))  # walter 56

        greet=('bonjour')
        print(greet)
        print(greet[::-1]) # returns a reversed a string
        print(greet[0:len(greet):1]) #print characters in index 0 to len(greet) stepover 1
        print(greet[0:4]) #[0] to [3]
        print(greet[::2]) #[0] to last stepover 2
        print(greet[1::2]) #[1] to last stepover 2
        print(greet[:5]) #print till string index 5
        print(greet[-1:-4:-1]) #index -1=r to -4 stepover -1

        #immutability of string
        stri='bonjour'
        # stri[1]='j' #INVALID CODE

        #we can concatenate using  +
        stri=stri+' senora'
        print(stri)

        #BUILT-IN String functions
        stri='heisenberg'
        print(len(stri)) #returns the length of a string
        print(stri.upper()) #converts string contents to uppercase
        print(stri.capitalize()) #capitalizes first character in the string
        print(stri.lower()) #convert to lowercase characters
        print(stri.find('berg'))
        stri=stri.replace('berg','stein')
        print(stri)
        #type conversion
        name=input('Enter your name')
        birth_year=input('Enter your birth year')
        age=2024-int(birth_year)
        print(f'hi {name}!! You are {age} years old') #if you format a string then no need to match the datatypes
    string_functions()
strings()
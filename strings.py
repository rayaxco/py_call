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
        print('hi '+name+' you\'re: '+str(age)+' years old!!' )
    string_functions()
strings()
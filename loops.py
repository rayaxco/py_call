def forloops():
    #this function loops over strings
    def loop_string(st):
        for item in st:
            print(item+'\t',end="")
        print("") #new line at the end of the loop
    #this function loops over a list of numbers and adds them one by one
    def loop_list(li):
        sum=0
        for item in li:
            sum+=item
        print(sum)
    #this function loops over a list in a range of specific index and prints their sum
    def loops_partially(li):
        sum =0
        for item in range(0,5,1):
            sum+=li[item]
        print(sum)

    #this function loops over a tuple
    def loopstuple(tu):
        for i in tu:
            print(i,'\t',end="")
        print("")

    #this function loops over a dictionary
    def loop_dict(dic):
        for key,value in dic.items():
            print(key,'\t',value)

        #only keys
        for key in dic.keys():
            print(key,'\t')

        # only keys
        for values in dic.values():
            print(values, '\t')

    def loop_set(st):
        for i in st:
            print(i,' ',end="")

    loop_string('this is a sentence')
    loop_list([1,2,3,4,5,6,7,8,9,10])
    loops_partially([1,2,3,4,5,6,7,8,9,10])
    loopstuple((1,2,1,4,5,6,56,25))
    dicti = {
        'name': 'peter',
        'partner': 'olivia',
        'father': 'walter',
    }
    loop_dict(dicti)
    loop_set({8,5,2,1,4,6,3,7,9})

#forloops()

def whileloops():
    def while_cond_true(a):

        i=0
        while i != len(a): #expression i!=len(a) is true
            print(a[i])
            i=i+1

    while_cond_true([2,14,15,1,13,11,6,8,9,8,7,2,3,6,4,1])
whileloops()
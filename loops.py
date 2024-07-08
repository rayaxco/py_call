def loops():
    #this function loops over strings
    def loop_string(st):
        for item in st:
            print(item+'\t',end="")

    loop_string('this is a sentence')
loops()
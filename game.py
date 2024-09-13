from random import randint
import sys
first=int(sys.argv[1])
last=int(sys.argv[2])
gen=randint(first,last)
while True:
    try:
        guess=int(input('Enter a guess'))
        if first<guess<last:
            if gen == guess:
                print('you\'re right')
                break
    except ValueError:
        print('cut it out')
        continue
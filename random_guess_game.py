import random

answer=random.randint(1,10)
while True:
    try:
        print(answer)
        guess=int(input('please enter a number between 1-10---> '))
        if 0<guess<11:
            if guess==answer:
                print('correct')
                break
        else:
            print('I said a Number between 1--10')
    except ValueError as valerr:
        print('please enter a valid number')
        continue




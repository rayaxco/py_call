while True:
    try:
        age=int(input('Enter your age: '))
        10/age
    except ValueError:
        print('Enter a valid age')
    except ZeroDivisionError:
        print('Enter a number higher than Zero')

    else:
        print('Thank You!')
        break

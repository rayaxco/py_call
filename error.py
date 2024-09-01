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
    finally:
        print('ok i\'m finally done')
# def sum(num1,num2):
#     try:
#         return num1+num2
#     except (TypeError,ValueError) as err:
#         print(err)
#
# print(sum(1,'2'))
def do_stuff(num):
    try:
        if num:
            return int(num) + 5
        elif num is 0:
            return 'please enter a natural number'
        else:
            return 'please enter a number'
    except ValueError as err:
        return err
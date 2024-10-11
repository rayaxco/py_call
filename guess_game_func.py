def guess_game(guess,answer):
    try:

        if 0<guess<11:
            if guess==answer:
                return 'correct'
        else:
            return 'Nope'
    except ValueError as valerr:
        return valerr

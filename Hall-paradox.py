def proof(iterations,door_amount=3):
    '''
    iterations - how many times try to proof this,
    door_amount - how many doors.
    Function returs two numbers:
        First - number of wins without changing the door,
        Secomn - number of wins with door change.
    '''
    from random import randint
    win1 = 0
    win2 = 0
    for i in range(iterations):## x > 0:
        a = randint(1,door_amount)
        b = randint(1,door_amount)
        c = randint(1,door_amount)
        while c == b:
            c = randint(1,door_amount)
        if a == b:
            win1 +=1
        if a == b or a == c:
            win2 +=1
    print(
        'Without cange: ',
        (win1/iterations)*100,
        '%\nWith change: ',
        (win2/iterations)*100,'%'
        )
    return win1,win2


import random

how_many_times = input('How many times do you want to flip the coin?')
how_many_times_int = int(how_many_times)

while how_many_times_int != 0:
    toss = random.randint(1, 2)

    if toss == 1:
        coin = 'head'
    else:
        coin = 'tails'

    print(coin)
    how_many_times_int -= 1

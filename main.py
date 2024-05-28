import random

head = 0
tails = 0

how_many_flips = input('How many times do you want to flip the coin?')
how_many_flips_int = int(how_many_flips)

while how_many_flips_int != 0:
    toss = random.randint(1, 2)

    if toss == 1:
        coin = 'head'
        head += 1
    else:
        coin = 'tails'
        tails += 1

    print(coin)
    how_many_flips_int -= 1

print(f'There was {head} heads')
print(f'There was {tails} tails')

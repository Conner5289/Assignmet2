import random


class coin_flip:
    def flip():
        head = 0
        tail = 0

        how_many_flips = input('How many times do you want to flip the coin?')
        how_many_flips_int = int(how_many_flips)

        while how_many_flips_int != 0:
            toss = random.randint(1, 2)

            if toss == 1:
                # coin = 'head'
                head += 1
            else:
                # coin = 'tails'
                tail += 1

            # print(coin)
            how_many_flips_int -= 1
        total = head + tail

        return [head, tail, total]

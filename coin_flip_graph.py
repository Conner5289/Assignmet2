from main import coin_flip
import matplotlib.pyplot as plt

keep_playing = True


while keep_playing:
    result = coin_flip.flip()  # [heads, tails, total]

    coin_result = [result[0], result[1]]
    total = result[2]

    fsig, ax = plt.subplots()

    faces = ['heads', 'tails']

    ax.bar(faces, coin_result)
    ax.set_ylabel('Number of flips')
    ax.set_title('Coin toss ')

    print(f'There is a total of {
          coin_result[0]} heads and a total of {coin_result[1]} tails')  # python nvim formatter keeps breaking the line

    plt.show()

    yes_no = input('Do you want to keep playing? Y/N ')
    yes_no_upcase = yes_no.upper()
    print(f'{yes_no_upcase}')

    if yes_no_upcase == 'Y':
        keep_playing = True
    else:
        keep_playing = False
        print("Goodbye")

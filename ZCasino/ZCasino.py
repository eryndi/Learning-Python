from random import randrange
from math import ceil


def valid_num(num):
    try:
        return int(num)
    except ValueError:
        print(num, "is not a whole number. Try again.")
        return False

def valid_bet(bet):

    try:
        bet = valid_num(bet)
    except ValueError:
        return False

    if bet < 0 or bet > 49:
        bet = input("Must be number between 0 and 49. Please, insert a valid bet:")
    return bet


def roulette_logic(bet, sum):

    roulette = randrange(50)
    roulette_is_even = (roulette % 2) == 0

    print("Roulette is", roulette,  end=' ')
    if roulette_is_even:
        print("black")
    else:
        print("red")
    print("You have won", end=' ')

    bet_is_even = (bet % 2) == 0
    if bet == roulette:
        return sum * 3
    if bet_is_even == roulette_is_even:
        return ceil(sum / 2)
    else:
        return 0


if __name__ == '__main__':

    print("Hello this is roulette")
    while (True):
        try:
            bet = valid_bet(input("What is your bet? Choose a whole number between 0 and 49"))
        except ValueError:
            continue


        sum = valid_num(input("How much would you like to bet?"))

    # bet = valid_bet(bet)
    # sum = valid_num(sum)
    print("You are betting on", bet, "with total amount of", sum, "$")
    result = roulette_logic(int(bet), float(sum))
    print(result, "$")

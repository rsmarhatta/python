import random
guess = ''
def convert_guess(guess):
    if guess.lower() == 'heads':
        return 1
    elif guess.lower() == 'tails':
        return 0
    else:
        return guess
while guess not in ('heads', 'tails'):
    guess = input('Guess the coin toss! Enter heads or tails:')
    guess= convert_guess(guess)

    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    print(f"Random toss is: {toss}, guess is {guess}")
    if toss == guess:
        print('You got it!')
        break
    else:
        guesss = input('Nope! Guess again!' )
        guesss_c = convert_guess(guesss)
        print(f"Random toss is: {toss}, guess is {guesss_c}")
        if toss == guesss_c:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')
        guess = guesss
        break
import random

#generate random number between 1 - 10
random_num = random.randint(1,10)

while True:
    #get a number guess from player
    guess = int(input('Pick a number between 1 and 10...'))
    if random_num == guess:
        print('You guessed correctly!')
        break
    else:
        print('Try again...')

#compare guess to secret number
#print hit or miss

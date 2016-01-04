import random



#while True:
    #get a number guess from player
    #guess = int(input('Pick a number between 1 and 10...'))
    #print hit or miss
    #compare guess with random number
    #if random_num == guess:
        #print('You guessed correctly!')
        #break
    #else:
       #print('Try again...')

def game_loop():
    #generate random number between 1 - 10
    random_num = random.randint(1,10)
    
    #limit the number of guesses
    guesses = []
    while len(guesses) < 3 :
        try:
            guess = int(input('Guess a number between 1 and 10!')
                        
        #catch when someone submits a non integer
        except ValueError:
            print('{} is NOT a number!',format(guess))
        if random_num == guess:
            print('You guessed correctly! My number was {}'.format(random_num))
            game_loop()
        #print "too low" or "too high" msgs for bad guesses
        elif guess < random_num:
            print('Too low, try again...')
            game_loop()
        elif guess > random_num:
            print('Too high, try again...')
            game_loop()
        else:
            print('Good try!')
        guesses.append(guess)

game_loop()
#let ppl play again
        

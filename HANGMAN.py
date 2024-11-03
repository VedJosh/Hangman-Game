from HANGMAN_ELEMENTS import logo, word_list,stages, game_over
import random
import time

print(logo)

def hangman():
    # choosing random word
    word = random.choice(word_list)
    # copying the word
    word_copy = list(word)
    # creating empty string with _ (underscores)
    empty_word = ['_' for _ in range(len(word))]
    # initializing the number of lives
    life = 6
    # taking guess from user as long as user has lives to guess the letter and not guessed all the letters
    while '_' in empty_word:
        if life>0:
            print(f'{life} left!')
            print(stages[life])
            print('Word to guess: ',' '.join(empty_word))
            guess = input('Guess a letter: ')
            if guess in word:
                if guess in word_copy:
                    empty_word[word_copy.index(guess)]=guess
                    word_copy[word_copy.index(guess)]=''
                else:
                    print(f'You already guessed {guess}')
            else:
                life-=1
                print(f"You guessed {guess}, that's not in the word. \
    You lose a life.")

        else:
            if life<=0:
                print(f'You Lose!! The word was {word}') 
                print(stages[life])
                break
    else:
        print(f'You Won!! The word was {word}')
            
wanna_play = True

while wanna_play:
    hangman()
    choice = input('Do you want to play the game again(yes/no): ').lower()
    wanna_play = choice == 'yes'
else:
    print(game_over)
    time.sleep(5)

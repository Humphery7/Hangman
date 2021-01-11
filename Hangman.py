import random

print('Welcome to Hangman Game')
lst = random.choice(['Engineering','chord','technology','Tesla','Mars', 'whatsuplagos','SpaceX'])
msc = '_______________' # msc provides space for missing letters

hint = print(lst[0], msc[0:(len(lst)-2)], lst[-1])
turns = 0

# you have only 6 chances
for i in range(6):
    guess = input("guess the word : ")
    # lst is not a list since it selects only one from list
    if guess == lst:
         print(guess)
         print("You Guessed Right, You Win")
         exit()
    else:
        turns += 1
        if turns == 1:
            print('---------')
        elif turns == 2:
            print('---------')
            print('    O    ')
        elif turns == 3:
            print('---------')
            print('    O    ')
            print(' /  |  \ ')
            print('    |    ')
        elif turns == 4:
            print('---------')
            print('    O    ')
            print(' /  |  \ ')
            print('    |    ')
            print('   / \   ')
        elif turns == 5:
            print('---------')
            print('    |    ')
            print('    O    ')
            print(' /  |  \ ')
            print('    |    ')
            print('   / \   ')
        elif turns == 6:
            print('---------')
            print('    |    ')
            print('    O____')
            print(' /  |  \ ')
            print('    |    ')
            print('   / \   ')
            print("you let him die, you loose")
            exit(0)



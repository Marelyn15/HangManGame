#Step 2

import random
word_list = ["apple", "baboon", "camel"]
chosen_word = random.choice(word_list)


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#The blank spaces will be saved in all_words
all_words = []
#For each space in the word 
for i in chosen_word:
    all_words.append('_')

#How many life You have
number_times = len(chosen_word)


while number_times > 0:

    print(f'Number of time left {number_times}')
    guess = input("Guess a letter: ").lower()

    #TODO-2: - Loop through each position in the chosen_word;
    #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for index, letter in enumerate(chosen_word):
    #for letter in chosen_word:
        if letter == guess:
            all_words[index] = letter
        else:
            continue

    #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

    #Result
    print(all_words)
    #If you dont finished the whole word you lose a life
    if '_' in all_words:
        number_times -= 1
    else:
        break
    

if '_' in all_words:
    print('You lose')
else:
    print('You won')

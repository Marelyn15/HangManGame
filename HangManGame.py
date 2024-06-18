import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["apple", "orange", "camel","excel"]
chosen_word = random.choice(word_list)


#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#The blank spaces will be saved in all_words and new_all_words for validation
all_words = [] 
new_all_words = [] 
#For each space in the word 
for i in chosen_word:
    all_words.append('_')
    new_all_words.append('_')


#How many life You have
number_times = len(chosen_word)

while number_times > 0:

    print(f'Number of time left {number_times}')
    guess = input("Guess a letter: ").lower()

    for index, letter in enumerate(chosen_word):
    #for letter in chosen_word:
        if letter == guess:
            all_words[index] = letter
        else:
            continue
    
   
    #Result
    print(all_words)
    print(new_all_words)

    #If both list are the same
    if new_all_words == all_words:
        #You gonna lose a life
        number_times -= 1
        #And the new list gonna keep without change
        new_all_words = new_all_words
        #print(new_all_words)
        print(stages[number_times])

    #If both lists are not the same then
    else:
        #You gonna update the new list
        new_all_words = all_words.copy()
        #print(new_all_words)
    
    #If you dont have a blank space in the first list then
    if '_' not in all_words:
        break

    

#If you lose all you life then
if '_' in all_words:
    print('You lose')
#if you break the algorithm
else:
    print('You won')

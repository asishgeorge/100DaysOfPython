#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

print("Welcome to Hangman! \n")

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


# choose a random word from the list
random_word = random.choice(word_list)

# get the length of the random word
length_of_word = len(random_word)

# set a counter for winning and losing
failure = 0
counter = 0

user_guess = []
# set the user guess for display
for x in range(length_of_word):
  user_guess.append("_")

# how long should the game go on.
end_of_game = False

# take input as the game is on
while not end_of_game:
  
  #take input for the guess
  guess = input("Guess a Letter: ").lower()

  life_lost = True
  for x in range(length_of_word):
    if random_word[x] == guess:       
    # check if letter in word
      if user_guess[x] == '_':
        counter+= 1
        user_guess[x] = guess
        life_lost = False
        
  
  # life lost 
  if life_lost == True:
    failure+=1
    print(f"{stages[-failure]}")
  

  # print guesses so far
  print(f"{user_guess}")
  
  # end of game
  if counter == length_of_word or failure == len(stages):
    end_of_game = True
  

# win or lose
if counter == length_of_word:
  print("You Won!")
else:
  print("You Lost!")
    

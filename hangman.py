# %%
# I have my own more interactive version, made using the skills gained from tasks done throughout the project. 
# This is the one trying my best to follow the TODOs as strictly as possible. 
# In my version (found in milestones.py file and in documentation file), I print many more statements that inform the user how many lives there are how many unique letters remain.

'''
Make sure you complete all the TODOs in this file.
The prints have to contain the same text as indicated, don't add any more prints,
or you will get 0 for this assignment.
'''

import random
import re

from pyparsing import null_debug_action

class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.
    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried
    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''

    def __init__(self, word_list, num_lives=5):
        # TODO 2: Initialize the attributes as indicated in the docstring
        # TODO 2: Print two message upon initialization:
        # 1. "The mistery word has {num_letters} characters"
        # 2. {word_guessed}

        self.num_lives  = num_lives 
        self.word_list = word_list
        self.word = random.choice(word_list)
        self.correct_guesses= []
        self.word_guessed = []
        self.num_letters = None
        self.num_lives = num_lives
        self.list_letters= []
        
        self.word_guess_list()
        self.num_unique_letter()

        print("The mistery word has {} characters".format(self.num_letters))
        print(self.word_guessed) 
             
        pass

    def word_guess_list(self):
        length = len(self.word)
        word_guess_list = []
        word_split =[]
        i = 0
        while i < length:
            word_guess_list.append("_")
            word_split.append(self.word[i])
            i +=1     
        self.word_guessed = word_guess_list
        self.word_split= word_split

        return self.word_guessed

    def num_unique_letter(self):
        x = len(self.word_split)
        correct_guess = len(self.correct_guesses)    
        j = 0
        k = 0

        while j < x:

            for jj in range(j+1,x):
                
                if self.word_split[j] == self.word_split[jj]:
                    k+=1 
            j+=1

        num_letters=  x-k -correct_guess
        self.num_letters = num_letters

    def check_letter(self, letter) -> None:
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.
        Parameters:
        ----------
        letter: str
            The letter to be checked
        '''
        x = True
        word = self.word.lower()
        self.list_letters.append(letter)

        while x==True:

            # Task 3: Define what happens if the letter is in the word.
            if  letter in word:
                
                self.new_list()
                self.num_letters -= 1
                self.correct_guesses.append(letter)
                x= False
                
            # Task 4: Define what happens if the letter is.     
            else:
                self.num_lives -=1
                x = False

        # TODO 3: Check if the letter is in the word. TIP: You can use the lower() method to convert the letter to lowercase
        # TODO 3: If the letter is in the word, replace the '_' in the word_guessed list with the letter
        # TODO 3: If the letter is in the word, the number of UNIQUE letters in the word that have not been guessed yet has to be reduced by 1
        # TODO 3: If the letter is not in the word, reduce the number of lives by 1
        # Be careful! A letter can contain the same letter more than once. TIP: Take a look at the index() method in the string class
        pass

    def new_list(self):
        i = 0
        while i < len(self.list_letters):
           
            ii =0 
            while ii < len(self.word_split):
                if self.word_split[ii] == self.list_letters[i]:
                    self.word_guessed[ii] = self.list_letters[i]
                    
                else:
                    pass
                
                ii +=1
            i +=1

        self.word_guessed = self.word_guessed
        print(self.word_guessed)



    def ask_letter(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        x= True
        while x == True:
            letter = input("Guess a letter in the word. Use lowercase only..thank you")
            if letter == letter.capitalize():
                print("Invalid letter. Please, enter a lowercase character.")
            
            elif re.search("!@??$%^&*()",letter) != None: 
                print("invalid letter. Please, enter a single alphabetical character.") 

            elif letter in self.list_letters:
                print("{} was already tried".format(letter))

            elif len(letter) != 1:
                print("Please, enter just one character.")

            else:
                self.check_letter(letter)
                x = False


        # TODO 1: Ask the user for a letter iteratively until the user enters a valid letter
        # TODO 1: Assign the letter to a variable called `letter`
        # TODO 1: The letter has to comply with the following criteria: It has to be a single character. If it is not, print "Please, enter just one character"
        # TODO 2. It has to be a letter that has not been tried yet. Use the list_letters attribute to check this. If it has been tried, print "{letter} was already tried".
        # TODO 3: If the letter is valid, call the check_letter method
        pass


def play_game(word_list):
    # As an aid, part of the code is already provided:
    game = Hangman(word_list, num_lives=5)
    
    # TODO 1: To test this task, you can call the ask_letter method
    # TODO 2: To test this task, upon initialization, two messages should be printed 
    # TODO 3: To test this task, you call the ask_letter method and check if the letter is in the word
    
    # TODO 4: Iteratively ask the user for a letter until the user guesses the word or runs out of lives
    # If the user guesses the word, print "Congratulations! You won!"
    # If the user runs out of lives, print "You lost! The word was {word}"

    p = True
    while p == True:

        if game.num_letters > 0 and game.num_lives > 0: 
            game.ask_letter()

        elif game.num_lives == 0:
            print("You lost! The word was {}".format(game.word))
            p = False

        elif game.num_lives > 0 and game.num_letters == 0:
            print("Congratulations! You won!")
            p = False

        else:
            break


    pass

if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)


# Code seems to run well. Prints the expected messages for each scenario. 
A repository containing descriptions of AiCore tasks, skills required to tackle them and codes that complete them. 


# AiCore Hangman Project Documentation

> Hangman Game Project. 

## Milestone 1: Set up the environment

- Q: What have you built? 
- A: Set up Github Repository. New directories.

- Q: What technologies have you used? 
- A: VS Code, MiniConda and Git. Command line - using terminal commands to manipulate files and directories. 

- Q: Why have you used those?
- A: VS Code works as the text editor. MiniConda is a useful virtual environment generating software. Git is a version control system that allows  everyone to track changes, revert back to a previous (usually 'working' version), contribute towards a final product (main/master branch).

## Milestone 2: Create the variables for the game

- Q: What have you developed within the environment?
- A: Writing scripts that can create, manipulate numbers, strings, lists, overall assinging/storing them to variables which can be called and/or printed.

- Q: What utilities have you learnt this time?
- A: I learnt to install pacakges in base and virtual environments for use. Importing modules that have useful functions embedded inside them.

```Python
"""
# %%

# List of Fruits

word_list = ["apple","lychee", "mangosteen", "clementine","grape"]

# %%
print(word_list)

# %%

# BMI checker

def BMI_check(height, weight):

    bmi= (weight/height**2)
    if bmi <18.5:
        print("Your BMI is {}. You're In the underweight range.".format(bmi))
    elif bmi >= 18.5 and bmi <= 24.9: 
        print("Your BMI is {}. You're In the healthy weight range.".format(bmi))
    elif bmi >=25 and bmi <= 29.9: 
        print("Your BMI is {}. You're In the overweight range.".format(bmi))
    elif bmi >= 30 and bmi <= 39.9: 
        print("Your BMI is {}. You're In the obese range.".format(bmi))

# %%

#Testing variations

BMI_check(1.83, 85)
BMI_check(1.55, 61)
BMI_check(2.09, 135)

# %%

# Flight Safety Checker

def check_safety(altitude,airspeed):
    if altitude < 100 or altitude > 50000:
        print("This atlitude is unsafe")
    elif airspeed < 60 or airspeed > 500: 
        print("This atlitude is unsafe")
    else: 
        print("This atlitude is safe!")

# %%

#Testing variations

check_safety(25000, 300)
check_safety(50001, 250)
check_safety(90, 125)

# %%

# Order of conditions
# Original order was:

##  x = int(input('Enter a number: '))
##  if x > 0: 
##      print('x is greater than 0')
##  elif x > 15:
##      print('x is greater than 15')
##  elif x > 20:
##      print('x is greater than 20')
##  else:
##      print('x is less than 0')

# the above will print the first conditional that is met, therefore, if x = 16, it would print only x is greater than 15.

#Corrected version below.
x = int(input('Enter a number: '))

if x > 20: 
    print('x is greater than 20')
elif x > 15:
    print('x is greater than 15')
elif x > 0:
    print('x is greater than 0')
else:
    print('x is less than 0')

# %%

# Unique Elements in the List

my_list = ["a","f","e","d","c","b","z","h"]
x = len(my_list)
i = 0
a = 0

while i < x:
    
    for ii in range(i+1,x):
        
        if my_list[i] == my_list[ii]:
            a+=1
    i+=1

if a > 0:
    print("There are duplicates in this list")
else: 
    print("No duplicates")     
        
for i in range(x):
    if my_list[i] in (my_list-list(my_list[i])):
        print("There are duplicates in this list")
    else: 
        print("No duplicates")     
        
#I know this is somewhat very inefficient but it works.

# %%

# Rock, Paper, Scissors

list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
if list_1 == list_2:
    print('The lists are the same.')
else:
    print('The lists are different.')

# %% 

# Chose to do the rock paper scissors this way. Inefficient but it works.

def rps(player1, player2):
    if player1 == "rock":
        if player2 == "rock":
            print ("It's a tie!")
        elif player2 == "scissors":
            print("Player 1 wins!")
        elif player2 == "paper":
            print("Player 2 wins!")
        else:
            print("Invalid input")
    elif player1 == "scissors":
        if player2 == "rock":
            print ("Player 2 wins!")
        elif player2 == "scissors":
            print("It's a tie!")
        elif player2 == "paper":
            print("Player 1 wins")
        else:
            print("Invalid input")
    elif player1 == "paper":
        if player2 == "rock":
            print ("Player 1 wins!")
        elif player2 == "scissors":
            print("Player 2 wins!")
        elif player2 == "paper":
            print("It's a tie!")
        else:
            print("Invalid input")
    else:
        print("invalid input")

rps("scissors", "scissors")

# %%

#Example lines to import class/functions from modules.

import pandas as pd
from pandas import DataFrame

# %%

#AiCore Task 2 - Choose a random word from the list.

#Step 1 +2 

import random

#Step 3 

x = random.choice(word_list)

print(x)

# %%

#Task 3 - Ask the user for an input

guess = input("Enter a single letter!")
print(guess)

# %%

#Task 4 - Check that the input is a single character

guess = input("Enter a single letter!")

if len(guess) ==1 and type(guess) == str:
    print("Good guess!")
else:
    print("That is not a a valid input")
    
# %%

#Task 5 - Start documenting your experience....

#Uploaded milestones and descriptions onto GitHub.

```

## Milestone 3: Check if the guessed character is in the word

- Q: What utilities have you learnt this time?
- A: In this milestone, I have learnt to write several functions by defining them first, then calling them with or without arguments. I have developed if statements that check for certain types and range of input, thus filtering unwanted input values.

- Q: What did I struggle with?
- A: Recursive functions was a challenge to get my head around it. It still is rather difficult to understand. At the moment, I am using trial and error to find the script that works but I imagine I will eventually understand it well.

```Python
"""
# %% 

# MILESTONE 3 #

# Task 1: Iteratively check if the input is a valid guess

x = True
while x == True:
    guess = input("Guess a letter in the word.")
    if len(guess) == 1:
        x = False
        print(guess)
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        
# %%

# Task 2: Check whether the guess is in the word
import random

word_selection = ["Shenanigans","Bamboozle", "Bodacious", "Brouhaha", "Canoodle", "Gnarly", "Goggle", "Gubbins", "Malarkey", "Nincompoop" ]

word_of_the_run = random.choice(word_selection).lower()

# print(word_of_the_run)

# Guess a letter in the randomly selected word.

x= True
while x== True:
    guess = input("Guess a letter in the word. Use lowercase only..thank you")
    if len(guess) == 1 and guess in word_of_the_run:
        x = False
        print("Good guess '{}' is in the word.".format(guess))
    elif len(guess) != 1:
        print("Invalid letter. Please, enter a single alphabetical character.")
    else:
        print("Sorry, '{}' is not in the word. Try again".format(guess))
       

# %%

#Pre-requisite tasks

# Void Functions

def void_function():
    print("This is a void function")

void_result = void_function()

# The above line by itself, prints the message because it calls the function - and thus prints the message.

print(void_result)

# However, message printed is not assigned to a variable during the calling of the void_function function. Thus nothing is stored in void_result variable.

# %%

#Range Checker

def in_range(lower_bound, upper_bound, number):
    
    if int(number) >= int(lower_bound) and int(number) <= int(upper_bound):
        print( "{number} is between  {lower_bound} and {upper_bound}")
    elif int(number) < int(lower_bound) or int(number) > int(upper_bound):
        print( "{number} is NOT between  {lower_bound} and {upper_bound}") 
    else: 
        print("Likely an invalid input format. Please make sure arguments are numbers")
# Tests..

in_range(1,5,2)
in_range(3,5,2)
in_range(5,100,98)

# %%

# Volume of a Sphere   (V=4/3 π r^3)  radius in metres

def volume_of_sphere(radius):
    pi=3.14
    radius_cube = int(radius)**3
    volume = 4/3 * pi * radius_cube
    return volume

sphere = volume_of_sphere(8)
print(sphere)

#function could be one line - but it is less modifiable (e.g. if input units are not limited to metres)

def volume_of_sphere_short(radius):
    return 4/3 * 3.14 * radius**3

sphere2 = volume_of_sphere_short(8)
print(sphere2)

# %%

#Challenge for a function!

#Make a function that calculates how many portions of cheesecake (or any other food you like) you can make from the ingredient amounts you have.
# E.g. making a oreo cheesecake

def can_we_feed_5000(oreos_n,butter_g,cream_cheese_g,sugar_g,vanilla_extract_tsp,whipping_cream_cups):
    #ingredient list and numbers
    oreo=39
    butter=60
    cream_cheese= 453
    sugar = 1
    vanilla_extract= 1
    whipping_cream= 400
    
    o=  (oreos_n / oreo)
    b=  (butter_g / butter)
    cc= (cream_cheese_g / cream_cheese)
    s=  (sugar_g/ sugar)
    ve= (vanilla_extract_tsp / vanilla_extract)
    wc= (whipping_cream_cups/ whipping_cream)

    ratio = [o,b,cc,s,ve,wc]
    ratio.sort()
 
    print("You have enough of each ingredient to make {} oreo cheesecakes.".format(int(ratio[0])))
    
can_we_feed_5000(78,120,1000,10,20,5000)

#will 10000 of everything enough to make for 5000 portions? 

can_we_feed_5000(10000,10000,10000,10000,10000,10000)

#nope cream cheese and whipping cream needs a lot more...

can_we_feed_5000(1000000,1000000,1000000000,10000000,10000000,2000000)

# %%

# Default Arguments

printlist = {"test":1,"haha":2, "huhu":4}
list = ["test"]

def check_dict(list):
    attributes_to_print = printlist
    x=0
    while x < len(list):
        if list[x] in printlist.keys():
            print(list[x],"exists in the word")
            x +=1
        else:
            print("{list[x]} does not exist")
    
check_dict(list)
# %%

# Profile Validation

import re

# Regular Expressions

def name_check(name):
    if re.search("!@£$%^&*()",name) == None:
        return name
    else: 
        return "invalid format -please try again"
    
def age_check(age):
    if int(age) > 12:
        return age
    else: 
        print("You must be over 12.")

def email_check(email):
    if re.search( '\w@\w',email) != None:
        return email
    else: 
        print("invalid format -please try again")

def profile_check(name,age,email):
    profile = []
    profile.append(name_check(name))
    profile.append(age_check(age))
    profile.append(email_check(email))
    print(profile)
    
profile_check("DC",28,"dc.choi@kcl.ac.uk")

# %%

#Factorial Function

def factorial(number):
    if number ==0:
        return 1
    else:
        return number * factorial((number-1))

print(factorial(4))
# %%

# Recursive Fibonacci Function

# 0 1 1 2 3 5 8 13 21 ....

def fibonacci_seq(number):
    if number == 0:
        return 0
    elif number ==1:
        return 1
    else:
        return (fibonacci_seq(number-1) + fibonacci_seq(number-2))

x=35
list=[]
while x>=1:
    list.append(str(fibonacci_seq(x-1)))
    x -=1
    print(fibonacci_seq(x))
list.sort()
print(list)

# %%

# Inverse a string

word_list = ["hello", "hi"]
list= []
for words in word_list:
    for letter in words:
        
        list.append(letter)
list.reverse()
print(list)

# %%

#Palindrome Checker

palindromes = ['racecar','bob','neveroddoreven','poop']
non_palindromes = ['racecars', 'boba', 'evenstevens','diarrhea']

def check_if_palindrome(list):
    list =[]
    for word in list:
        x = len(word)
        if x % 2 == 0:
            for letter in word:
                list.append(letter)
                print(list)
                two = list.reverse()
                print(two)

# %%

list= []
word = "racecars"
for letter in word:
    list.append(letter)
    x= list
    y= list

# %%

#Task 3 - Create functions to run the checks   

def check_guess(guess,word):
    x = True
    word = word.lower()
    while x==True:
        if  guess in word:
            x = False
            print("Good guess '{}' is in the word.".format(guess))
        else:
            print("Sorry, '{}' is not in the word. Try again".format(guess))
            guess = input("Guess a letter in the word.")
            
def ask_for_input(word):
    x= True
    while x == True:
        guess = input("Guess a letter in the word. Use lowercase only..thank you")
        if guess == guess.capitalize():
            guess = input("Invalid letter. Please, enter a lowercase character.")
        elif len(guess) == 1:
            x = False
        elif len(guess) != 1:
            guess = input("Invalid letter. Please, enter a single alphabetical character.")
        else:
            break
    check_guess(guess,word)

# %% 

#Testing the ask_for_input function using a few example words.

word_1 = 'Hello'
word_2 = 'Tatratea'
word_3 = 'Hangman'
word_4 = 'AirPods'

ask_for_input(word_1)
ask_for_input(word_2)
ask_for_input(word_3)
ask_for_input(word_4)

# %%

# Task 4: Update your documentation

# Milestone 3 scripts cleaned and uploaded into GitHub repo (https://github.com/chedongchan/AiCore_Milestones/)
# Script file and Documentation updated, added, committed and pushed into github repo using the terminal.
```

## Milestone 4: Check if the guessed character is in the word

- Q: What utilities have you learnt this time?
- A: In this milestone, I have learnt to create a class and learn to define functions within the class. Classes can allow for unique functions that only work in instances where the class is called. 

- Q: What did I struggle with?
- A: To understand exactly how classes work. How one can manipulate the initialised values from subsequent functions. However, with some trial and errors, and thinking about the logic of classes, I believe I have at least understood enough to make the script run- though I believe there should be a cleaner way to do this... For example, I am not sure if I am supposed to consistently refer to self._insert variable__ throughout the class. I am also not entirely sure why some variables are underscored with red error lines in the code. 

``` Python

"""        
# %%

# Milestone 4: Create the Game Class

# Import modules required for this Class

# Task 1: Create the Class

import random
import re

# Task 1: Create the Class

class Hangman():

    # Initialise attributes in the first call of the instance. 
    # Set default number of lives to 5, unless specified via argument input.
    # Word_list argument taken in

    def __init__(self,word_list,num_lives=5):

        self.num_lives  = num_lives 
        self.word_list = word_list
        self.word = None
        self.word_guessed = None
        self.word_split = None
        self.list_of_guesses= []
    
    # Randomly select a word from the word_list. Requires random module import.
    # Assigns a random word from the word list to word variable.

    def random_word(self):
        self.word = random.choice(self.word_list).lower()
        return self.word

    # Creates a list of letters in the word assigned as word_split. 
    # Creates a duplicate list of word_split but letters substituted by underscores

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
    
    # A function to find the number of unique characters in the word. 
    # Used later to indicate to the user how many letters need to be correctly guessed to complete the word.

    def num_letters(self):
        
        x = len(self.word_split)
        j = 0
        k = 0

        while j < x:

            for jj in range(j+1,x):
                
                if self.word_split[j] == self.word_split[jj]:
                    k+=1 
            j+=1

        if k > 0:

            print("There are {} unique letters in this list".format(x-k))

        else: 
            print("No match! Try again. {} unique letters left".format(x))

        return        
    # Task 2: Create methods for running the checks
    # Asks user for input of a single character.
    # Checks for invalid formats. 
    # Calls the check_guess function if valid format is input.

    def ask_for_input(self):
        x= True
        while x == True:
            guess = input("Guess a letter in the word. Use lowercase only..thank you")
            if guess == guess.capitalize():
                print("Invalid letter. Please, enter a lowercase character.")
            
            elif re.search("!@£$%^&*()",guess) != None: 
                print("invalid letter. Please, enter a single alphabetical character.") 

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            elif len(guess) != 1:
                guess = print("Invalid letter. Please, enter a single alphabetical character.")

            else:
                
                self.check_guess(guess)

    # Checks the guessed letter against the word currently assinged.
    # Returns output messages depending on successful or unsuccessful guess.
    # Calls record function, which populates a string to indicate how many lives are left and a history of previous guesses.
           
    def check_guess(self,guess):
        x = True
        word = self.word.lower()
        self.list_of_guesses.append(guess)
        while x==True:

            # Task 3: Define what happens if the letter is in the word.
            if  guess in word:
                print("Good guess '{}' is in the word.".format(guess))
                self.new_list()
                x = False

            # Task 4: Define what happens if the letter is.     
            else:
                self.num_lives -=1
                print("Sorry, '{}' is not in the word. Try again".format(guess))    
                x = False
    
        print(self.word_guessed)
        self.record()
        
    # Prints a message to indicate to the user what guesses have been tried before, and how many lives are left.
                     
    def record(self):
        print("These are your guesses so far: {}".format(self.list_of_guesses), "You have {} guesses left.".format(self.num_lives))

    # Upon correct guess, the hidden letters that match the guessed letter will be revealed from the word

    def new_list(self):
        i = 0
        while i < len(self.list_of_guesses):
            ii =0 
            while ii < len(self.word_split):
                if self.word_split[ii] == self.list_of_guesses[i]:
                    self.word_guessed[ii] = self.list_of_guesses[i]
                else:
                    pass
                
                ii +=1
            i +=1

        return self.word_guessed

# Task 5: Update your documentation.

# %%
# Test the Hangman Class and Game
word_selection = ["Shenanigans","Bamboozle", "Bodacious", "Brouhaha", "Canoodle", "Gnarly", "Goggle", "Gubbins", "Malarkey", "Nincompoop" ]
x = Hangman(word_selection)
x.random_word()
x.word_guess_list()
x.num_letters()
x.ask_for_input()
print(x.list_of_guesses)
print(x.word_guessed)
print(x.word)
print(x.word_split)

```

## Milestone 5: Putting it all together.

- Q: What utilities have you learnt this time?
- A: In this milestone, I have learnt to simplify each function to do one task (if possible) and then place them under a single function that follows a overarching logic gate required for the Hangman game. 

- Q: What did I struggle with?
- A: There were many while loops within the code, which meant that when putting all the functions together, I got lost which loop was not being broken in order for the code to proceed to the next line. After some troubleshooting, such as setting the conditions False from the very beginning, I was able to narrow down the culprit to a single while loop. Turn out, my last while loop conditional IF statements were not in the right order. 

``` Python
"""
# %%

# Milestone 5: Putting it all together

# Task 1: Code the logic of the game

def play_game():
    word_list = ["apple","lychee", "mangosteen", "clementine","grape"]
    game = Hangman(word_list)
    game.random_word()
    game.word_guess_list()
    game.num_unique_letter()

    p = True
    while p == True:
        if game.num_letters > 0 and game.num_lives > 0: 
            game.ask_for_input()
            
            

        elif game.num_lives == 0:
            print("You lost!")
            p = False

        elif game.num_lives > 0 and game.num_letters == 0:
            print("You won the game!")
            p = False

        

        else:
            break
        
play_game()

# Task 2: Define play_game function.

# Logic: 
# 1. Set a variable called Word_list inside the function (in the future, this can be an argument for the function instead...)
# 2. Call an instance of Hangman using the word_list as the input argument. Number of lives are set to 5 as default.
# 3. Call the random_word() function to randomly select a word from word_list.
# 4. Call the word_guess_list() function, which generates two lists. The first one sequentially stores each letter per index of the list. The second is the 'hidden behind underscores' version of the same list.
# 5. Call the num_unique_letter() function, which generates a print statement based on how many remaining unique letters the player has to guess.
# 6. While loop that continues until the condition is set to False, contains conditional if statements that either keep the loop condition true or false:
#   a) Calls the ask_for_input() function if both number of unique letters and number of lives are greater than 0. 
#   b) If number of lives reach 0, set loop condition to be False, printing out "You lost!" message, and ending the game.
#   c) If number of lives is greater than 0 but no more unique letters exist (every letter guessed!), then set loop condition to be False, printing out "You won the game!" message, and ending the game.
# 7. Call the function outside. 



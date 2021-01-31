'''
JHUb Coding assessment - module 3 - Hangman Game
Trevor Bradley

Created 31 Jan 2021

Purpose of program is to get a list of words from a text file 
Randomly select one
Use file for a game of hangmans with 7 lives
No other user interaction
game is not case sensitive
'''
#use the random number package
import random

#varialbes needed with defaults as follows

#continue_playing
game_on = True

#number of lives instruction was for 7 lives
lives = 7

#this is the word that we will get from the file and will use to check guesses against
ans_word = ''

#The size of this will depend on the size of ans_word
disp_word=''
disp_word_list =[]

#This is the list of words that we will choose from it will be populated from the dictionary file
word_list=[]

#The length of the list.  we will use this in the random selection of a word.
list_length = 0

#this is the name of the dictionary file
file_name='word_list.txt'

#read in the dictionary file
#there could be an argument for putting the load and word selection elements into functions but we only do it once
#and don't call it from elsewhere
dict_handle=open(file_name,"r")

#iterate through the dictionary file and load each word into the word list
for each_word in dict_handle:
    word_list.append(each_word)
    list_length+=1

#close the file when the dictionary has been loaded
dict_handle.close()


#select a word at random subtract one from list length due to 0 indexing
rand_place=random.randint(0,list_length-1)
ans_word=word_list[rand_place]

#create a copy of the answer for the display of the mystery word.
#we need to do some type conversion for this due to limitations as to what we can do with strings
disp_word_list = list(ans_word)
#don't forget to strip off the cariage return from the end otherwise loops go wrong
disp_word_list.remove('\n')

#make a copy so we can check letters against it later.
ans_word_list = disp_word_list.copy()

#create a string of *s to represent the word
count_pos=0
for i in disp_word_list:
    disp_word_list[count_pos]="*"
    count_pos+=1

#converts the list back into a string
disp_word="".join(disp_word_list)

# keep on going until game is won or lost
# could put this in a function but not really worth it.  The code above would be the main function.
# this would be another one

while game_on:
    
    #nested loop to validate input - no error message just keep asking - again could be a function
    inp_req = True
    
    while inp_req:
        char_guess=input(disp_word+' Please enter your next guess: ')
        
        #check if it is a letter and change to lower case which makes comparison easier
        if char_guess.isalpha():
            char_guess=char_guess.lower()
            inp_req = False
    
    #now check char_guess against the selected word 
    #if not found take a life off
    #a touch inefficient computationally as we are essentially going through the word twice
    if char_guess in ans_word:
            
            #check each position in the answer and if present copy the letter to the display word
            pos_count = 0
            while pos_count < len(ans_word_list):
                
                if ans_word_list[pos_count] == char_guess:
                    disp_word_list[pos_count] = char_guess
                
                pos_count+=1
                            
            #now copy it to a string to display
            disp_word="".join(disp_word_list) 
    else:
        lives-=1
        
    #see if the game has been lost or won
    if lives == 0:
        game_on = False
        print('you lose')
    elif '*' not in disp_word:
        game_on = False
        print('congratulations you win')
    
#and that's it 
    
    



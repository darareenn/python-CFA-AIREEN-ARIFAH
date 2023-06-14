#!/usr/bin/env phython

import random
#library that we use in order to choose
#on random genres from list of genres

name = input("what is your name? ")

#Here the user is ask to enter the name

print("Break a leg! ", name)

genres = ['rock', 'hiphop', 'rap', 'jazz', 'opera', 'classic','indie']
#function will choose one random 
#genres from this list of genres
genre = random.choices(genres)


print("Guess the music genres")

guesses = ''

# any number of turns can be used here
turns = 6




while turns > 0:

    # counts the number of times a user fails 
    failed = 0

    # all genres from the input
    # genres taking one at a time.
    for str in genre:

        # comparing that genres with 
        # the genres in guesses
        if str in guesses:
            print(str, end = " ")

        else:
            print("_")

            # for every failure 1 will be
            # incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0
        # and 'War is over'  will be given as output
        print("")
        print ("You win!")

        # this print the correct genre
        print("The genre is: ", genre)
        break


    # if user has input the wrong genre then
    # it will ask user to enter another genre
    print()
    guess = input("guess a genre:")

    #every input genres will be stored in guesses
    guesses += guess

    #check input with the genres in genres
    if guess not in genre:

        turns -= 1

        #if the genres doesnt match the genres 
        #then "incorrect" will be given as output
        print("incorrect")

        #this will print the number of 
        #turn left for the user
        print("You have", + turns, 'more guesses')


        if turns == 0:
            print("Sorry you failed")
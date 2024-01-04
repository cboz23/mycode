#!/usr/bin/env python3


round = 0           # integer round initiated to 0
while True:        # sets up an infinite loop condition
    round = round + 1     # increase the round counter
    print('Answer the following question; "The Legend of Zelda\'s main character is named ______"')
    answer = input("Your guess--> ")    # string ans collected from user
    if answer == 'Link': # logic to check if user gave correct answer
        print('Correct!')
        break             # break statement escapes the while loop
    elif round == 3:    # logic to ensure round has not yet reached 3
        print('Sorry, the answer was Link.')
        break             # break statement escapes the while loop
    else:                 # if answer was wrong, and round is not yet equal to 3
        print('Sorry. Try again!')


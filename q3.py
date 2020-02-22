# File: q3.py
# Author: Brittany Vamvakias
# Date: 02/11/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code takes an input from the user and checks whether or not it contains two identicle consecutive letters and prints whether it does or not. This code continues to run until the user types "quit".

print("*************************************************************************")
run_loop = True

while run_loop == True:
    word = input("Enter a word: ")
    word = word.capitalize()

    if word != "Quit":
        for x in range(len(word) - 1):
            check_consec = word[x] == word[x + 1]

            if check_consec == True:
                print(f"{word}: identical consecutive letters")
                break
            elif x < len(word) - 2:
                continue
            elif x == len(word) - 2:
                print(f"{word}: no identical consecutive letters")
                break
    else:
        print("*************************************************************************")
        run_loop == False
        break



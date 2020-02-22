# File: q2.py
# Author: Brittany Vamvakias
# Date: 02/11/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code prompts the user to input the height for a triangle and two symbols to use for the triangle. The code then runs a while loop producing the correct amount of symbols in each row, starting from the base, alternating the symbols in each line, and lining them up to form a triangle. Once the row only has one symbol, an additional triangle is form from the peak to the base, using the previous triangles peak as the second triangles peak.

print("*************************************************************************")

height = int(input("Height of triangle: "))
first_sym = input("Enter first symbol: ")
second_sym = input("Enter second symbol: ")

num_sym = (height * 2) - 1  # this gives the number of symbols in a row
blank = " "
row_count = 0  # the current row you're in, starts at 0
num_blank = 0  # number of spaces on each side of the triangle in each row

while num_sym >= 0:  # creates the first triangle
    if row_count % 2 == 0:  # even rows
        print(blank * num_blank, first_sym * num_sym, blank * num_blank)  # prints the blanks, symbols and blanks
        num_blank += 1  # adds a blank to each side
        num_sym -= 2  # subtracts two symbols from each row
        row_count += 1  # moves down a row
        continue
    else:  # odd rows
        print(blank * num_blank, second_sym * num_sym, blank * num_blank)
        num_blank += 1
        num_sym -= 2
        row_count += 1
        continue

row_count = 0  # resets the row number
num_sym -= 2
num_blank -= 2

while num_sym >= -1 * ((height * 2) - 1):  # creates the second triangle
    if row_count % 2 == 0:  # even rows
        print(blank * num_blank, first_sym * -num_sym, blank * num_blank)
        num_blank -= 1
        num_sym -= 2
        row_count += 1
        continue
    else:  # odd rows
        print(blank * num_blank, second_sym * -num_sym, blank * num_blank)
        num_blank -= 1
        num_sym -= 2
        row_count += 1
        continue




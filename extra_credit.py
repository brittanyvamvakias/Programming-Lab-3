# File: extra_credit.py
# Author: Brittany Vamvakias
# Date: 02/12/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description:

print("************************************************************       ")
string = input("Enter a string variable: ")
print(f"Length of the string {string} is {len(string)}")
print()

index = 0
while index <= len(string) - 1:
    if len(string) % 2 == 0:
        print(string[index], end=" ")
        print(index, end=" ")
        index += 2
        continue
    else:
        print(string[index + 1], end=" ")
        print(index + 1, end=" ")
        index += 2
        continue



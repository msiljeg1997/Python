
# # Introduction
# # Day 1 - 30DaysOfPython Challenge

# print(2 + 3)   # addition(+)
# print(3 - 1)   # subtraction(-)
# print(2 * 3)   # multiplication(*)
# print(3 / 2)   # division(/)
# print(3 ** 2)  # exponential(**)
# print(3 % 2)   # modulus(%)
# print(3 // 2)  # Floor division operator(//)

# # Checking data types

# print(type(10))                  # Int
# print(type(3.14))                # Float
# print(type(1 + 3j))              # Complex
# print(type('Asabeneh'))          # String
# print(type([1, 2, 3]))           # List
# print(type({'name':'Asabeneh'})) # Dictionary
# print(type({9.8, 3.14, 2.7}))    # Set
# print(type((9.8, 3.14, 2.7)))    # Tuple


# https://www.practicepython.org/

# # vjezba1 Character Input

# from datetime import datetime

# name = input("What is your name? ")
# age = int(input("How old are you? "))
# kojaCeBitGodinaKadCesImatSto = (100 - age) + datetime.now().year
# print(name + " When you will be 100 years old, it's gonna be year " + str(kojaCeBitGodinaKadCesImatSto))

# # vjezba2 Odd or Even

# number = int(input("Enter a number: "))
# if number % 2 == 0:
#     if number % 4 == 0:
#         print(f"{number} is even and a multiple of 4")
#     else:
#         print(f"{number} is even")
# else:
#     print(f"{number} is odd")

# num = int(input("Enter first number: "))
# check =int(input("Enter second number: "))
# if check % num == 0:
#         print("The second number divides evenly with first number")
# else:
#         print("The second number does not divides evenly with first number")

# #vjezba3 List Less Than Ten

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# for element in a:
#     if element < 5:
#         print(element)

# nova_lista = [element for element in a if element < 5]
# print(nova_lista)
# # new_list = creates a new list called new_list that will hold the filtered elements.
# # [ starts a list comprehension, which is a concise way to create a new list in Python.
# # element is the name we give to the variable that represents each element in the original list a.
# # for element in a specifies that we will iterate over each element in the original list a.
# # if element < 5 is a condition that filters the elements. Only elements that are less than 5 will be included in the new list.
# # ] ends the list comprehension.


# num = int(input("Give me some number: "))
# nova_lista_2 = [element for element in a if element < num]
# print(nova_lista_2)

# # vjezba4 Divisors

# num = int(input("Give me some random number: "))
# divisors = []

# for i in range(1, num+1):
#     if num % i == 0:
#         divisors.append(i)
# print("the divisor of ", num, "are:", divisors)

# vjezba5 List Overlap

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# common_list_elements = list(set(a) & set(b))
# print(common_list_elements)

# vjezba6 String Lists

# string = input("Enter a string: ")
# string = string.lower()

# if string == string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

# vjezba7 List Comprehensions

# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# samoEvenNum = [num for num in a if num % 2 ==0]
# print(samoEvenNum)

# vjezba8 Rock Paper Scissors

# print("Welcome to classic rock paper scissors, RULES: type R for rock, P for paper and S for scissors, all invalid inputs wont be processed")

# while True:
#     player_one = input("What do you play PLAYER ONE? ").lower()
#     player_two = input("What do you play PLAYER TWO? ").lower()

#     if player_one not in ["r","p","s"] or player_two not in ["r","p","s"]:
#         print("Invalid input")
#         continue

#     if player_one == player_two:
#         print("Tie!")
#     elif player_one == "r" and player_two == "s":
#         print("Player 1 wins")
#     elif player_one == "s" and player_two == "p":
#         print("Player 1 wins!")
#     elif player_one == "p" and player_two == "r":
#         print("Player 1 wins!")
#     else:
#         print("Player 2 wins!")

#     play_again = input("Do you want to playe again? (y/n)").lower()
#     if play_again != "y":
#         break

#  #vjezba9 guessing game one

# import random

# randomnNum = random.randint(0,9)
# odgovor = int(input("guess what number  "))

# print(randomnNum)

# if odgovor == randomnNum:
#     print("you got it right! nice!")
# else:
#     print("try again!")

# #vjezba10 list overlap again

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,164]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,164]

# new_list = (list(set(a) & set(b)))
# print(new_list)

#vjezba11 check primality functions

# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range (2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# arr = list (range(0,101))
# primes = []
# for el in arr:
#     if is_prime(el):
#         primes.append(el)

# print(primes)

# # In this code, is_prime() is a function that checks whether a given number n is prime or not.
# #  It does so by iterating over all the integers from 2 to the square root of n (inclusive) 
# # and checking if any of them divide n without leaving a remainder. If such a number is found,
# #  then n is not prime, and the function returns False. Otherwise, it returns True.
# # We then create an array arr using the range() function with the argument (0, 101) to generate
# #  a sequence of integers from 0 to 100 (inclusive). We initialize an empty list primes to store
# #  the prime numbers that we find. We then iterate over all the numbers in arr and use the is_prime()
# # function to check if each number is prime. If it is, we add it to the primes list.
# # Finally, we print the primes list to display all the prime numbers in the array.

# vjezba 12 List Ends

# a = [5, 10, 15, 20, 25]

# def firstLast (el):
#     return [el[0], el[-1]]

# novaLista = firstLast(a)
# print(novaLista)

# # vjezba13 Fibonacci Function


# def fibonacci():
#     num = int(input("How many numbers that generates?:"))
#     i = 1
#     if num == 0:
#         fib = []
#     elif num == 1:
#         fib = [1]
#     elif num == 2:
#         fib = [1,1]
#     elif num > 2:
#         fib = [1,1]
#         while i < (num - 1):
#             fib.append(fib[i] + fib[i-1])
#             i += 1
#     return fib
# print(fibonacci())
# input()

## vjezba14 List remove Duplicates Function
# def remove_duplicates(lst):
#     """Return a new list with all duplicates removed."""
#     new_lst = []
#     for item in lst:
#         if item not in new_lst:
#             new_lst.append(item)
#     return new_lst

# # Define a list with duplicates
# my_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]

# # Call the remove_duplicates function to get a new list with duplicates removed
# novaLista = remove_duplicates(my_list)

# # Print the new list
# print(novaLista)  # Output: [1, 2, 3, 4, 5]

## vjezba15 Reverse String

# def reverse_string(string):
#     # Split the string into words
#     varRijec = string.split()
#     # Reverse the order of words
#     varRijec.reverse()
#     # Join the words back into a string
#     reversed_string = " ".join(varRijec)
#     return reversed_string

# # Implimentacija funkcije
# input_string = input("Enter a long string containing multiple words: ")
# reversed_string = reverse_string(input_string)
# print(reversed_string)

## vjezba16 Password Generator

# import random

# def randomPassword(length=10, chars=None):
#     if chars is None:
#         chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%¨&*()_+/*\\|<>;:"
#     password = ""
#     for i in range(length):
#         password += random.choice(chars)
#     return password


# print(randomPassword())
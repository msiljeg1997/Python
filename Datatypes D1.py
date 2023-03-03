
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

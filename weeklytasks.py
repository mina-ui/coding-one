# WEEK 1
# Write a program that outputs “even” if a number is even and “odd” if a number is odd.
# Think about what if the value is neither even nor odd (the value can be fractional or it can even not be a number at all). 
# Hint: you may need to find out how to print a message to the terminal from Python and how to write + run a Python script file. 

# num = int(input("Enter a number:"))

# if num % 2 == 0:
#     print("even")
# elif num % 2 != 0:
#     print("odd")
# else:
#     print("not an integer")
# traceback if you put anything that isn't an int- making else statement pointless

# WEEK 2 TASK 1
# Given 3 positive integers, find the sum of all numbers between the first two that are a multiple of the third
# Eg. Given "1, 10, 2" the expected output is "20"

# a = 1
# b = 10
# c = 2

# sum = 0

# for i in range(a, b):
#     if i % c == 0:
#         sum += i

# print(sum)


# a = int(input("input your first positive integer:"))
# b = int(input("input your second positive integer:"))
# c = int(input("input your third positive integer:"))

# sum = 0

# for n in range(a + b):
#     if n % c == 0:
#         sum += n

# print(sum)
# why doesn't above work?

# WEEK 2 TASK 2
# Given a string of text, print the number of times each letter in the alphabets a-z appear.

# alphabets = "abcdefghijklmnopqrstuvwxyz"
# sentence = "the quick brown fox jumps over the lazy dog"

# for x in alphabets:
#     sum = 0
#     for y in sentence:
#         if x == y:
#             sum += 1
#     print(str(x) + ": " + str(sum))

# WEEK 2 TASK 3
# Implement division as a series of subtraction. 
# The program should only deal with integers and report the remainder if there is one
# I don't know

# WEEK 3 TASK 1
# Make a function that takes two arguments (given name and family name) and print a greeting.
# def first_name(fname):
#      input("Hello, what is your first name?")
# def last_name(lname):
#     input("What is your last name?")

# print("Hello there, " + fname + " " + lname + " nice to meet you!")
# I don't know anythingggg

# WEEK 3 TASK 2
# Write a function that takes an english word and turns it into pig latin
# def pig_latin(text):
#   words = text.split()
#   pigged_text = []

#   for word in words:
#     word = word[1:] + word[0] + 'ay'
#     pigged_text.append(word)

#   return ' '.join(pigged_text)

# print(pig_latin("hello how are you"))

# WEEK 4 TASK 1
# Write a program that given a list of numbers, multiply all numbers in the list
# a = int(input("Give me a number!"))
# b = int(input("Give me another number!"))
# c = int(input("Give me a final number!"))

# x = a * b * c
# for n in x:
#     print(n)
# don't know how to ask for input from user and still get the result below is simplified version:

# def multiply(numbers):
#     total = 1

# for x in numbers:
#     total *= x 

# return total

# print(multiply((9, 10, 3, 5)))

# WEEK 4 TASK 2
# Start with 4 words “comfortable”, “round”, “support”, “machinery”, return a list of all possible 2 word combinations.
# https://blog.enterprisedna.co/how-to-generate-all-combinations-of-a-list-in-python/
# import itertools
# from itertools import permutations 

# list_words = ["comfortable", "round", "support", "machinery"]

# combinations = list(itertools.combinations(list_words, 2))

# print(combinations)

# WEEK 5 TASK 1
# Make a program that uses a lookup table to convert any set of alphabets into their corresponding NATO phonetic alphabets. Also implement the inverse function.
# my_Dict = {
#     "a": "Alpha",
#     "b": "Bravo",
#     "c": "Charlie",
#     "d": "Delta",
#     "e": "Echo",
#     "f": "Foxtrot",
#     "g": "Golf",
#     "h": "Hotel",
#     "i": "India",
#     "j": "Juliett",
#     "k": "Kilo",
#     "l": "Lima",
#     "m": "Mike",
#     "n": "November",
#     "o": "Oscar",
#     "p": "Papa",
#     "q": "Quebec",
#     "r": "Romeo",
#     "s": "Sierra",
#     "t": "Tango",
#     "u": "Uniform",
#     "v": "Victor",
#     "w": "Whiskey",
#     "x": "X-ray",
#     "y": "Yankee",
#     "z": "Zulu"
# }

# SPELL CHECKER- GAVE ON SLACK
# from Levenshtein import distance

# text = open("./cyberspace.txt")
# lines = text.readlines()

# # print(lines)

# # Load in dictionary
# dictionary_file = open("./dictionary.txt")
# dictionary = dictionary_file.readlines()
# for index, word in enumerate(dictionary):
# 	dictionary[index] = word.strip()

# # Split into words
# split_lines = []
# for line in lines:
# 	split_lines.append(line.split(" "))

# # Spellchecking
# for line in split_lines:
# 	for i, word in enumerate(line):
# 		if word.lower().strip() in dictionary or word == "\n":
# 			# Spelled correctly
# 			line[i] = word
# 		else:
# 			# Misspelled
# 			minimum = 3
# 			correct_word = word
# 			for dict_word in dictionary:
# 				final_distance = distance(word.lower(), dict_word)
# 				if minimum > final_distance:
# 					minimum = final_distance
# 					correct_word = dict_word

# 			print(str(minimum) + " " + correct_word)
# 			line[i] = correct_word

# # Output text
# join_lines = []
# for split_line in split_lines:
# 	join_lines.append(" ".join(split_line))

# with open("./corrected.txt", "w") as file:
# 	file.write("".join(join_lines))
# DICE TASK- DONE IN CLASS
# from random import randrange

# class Dices:
#     sides = 6

#     dices = []

#     def __init__(self, number, sides):

#         for i in range(number):

#             self.dices.append(Dice(sides))

#     def roll(self, times=1):

#         result = []
#         # roll multiple times

#         for i in range(times): 

#             for dice in self.dices:

#                 result.append(dice.roll())

#         return result

# pieces = Dices(2, 6)

# print(pieces.roll())
# print(pieces.roll(2))


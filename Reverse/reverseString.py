"""Using lambda function to reverse a string"""

name = input("Enter a word: ")
reverseString = lambda name: print(name[::-1])
reverseString(name)

# Outputs a message to the user
print("This program will accept binary input and generate a corresponding octal and hexadecimal.")
# Get a number from the user
num = input("Please enter a binary number: ")

binary_string = num  # assigns the number to the variable binary_string
# converts the number from a string to an integer(decimal number) and assigns it to decimal_representation
decimal_representation = int(binary_string, 2)

# converts the decimal number to a octal number and assigns it to octal string
octal_string = oct(decimal_representation)
# outputs the octal_string but removes the the two prefixes before the output
print("The octal equivalent of the number is ", str(octal_string).removeprefix('0o'), "\n")

binary_string = num  # assigns the number to the variable binary_string
# converts the number from a string to an integer(decimal number) and assigns it to decimal_representation
decimal_representation = int(binary_string, 2)
# converts the decimal number to a hexadecimal number and assigns it to hexadecimal_string
hexadecimal_string = hex(decimal_representation)
print("The hexadecimal equivalent of the number is ", str(hexadecimal_string).removeprefix('0x').upper())

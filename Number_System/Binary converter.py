print("This program will accept binary input and generate a corresponding octal and hexadecimal.")
num = input("Please enter a binary number: ")

binary_string = num
decimal_representation = int(binary_string, 2)
octal_string = oct(decimal_representation)
print("The octal equivalent of the number is ", str(octal_string).removeprefix('0o'), "\n")

binary_string = num
decimal_representation = int(binary_string, 2)
hexadecimal_string = hex(decimal_representation)
print("The hexadecimal equivalent of the number is ", str(hexadecimal_string).removeprefix('0x').upper())

print("This program will accept a decimal number and generate a corresponding binary, octal and hexadecimal output.")
num = int(input("Please enter a decimal number: "))

def binary(num):
    numBinary = []
    while num > 0:
        binNum = num % 2
        numBinary.append(binNum)
        num = num // 2
    numBinary.reverse()
    print("The binary equivalent of the number ", "is ", end="")
    for i in numBinary:
        print(i, end="")
    print("\n")

def octal(num):
    numOctal = []
    while num > 0:
        octNum = num % 8
        numOctal.append(octNum)
        num = num // 8
    numOctal.reverse()
    print("The octal equivalent of the number ", "is ", end="")
    for i in numOctal:
        print(i, end="")
    print("\n")

def hexa(num):
    numHexa = []
    while num > 0:
        hexaNum = num % 16
        if hexaNum == 10:
            hexaNum = "A"
        elif hexaNum == 11:
            hexaNum = "B"
        elif hexaNum == 12:
            hexaNum = "C"
        elif hexaNum == 13:
            hexaNum = "D"
        elif hexaNum == 14:
            hexaNum = "E"
        elif hexaNum == 15:
            hexaNum = "F"
        numHexa.append(hexaNum)
        num = num // 16
    numHexa.reverse()
    print("The hexadecimal equivalent of the number is ", end="")
    for i in numHexa:
        print(i, end="")
binary(num)
octal(num)
hexa(num)




import random

print("Enter your full name.")
yourName = input(">> ").title().strip()
print("Enter your crush's full name.")
yourCrush = input(">> ").title().strip()

percentage = random.randint(1, 100)

print(f"Percentage of love between {yourName} and {yourCrush}: {percentage}%.")
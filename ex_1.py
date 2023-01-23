"""Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum."""
# user inputs number 1 and number 2
number1 = input("Enter number1: ")
number2 = input("Enter number2: ")
product = int(number1) * int(number2)
sum = int(number1) + int(number2)
if product <= 1000:
    print(product)
else:
    print(sum)

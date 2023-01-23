#!/usr/bin/python
"""Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum."""
def multi_sum(number1, number2):
    # user inputs number 1 and number 2
    number1 = input("Enter number1: ")
    number2 = input("Enter number2: ")
    product = number1 * number2
    sum = number1 + number2
    if product <= 1000:
        return product
    else:
        return sum

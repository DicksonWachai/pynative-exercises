"""Write a program to check if the given number is a palindrome number."""
def palindrome_check(num):
    number = num
    print("orignal number {}".format(num))
    # declare a variable to store the reversed number
    reverse_num = 0
    while num != 0:
        # get the last digit of the number using modulus
        last_digit = num % 10
        # add the last digit to be the first digit of reversed number
        reverse_num = reverse_num * 10 + last_digit
        num //= 10    
    if reverse_num == number:
        print("Yes. {} is a palindrome number".format(number))
    else:
        print("No. {} is not a palindrome number".format(number))
        
palindrome_check(121)
palindrome_check(125)
palindrome_check(202)


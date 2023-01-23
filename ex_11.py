"""Write a Program to extract each digit from an integer in the reverse order."""
def reverse_order(num):
    reverse_order = 0
    while num != 0:
        last_digit = num % 10
        reverse_order = reverse_order * 10 + last_digit
        num //= 10
    for i in str(reverse_order):
        print(int(i), end=' ')
reverse_order(7536)

"""Write a program to accept a string from the user and display characters that are present at an even index number."""
def print_char(string):
    for i in range(len(string)):
        if i % 2 == 0:
            print(string[i])
result = print_char("pynative")

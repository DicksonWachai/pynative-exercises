"""Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number."""
previous_num = 0
for i in range(0, 10):
    sum = previous_num + i
    previous_num = i
    print(sum)

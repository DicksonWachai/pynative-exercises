"""Iterate the given list of numbers and print only those numbers which are divisible by 5"""
def divisible_by_5(my_list=[]):
    print("Given lsit is {}".format(my_list))
    # create a variable n and assign the length of my_list
    n = len(my_list)
    print("Divisible by 5")
    for i in range(n):
        if my_list[i] % 5 == 0:
            print(my_list[i])
divisible_by_5([10, 20, 33, 46, 55])

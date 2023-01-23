"""Write a function to return True if the first and last number of a given list is same. If numbers are different then return False."""
def compare_first_last(my_list=[]):
    n = len(my_list)
    if my_list[0] == my_list[n - 1]:
        print("Given lists: {}".format(my_list))
        print("result is {}".format((my_list[0] == my_list[n-1])))
    else:
        print("my_list = {}".format(my_list))
        print("result is {} ".format((my_list[0] == my_list[n-1])))
compare_first_last([10, 20, 30, 40, 10])
compare_first_last([75, 65, 35, 75, 30])

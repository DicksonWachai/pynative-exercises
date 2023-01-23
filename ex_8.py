"""Print a pattern"""
# use a nested loop 
# the outer loop is for the rows
for i in range(1, 6):
    # the inner loop is for columns
    for j in range(i):
        # displays number
        print(i, end=' ')
    # new line after each row
    print('')

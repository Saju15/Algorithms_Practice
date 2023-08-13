def count(i):
    print(i)
    if i == 1: #base case
        return 
    else:
        count(i-1) #recursive case

count(5)
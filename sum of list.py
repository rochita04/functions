#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20

def sum_list():
    a=[8, 2, 3, 0, 7]
    b=0
    for i in a:
        b=b+i
    return b
        
print(sum_list())

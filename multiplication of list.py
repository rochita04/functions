##Write a Python function to multiply all the numbers in a list.
#Sample List : (8, 2, 3, -1, 7)
#Expected Output : -336


def m_list():
    a=[8, 2, 3, -1, 7]
    b=1
    for i in a:
        b=b*i
    return b
        
print(m_list())

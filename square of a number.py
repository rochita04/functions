#Write a Python function to create and print a list where the values are the squares of numbers between 1 and 30 (both included).


def square():
    a=[]
    for i in range(1,30+1):
        a.append(i*i)
    print(a)

square()
    

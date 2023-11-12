#Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.



def factorial_list(a):
    #a=int(input('enter a number: '))
    b=1
    for i in range(1,a+1):
        b=b*i
    return b
        
print(factorial_list(5))

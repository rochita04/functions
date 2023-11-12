#Write a Python function that takes a number as a parameter and checks whether the number is prime or not.
#Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

def prime(a):
    x=[]
    if a>1:
        for j in range (1,a+1):
            if a%j==0:
              x.append(j)
        if len(x)>2:
                print('not prime')
        else:
            print(a,'is a prime number')
    else:
        print('number should be great then 1')

prime(11)

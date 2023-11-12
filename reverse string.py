
#4. Write a Python program to reverse a string.
#Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse(s):
    #s=input('enter a string: ')
    a=list(s)
    a.reverse()
    b=''.join(a)
    print(b)


reverse('rochita')

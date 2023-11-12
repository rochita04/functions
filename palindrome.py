#Write a Python function that checks whether a passed string is a palindrome or not.
#Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run


def palindrome(s):
    #s=input('enter a string: ')
    a=list(s)
    a.reverse()
    b=''.join(a)
    
    if s==b:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")

palindrome('mom')

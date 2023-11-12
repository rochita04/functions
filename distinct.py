#Write a Python function that takes a list and returns a new list with distinct elements from the first list.
#Sample List : [1,2,3,3,3,3,4,5]
#Unique List : [1, 2, 3, 4, 5]



def distinct():
    a=[]
    n = int(input("Enter number of elements : "))
    for i in range(0, n):
      b= int(input("enter number:"))
      a.append(b)
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
        else:
            continue
    print(b)

distinct()

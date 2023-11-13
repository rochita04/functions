def multiples_of_5():
    a=int(input("enter a number: "))
    b=[]
    for i in range(1,a+1):
        if i%5==0:
            b.append(i)
    print(b)




multiples_of_5()

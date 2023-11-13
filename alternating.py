def alternating():
    lst=[23,32,24,34,26,39]
    a=len(lst)
    lst2=[]
    for i in range(0,a-1,2):
        lst2.append(lst[i])
    print(lst2)

alternating()

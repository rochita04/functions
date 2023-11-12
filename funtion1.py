from multipledispatch import dispatch


@dispatch(int, int)
def func1(a,b):
    return a,b
@dispatch(int, int, int)
def func1(first, second, third):
    return first,second,third

print(*func1(1,2))

print(*func1(3,4,5))

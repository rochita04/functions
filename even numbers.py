#Generate a Python list of all the even numbers between 4 to 30
def even(a,b):
  z=[]
  for i in range(a,b+1):
    z.append(i)
  y=[]
  for j in z:
    if j%2==0:
      y.append(j)
    else:
      continue
  print(y)

even(4,30)

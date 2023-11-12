#Write a Python function to check whether a number falls within a given range

def checknum(b):
  #L=int(input("enter starting of range: "))
  #R=int(input('enter ending of range: '))
  a=[]
  for i in range(1,101):
    a.append(i)
  #b=int(input('enter a number: '))
  if b in a:
    print(b,'falls within the given range')
  else:
    print(b,'does not falls within the given range')


checknum(500)

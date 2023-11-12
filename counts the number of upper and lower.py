#Write a Python function that accepts a string and counts the number of upper and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12


def LOWERorUPPER():
  a=input('enter a string: ')
  b=[]
  c=[]
  for i in a:
    if i.islower()==True:
      b.append(1)
    elif i.isupper()==True:
      c.append(1)
  print('No. of Upper case characters : ',len(c),'and No. of Lower case Characters : ',len(b))

LOWERorUPPER()

#Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.
#Sample Items : green-red-yellow-black-white
#Expected Result : black-green-red-white-yellow

def sort_hyphen():
  a= input("Enter values for the list hyphen by spaces: ")
  list = a.split("-")
  list.sort()
  for i in range(1,len(list)*2-1,2):
    list.insert(i,'-')
  b=''.join(list)
  print(b)

sort_hyphen()

#Write a Python function to check whether a string is a pangram or not.
#Note : Pangrams are words or sentences containing every letter of the alphabet at least once.



def ispangram(input_str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    z = 0
    for i in alphabet:
        j = i.upper()
        if i not in input_str and j not in input_str:
            z = z + 1
            print("Not a pangram")
            break
    
    if z == 0:
        print('Is a pangram')

# Example usage:
ispangram('rochita')

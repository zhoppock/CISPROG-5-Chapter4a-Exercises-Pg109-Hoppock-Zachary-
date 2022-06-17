print("Exercise 1")
def encryption(text):
  print("\nUnencrypted:", text)
  plainText = text
  distance = 3
  code = ""
  for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
      cipherValue = ord('a') + distance - \
      (ord('z') - ordvalue + 1)
    code += chr(cipherValue)
  print("Encrypted:", code)
  return
#a
text = "python"
encryption(text)
#b
text = "hacker"
encryption(text)
#c
text = "wow"
encryption(text)

"""
Exercise 2
In regards to the encryption and decryption of the ASCII table, I believe in order for us to use all possible characters in it we need to remove the if statements in the code, as they are there to prevent the program from using any characters other than lower case letters.

Exercise 3
First of all, we take the decryption program from this section and we turn in into a while loop.  Set the while loop with a value of "no" so it keeps going until you answer the question of "Has this been decrypted?" with the answer "yes".  Within this loop, ask the user for an input of distance that the decryption process should try for each time you need to loop it.  Each loop it will take the distance you gave it and come up with a different set of characters until you are sure you decrypted it correctly.
"""
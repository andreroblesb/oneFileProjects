"""
On this file we will encrypt a message with a key with a one time pad approach.

The one time pad approach is a non-reusable encryption method, which consists on agreeing on a rando key (as random as possible), which then to encode the message, assigning for the encoded symbols each a number. We use the sum of the values of the key and text to encrypt, and then use the substraction of the key from the cyphertext to return to its original value. This method natively uses mod n, where n is the number of symbols.

Instead of creating a dictionary, we use ASCII values to compute substractions. This is, technically, cheaper in memory, however more expensive in computation time. This is done purely because of the fun of it.

It supports basic punctuation, which is not encoded. Honestly adding punctuation would make having a dictionary just more easy at this point. Another convenience is that input is always processed in uppercase (because of ASCII), therefore output is always on uppercase.

"""
import random

def decrypt(cypherText, key):
    cipherText = ""
    for key_char, cipher_char in zip(key, cypherText):
        computed_mod = ((endBase - base) + (ord(cipher_char)-base) - (ord(key_char)-base))  % (endBase - base)
        cipherText += chr(base + computed_mod)
    
    return cipherText

def encrypt(plainText, key):
    cipherText = ""
    for key_char, text_char in zip(key, plainText):
        computed_mod = ((ord(key_char) + ord(text_char)) - (2*base))  % (endBase - base)
        cipherText += chr(base + computed_mod)
    
    return cipherText

def generateKey(n):
    return "".join([chr(random.randint(base, endBase)) for _ in range(n)])

def retainPunctuation(plainText : str):
    indexes = []
    punctuation = []
    cleaned_text = []
    for i, c in enumerate(plainText, start=0):
        if c in (" ", ",", ".", ":", ";", "-"):
            punctuation.append(c)
            indexes.append(i)
        else: 
            cleaned_text.append(c)
            
    return indexes, punctuation, cleaned_text
    
def includePunctuation(plainText : str, indexes, punctuation):
    plainText : list = list(plainText)
    for i, c in zip(indexes, punctuation):
        plainText.insert(i, c)
    return "".join(plainText)
        
def main():
    global base
    global endBase
    base = ord("A")
    endBase = ord("Z")
    
    # Ask for input
    plainText = str(input("Provide the plainText (In English): ")).upper()
    
    # preprocess code
    indexes, punctuation, plainText = retainPunctuation(plainText)
    
    # generate key
    key = generateKey(len(plainText))

    # generate ciphertext
    cipherText = encrypt(plainText, key)
    
    # decrypt ciphertext
    plainText = decrypt(cipherText, key)
    
    # re-process for original input
    original = includePunctuation(plainText, indexes, punctuation)
    print("Bringing back input:", original)
    return

if __name__=="__main__":
    main()
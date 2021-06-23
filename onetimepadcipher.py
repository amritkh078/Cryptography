# Python code to omplement one time pad

def Cypher( text, key ):
    # Returns the Cypher for given string and key 
    answer = "" # the Cypher text
    p = 0 # pointer for the key
    for char in text:
        answer += chr(ord(char) ^ ord(key[p]))
        p += 1
        if p==len(key):
            p = 0
    return answer

                      
MY_KEY = "encryption"
while True:
    PlainText = input("Enter text to encrypt: ")
    # Encrypt
    encrypt = Cypher(PlainText, MY_KEY)
    print("Cypher text: "+encrypt)
    # Decrypt
    decrypt = Cypher(encrypt, MY_KEY)
    print("Decrypt: "+decrypt)
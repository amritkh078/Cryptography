# Python code to implement vigenere cipher

def generate(string,key):
    key = list(key)
    if len(string) == len(key):
        return (key)
    else:
        for i in range(len(string)-len(key)):
         key.append(key[i % len(key)])
    return ("".join(key))

# To encrypt generated text with the help of key

def encrypt(string,key):
    text = []
    for i in range(len(string)):
        a = (ord(string[i])+ord(key[i])) % 26
        a += ord('A')
        text.append(chr(a))
    return ("".join(text))

# To decrypt encrypted text into original text

def decrypt(text,key):
    original_text = []
    for i in range(len(text)):
        b =(ord(text[i])-ord(key[i]) +26) % 26
        b += ord('A')
        original_text.append(chr(b))
    return("".join(original_text))

# Driver code

if __name__ == "__main__":
    string = "VIGENERECIPHER"
    keyword = "ENCRYPT"
    key = generate(string,keyword)
    text = encrypt(string,key)
    print("Cipher text:", text)
    print("Decryptes text:", decrypt(text,key))
    
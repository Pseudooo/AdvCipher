import random

chars = [chr(i) for i in range(32, 127)] # Define character set
print(chars)

# Function to verify that a key is valid
def isKeyValid(key):
    Allowed = "0123456789n#*+-/"
    
    if any(char not in Allowed for char in key):
        return False
    
    try:
        a,b=key.split('#')
        n=1 #declare variable for use in evaluation
        int(eval(a))
        int(eval(b))
        return True
    except:
        return False

def encrypt(PlainText, Key):
    s,r=Key.split('#')
    output=""
    
    CurrentChars = chars[:] # make copy of chars for shuffling
    
    for n in range(len(PlainText)):
        
        s_v=eval(s) % len(chars) #Calc values of s and r for value of n
        r_v=eval(r)
        
        random.seed(r_v) # Shuffle the CurrentChars for random permutation of character set
        random.shuffle(CurrentChars)
        
        CharIndex = (CurrentChars.index(PlainText[n]) + s_v) % len(chars) #Apply shift
        output+=CurrentChars[CharIndex]
        
    print(output)
    
def decrypt(CipherText, Key):
    s,r = Key.split('#')
    output = ""
    
    CurrentChars = chars[:]
    
    for n in range(0, len(CipherText)):
        
        s_v = eval(s) % len(chars)
        r_v = eval(r)
        
        random.seed(r_v)
        random.shuffle(CurrentChars)
        
        CharIndex = (CurrentChars.index(CipherText[n]) - s_v) % len(chars) # Reverse the character shift to the original character
        output+=CurrentChars[CharIndex]
        
    print(output)

# Main Loop
active = True
while(active):
    func = input("> ")
    
    if(func=="encrypt"): #encrypt command run
        key = input("Key: ")
        if(isKeyValid(key) == False):
            print("Invalid key")
            continue
        
        plaintext = input("Plain Text: ")
        encrypt(plaintext, key)
        
    elif(func=="decrypt"):
        key = input("Key: ")
        
        if(isKeyValid(key) == False):
            print("Invalid Key")
            continue
        
        ciphertext = input("Cipher Text: ")
        decrypt(ciphertext, key)
        
        
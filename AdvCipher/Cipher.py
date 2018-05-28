import random

chars = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789 _-.,:;=(){}[]'?!\"\\@#$%&/+*�" #char set

####################################################################################################
######################################################### Encryption Function
def encrypt(plaintext, key):
    
    #Function will encrypt plain text based on a given key
    
    s,r=key.split("#") #Define the s and r functions
    output = ""
    
    for n in range(0, len(plaintext)): #Cycle through characters of input
        
        s_v = eval(s) % len(chars) #Calculate values for s and r based on index
        r_v = eval(r)
        
        alphabet = list(chars) #Define a new alphabet list of characters
        
        random.seed(r_v)
        random.shuffle(alphabet) #Generate the permutation of char set to be used for index n
        
        for c in range(0, len(alphabet)): #Cycle through characters of permutation of alphabet
            
            if plaintext[n]==alphabet[c]: #Message char is same as alphabet char
                
                shift = (s_v + c) % len(chars) #Calcuate shift respective to 0
                output = output + alphabet[shift] #append shifted character to output
                break
            
    return output
####################################################################################################
        
####################################################################################################
######################################################### Decryption Function
def decrypt(ciphertext, key):
    
    #Function will decrypt ciphertext based on a given key
    
    s,r=key.split("#") #Define s and r functions
    output = ""
    
    for n in range(0, len(ciphertext)): #Cycle through characters of ciphertext
        
        s_v = eval(s) % len(chars) #Calculate values of function for index
        r_v = eval(r)
        
        alphabet = list(chars) #Defined alphabet list that can be shuffled
        
        random.seed(r_v) #Generate permutation of char set for index
        random.shuffle(alphabet)
        alphabet = alphabet[::-1] #Reverse for decryption
        
        for c in range(0, len(alphabet)): #Cycle through characters of alphabet permutation
            
            if ciphertext[n]==alphabet[c]:
                
                shift = (s_v+c) % len(chars) #Calculate shift respective to 0
                output = output + alphabet[shift] #append shifted char to output
                break
    
    return output
####################################################################################################

####################################################################################################
######################################################### Character Check
def messageValid(message):
    
    #Function to check that all characters in the message are also in the defined character set
    
    valid = True
    
    for n in range(0, len(message)): #Cycle through letters of the message
        
        found = False #Declare a found variable for letter
        
        for c in range(0, len(chars)): #Cycle through characters of charset
            if message[n]==chars[c]: #letter found
                
                found = True #Declare and break loop
                break
        
        if found==False: #If found is false then character is missing and message can't be encrypted
            valid = False
            break
        
    return valid
####################################################################################################

####################################################################################################
######################################################### Key Check
def keyValid(key):
    
    #Function to check that a key is valid
    
    s=""
    r=""
    try:
        s,r=key.split("#") 
        n=1 #Keys contain a variable n
        eval(s)
        eval(r)
    except:
        return False
    return True
####################################################################################################

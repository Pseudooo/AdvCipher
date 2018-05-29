import random
from pathlib import Path

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
        n=1 #Keys contain a variable n (Hopefully)
        eval(s)
        eval(r)
    except:
        return False
    return True
####################################################################################################

####################################################################################################
######################################################### Encrypt File Method
def encryptFile():
    
    # Function that allows for the encryption of files 
    print("Please note that this will only work for raw text files")
    TargetFile = Path(input("File: ")) #Take File path from user
    if TargetFile.is_file()==False:
        print("The Path you have entered is not valid.") #Invalid file
    else:
        key = input("Key: ") #Take Key
        if keyValid(key)==False:
            print("The Key you have entered is not valid.") #Invalid key
        else:
            print("Reading file...")
            FileObj = open(TargetFile, "r")
            FileLines = FileObj.readlines() #Construct array from lines
            
            print("Selected File has:")
            print(str(len(FileLines)) + " Lines") #Confirmation
            
            if input("Continue? [Y/N] ")=="Y":
                
                for n in range(0,len(FileLines)):
                    FileLines[n]=FileLines[n].strip("\n") #Encrypt lines and update array indexes 1 at a time
                    if(messageValid(FileLines[n])==False):
                        print("Error : Line "+str(n)+" has invalid characters and will not be encrypted "+FileLines[n])
                    else:
                        print("Encrypting Line: "+str(n+1)+"/"+str(len(FileLines)))
                        FileLines[n]=encrypt(FileLines[n], key)+"\n"
                        print("Done!")
                print("File Encryption is done")
                print("Writing to file...")
                FileObj.close()
                FileObj = open(TargetFile, "w+") #Write resultant array to file
                FileObj.writelines(FileLines)
                print("Done!")
    return
####################################################################################################

####################################################################################################
######################################################### Encrypt File Method
def decryptFile():
    
    # Function that allows for the encryption of files 
    print("Please note that this will only work for raw text files")
    TargetFile = Path(input("File: "))
    if TargetFile.is_file()==False:
        print("The Path you have entered is not valid.")
    else:
        key = input("Key: ")
        if keyValid(key)==False:
            print("The Key you have entered is not valid.")
        else:
            print("Reading file...")
            FileObj = open(TargetFile, "r")
            FileLines = FileObj.readlines()
            
            print("Selected File has:")
            print(str(len(FileLines)) + " Lines")
            
            if input("Continue? [Y/N] ")=="Y":
                
                for n in range(0,len(FileLines)):
                    FileLines[n]=FileLines[n].strip("\n")
                    if(messageValid(FileLines[n])==False):
                        print("Error : Line "+str(n)+" has invalid characters and will not be decrypted "+FileLines[n])
                    else:
                        print("Decrypting Line: "+str(n+1)+"/"+str(len(FileLines)))
                        FileLines[n]=decrypt(FileLines[n], key)+"\n"
                        print("Done!")
                print("File Decryption is done")
                print("Writing to file...")
                FileObj.close()
                FileObj = open(TargetFile, "w+")
                FileObj.writelines(FileLines)
                print("Done!")
    return
####################################################################################################

####################################################################################################
######################################################### Main Loop
def loop():
    
    #Loop function that allows users to actually use functions
    
    quitloop = False
    
    while(quitloop==False):
        
        func = input("> ") #Get desired function
        func=func.lower()
        
        if(func=="quit"):
            quitloop = True #Quit Loop
            
        elif(func=="encrypt"): #Encrypting a message
            
            key = input("Key: ") 
            if(keyValid(key) == False): #Validate Key
                print("The key you have entered is invalid.")
            else:
                msg = input("Message: ")
                if(messageValid(msg)==False): #Validate Message
                    print("The message you have entered contains invalid characters.")
                else:
                    print("Your generated ciphertext is: ")
                    print(encrypt(msg, key)) #Return ciphertext
                    
        elif(func=="decrypt"): #Decrypting a message
            
            key = input("Key: ")
            if(keyValid(key) == False): #Validating key
                print("The key you have entered is invalid.")
            else:
                msg = input("Ciphertext: ")
                if(messageValid(msg)==False): #Validating message
                    print("The ciphertext you have entered contains invalid characters.")
                else:
                    print("Your plaintext is: ")
                    print(decrypt(msg, key)) #Return plaintext
                    
        elif(func=="author"): #About me! OwO
            print("Pseudo ~")
            print("GitHub: https://github.com/Pseudooo")
            
        elif(func=="encryptf"):
            encryptFile()
        elif(func=="decryptf"):
            decryptFile()
        else: #Invalid
            print("Invalid Function.")
####################################################################################################
loop()
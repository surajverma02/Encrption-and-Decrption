'''
Topic : Write a program for encrption and decrption of message by ceasar cipher code
''' 

def key():
    input_key = int(input("Enter key : "))
    if input_key>26:
        input_key %= 26
    return input_key

def message():
    input_message = input("Enter message : ")
    return input_message

def translate_text(key,message):
    result = ''
    for ch in message:
        if(ch.isupper()):
            cipher = ord(ch) + key
            if(cipher>90):
                cipher -= 26
            elif(cipher<65):
                cipher += 26
            result += chr(cipher)
        else:
            cipher = ord(ch) + key
            if(cipher>122):
                cipher -= 26
            elif(cipher<97):
                cipher += 26
            result += chr(cipher)
    return result

while(True):
    print("\nChoose for operation : \na. '1' for Encrption \nb. '2' for Decrption \nc. '3' for decrption without key(brute force)\nd.  Enter any key for Exit\n")
    choice = input("Enter your choice : ")

    if(choice=='1'):
        print("Cipher text is : ",translate_text(key(),message()))
    elif(choice=='2'):
        print("Plain text is : ",translate_text(-key(),message()))
    elif(choice=='3'):
        message = message()
        for key in range(26):
            print("Plain text could be",key,translate_text(-key,message),sep=" : ")
    else:
        print("Thanks for use")
        exit()
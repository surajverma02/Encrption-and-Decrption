'''
Topic : Write a program for encrption and decrption of message by rail-fence code
''' 

# Function for input key
def key():
    input_key = int(input("Enter number of key : "))
    return input_key

# Function for input message
def message():
    input_message = input("Enter message : ")
    return input_message

# Function for encrption of plain text into cipher text
def cipher_text(key,message):
    
    # Grid with row = key and column = len(message)
    grid = [['' for i in range(len(message))]for j in range(key)]

    # Initialising row and column to 0
    column,row = 0,0

    # Loop for arranging plain text in grid
    for i in range(len(message)):

        # Replacing with character of message
        grid[row][column] = message[i]

        # Check the direction of the message 
        if(row==0):
            dir_down = True 
        if(row==key-1):
            dir_down = False

        # Update column and row
        column += 1
        if dir_down:
            row += 1
        else :
            row -= 1

    # Resulted text as list
    result = []
    for i in range(key):
        for j in range(column):
            if (grid[i][j]!=""):
                result.append(grid[i][j])
   
    # Return cipher text 
    return "Encrpted message is : " + ("".join(result))

# Function for decrption of cipher text into plain text
def plain_text(key,cipher):
 
    # Grid with row = key and column = len(cipher)
    grid = [['\n' for i in range(len(cipher))]for j in range(key)]
     
    # Initialising row and column to 0
    column,row = 0,0
     
    # Loop for arranging "*" in grid
    for i in range(len(cipher)):

        # Replacing with "*"
        grid[row][column] = '*'

        # Check the direction of the message
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        
        # Update column and row
        column += 1
        if dir_down:
            row += 1
        else:
            row -= 1
             
    # Replace "*" with the cipher text character
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (grid[i][j] == '*') :
                grid[i][j] = cipher[index]
                index += 1
         
    # Resulted text as list
    result = []
    row, column = 0, 0

    for i in range(len(cipher)):

        # Adding character into resulted list
        result.append(grid[row][column])

        # Check the direction of the message
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
        
        # Update row and column
        column += 1
        if dir_down:
            row += 1
        else:
            row -= 1

    # Return plain text
    return "Decrpted message is : " + ("".join(result))

while(True):
    print("\nChoose for operation : \na. '1' for Encrption \nb. '2' for Decrption \nc.  Any key for exit\n")
    choice = input("Enter your choice : ")

    if(choice=='1'):
        print(cipher_text(key(),message()))
    elif(choice=='2'):
        print(plain_text(key(),message()))
    else:
        print("Thanks for use")
        exit()